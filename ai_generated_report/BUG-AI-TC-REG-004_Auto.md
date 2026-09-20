# Bug Report: TC-REG-004 — Duplicate Username Registration Returns 201 Instead of 409

## Summary
When registering a new account with a `username` that already exists in the database, the backend returns **HTTP 201 (Created)** instead of the expected **HTTP 409 (Conflict)**. This violates the uniqueness constraint defined in the PRD and allows duplicate usernames to be created.

## Test Case Information
| Field | Value |
| :--- | :--- |
| **Test Case ID** | TC-REG-004 |
| **Related Requirement** | PRD §3.1 — Registration Rules (username must be unique) |
| **Severity** | High |
| **Priority** | High |
| **Component** | Backend — Registration Endpoint (Flask) |

## Environment
- **Frontend**: React, Ant Design
- **Backend**: Flask, SQLite
- **Test Type**: API / Integration

## Steps to Reproduce
1. Ensure a user with the username `existinguser` already exists in the database.
2. Send a registration request with the following payload:

json
{
  "username": "existinguser",
  "password": "AnotherPass1"
}


3. Observe the HTTP response status code and body.

## Expected Result
- **Status Code**: `409 Conflict`
- **Error Message**: `"Username already exists"`
- The duplicate account should **not** be created.

## Actual Result
- **Status Code**: `201 Created`
- The registration request succeeds and a duplicate account is created (or the existing record is overwritten, depending on implementation).
- No conflict error is returned to the client.

## Evidence
| Field | Value |
| :--- | :--- |
| **Injected Payload** | `{'username': 'existinguser', 'password': 'AnotherPass1'}` |
| **Expected Status** | `409` |
| **Actual Status** | `201` |

## Impact
- **Data Integrity**: Duplicate usernames can exist in the database, breaking the uniqueness constraint required for login and account identification.
- **Security**: Ambiguous account resolution during login could lead to unauthorized access or account takeover scenarios.
- **UX**: Users receive a false success message when attempting to register with an already-taken username.

## Root Cause (Suspected)
The registration handler in the Flask backend likely does not perform a uniqueness check against the `username` column before inserting the new record, or the check is bypassed/incorrectly implemented.

## Suggested Fix
1. In the registration endpoint, query the database for an existing user with the submitted `username` **before** insertion.
2. If a match is found, return `409 Conflict` with the body `{"error": "Username already exists"}`.
3. Optionally, enforce a `UNIQUE` constraint on the `username` column at the database schema level and handle the resulting `IntegrityError` to return the correct status code.

## Attachments
- Request/response logs for the failing test case (to be attached).
- Screenshot of the 201 response (to be attached).