# Bug Report: TC-REG-012 — Registration accepts username shorter than minimum length

## Summary
The registration endpoint accepts a username with a length of 1 character, violating the PRD rule that usernames must be at least 6 characters. The API returns HTTP 201 (Created) instead of the expected HTTP 400 (Bad Request).

## Test Case Details
| Field | Value |
| :--- | :--- |
| **Test Case ID** | TC-REG-012 |
| **Module** | Registration |
| **Severity** | High |
| **Priority** | High |
| **Type** | Functional / Validation |

## Environment
- **Frontend**: React, Ant Design
- **Backend**: Flask, SQLite
- **Endpoint**: Registration API

## Steps to Reproduce
1. Navigate to the registration page (or send a direct request to the registration endpoint).
2. Submit the following payload:
   json
   {
     "username": "a",
     "password": "ValidPass1"
   }
   
3. Observe the HTTP response status and body.

## Expected Result
- **Status**: `400 Bad Request`
- **Behavior**: Registration is rejected.
- **Error Message**: `"Username must be at least 6 characters"`

**PRD Reference (Rule 3.1):**
> `username` — Min length: 6 chars — Length error: "Username must be at least 6 characters"

## Actual Result
- **Status**: `201 Created`
- **Behavior**: The account is created successfully despite the username being only 1 character long.
- **Error Message**: None returned.

## Payload Used
json
{
  "username": "a",
  "password": "ValidPass1"
}


## Impact
- Invalid data is persisted in the database, violating the username length constraint defined in the PRD.
- Downstream systems relying on the 6-character minimum (e.g., login, display, uniqueness checks) may behave unexpectedly.
- Security and data integrity risk: short/weak usernames can be registered.

## Root Cause (Suspected)
The backend validation for the `username` field does not enforce the minimum length of 6 characters before persisting the record. The frontend validation (Ant Design) may also be bypassed when the API is called directly.

## Suggested Fix
1. Add server-side validation in the Flask registration handler to reject usernames with `len(username) < 6`.
2. Return HTTP `400` with the message `"Username must be at least 6 characters"`.
3. Ensure the frontend Ant Design form also enforces the same rule to prevent unnecessary requests.

## Attachments
- Request/Response log for TC-REG-012
- Screenshot of successful registration with 1-character username (if applicable)