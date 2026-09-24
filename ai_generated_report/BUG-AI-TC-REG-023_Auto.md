# Bug Report: TC-REG-023 — Stored XSS via Username Field During Registration

## Summary
The registration endpoint accepts a username containing an HTML/JavaScript payload (`<script>alert(1)</script>`) and returns **HTTP 201 Created** instead of rejecting the request with **HTTP 400 Bad Request**. This violates the PRD's registration validation rules and introduces a **Stored Cross-Site Scripting (XSS)** vulnerability.

## Test Case Reference
- **Test Case ID:** TC-REG-023
- **Related PRD Section:** 3.1 Registration Rules

## Environment
- **Frontend:** React, Ant Design
- **Backend:** Flask, SQLite
- **Endpoint:** Registration (`POST /register` or equivalent)

## Steps to Reproduce
1. Navigate to the registration page.
2. Submit the following payload:

   json
   {
     "username": "<script>alert(1)</script>",
     "password": "ValidPass1"
   }
   

3. Observe the HTTP response status and the persisted record.

## Test Data
| Field | Value |
| :--- | :--- |
| username | `<script>alert(1)</script>` |
| password | `ValidPass1` |

## Expected Result
- **HTTP Status:** `400 Bad Request`
- The username should be rejected because it violates the PRD validation rules:
  - The value does **not** satisfy the minimum length rule for a valid username (6+ characters of valid input).
  - The value contains unsafe characters (HTML/JS) that must be sanitized or rejected.
- Appropriate error message returned (e.g., `"Username must be at least 6 characters"` or a validation error for invalid characters).
- No record should be created in the database.

## Actual Result
- **HTTP Status:** `201 Created`
- The account is created successfully with the malicious username stored in the SQLite database.
- No validation error is returned.

## Severity
**Critical**

## Priority
**High**

## Impact
- **Security:** Stored XSS — the injected `<script>` payload may execute in the browser of any user (or admin) who views the affected username, leading to session hijacking, credential theft, or arbitrary script execution.
- **Data Integrity:** Invalid and unsafe data is persisted in the database, violating PRD Rule 3.1.
- **Compliance:** Direct violation of the documented validation rules for the `username` field.

## Root Cause (Suspected)
- The backend does not enforce the minimum-length constraint correctly (the payload length check may be bypassed or not applied).
- Input is not sanitized or escaped before being persisted and/or rendered.
- The frontend (React/Ant Design) does not block or warn on unsafe characters before submission.

## Suggested Fix
1. Enforce server-side validation on the `username` field:
   - Reject values shorter than 6 valid characters.
   - Reject or sanitize values containing HTML/script characters (`<`, `>`, `"`, `'`, etc.).
2. Return `400 Bad Request` with the appropriate PRD-defined error message.
3. Escape all user-supplied data on output (React auto-escapes by default — verify no `dangerouslySetInnerHTML` is used).
4. Add regression tests covering XSS payloads in the `username` field.

## Attachments
- Request payload: `{'username': '<script>alert(1)</script>', 'password': 'ValidPass1'}`
- Response status: `201 Created` (expected `400 Bad Request`)