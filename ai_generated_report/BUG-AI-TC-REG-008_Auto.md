# Bug Report: TC-REG-008 — Registration accepts username shorter than minimum length

## Summary
During execution of test case **TC-REG-008**, the registration endpoint accepted a payload containing a username that violates the minimum length requirement defined in the PRD. The API returned **HTTP 201 (Created)** instead of the expected **HTTP 400 (Bad Request)**, allowing an invalid account to be created.

## Test Case Details
| Field | Value |
| :--- | :--- |
| **Test Case ID** | TC-REG-008 |
| **Module** | Registration |
| **Related PRD Rule** | 3.1 Registration Rules — `username` (Min length: 6 chars) |
| **Severity** | High |
| **Priority** | High |
| **Type** | Functional / Validation |

## Environment
- **Frontend**: React + Ant Design
- **Backend**: Flask
- **Database**: SQLite

## Steps to Reproduce
1. Navigate to the registration page/endpoint.
2. Submit a registration request with the following payload:
   json
   {
     "username": "user1",
     "password": "ValidPass1"
   }
   
3. Observe the HTTP response status and body.

## Test Data
| Field | Value | Notes |
| :--- | :--- | :--- |
| `username` | `user1` | 5 characters — violates the "Min length: 6 chars" rule |
| `password` | `ValidPass1` | Valid, non-empty |

## Expected Result
- **HTTP Status**: `400 Bad Request`
- **Behavior**: The account should **not** be created.
- **Error Message**: `"Username must be at least 6 characters"` (per PRD §3.1)

## Actual Result
- **HTTP Status**: `201 Created`
- **Behavior**: The account was successfully created with an invalid username (`user1`), bypassing the minimum length validation.
- **Error Message**: None returned.

## Impact
- **Security / Data Integrity**: Invalid accounts can be created, polluting the user database with usernames that do not conform to the defined schema.
- **Consistency**: Downstream systems (login, profile display, uniqueness checks) may rely on the 6-character minimum assumption and behave unexpectedly.
- **PRD Compliance**: Direct violation of PRD §3.1 Registration Rules.

## Root Cause (Suspected)
The backend registration handler in Flask appears to be missing (or incorrectly implementing) the minimum length validation for the `username` field before persisting the record to SQLite. The uniqueness check may also be affected if it runs after length validation is skipped.

## Suggested Fix
1. Add/restore server-side validation in the registration endpoint:
   python
   if not username or len(username) < 6:
       return {"error": "Username must be at least 6 characters"}, 400
   
2. Ensure validation runs **before** any database write.
3. Add a corresponding unit/integration test asserting HTTP 400 for usernames with length < 6.
4. Optionally mirror the rule on the frontend (Ant Design form rule) for better UX, but the backend must remain the source of truth.

## Attachments
- Request payload: `{'username': 'user1', 'password': 'ValidPass1'}`
- Expected status: `400`
- Actual status: `201`