# Bug Report: TC-REG-024 — Duplicate Username Registration Returns 201 Instead of 409

## Summary
When registering a new account with a `username` that already exists in the database, the API returns **HTTP 201 (Created)** instead of the expected **HTTP 409 (Conflict)**. This allows duplicate usernames to be created, violating the uniqueness constraint defined in PRD §3.1.

## Test Case Reference
- **Test Case ID:** TC-REG-024
- **Related Requirement:** PRD §3.1 — Registration Rules (`username` must be unique; Conflict error message: *"Username already exists"*)

## Environment
- **Frontend:** React + Ant Design
- **Backend:** Flask + SQLite
- **Endpoint:** `POST /register` (registration endpoint)

## Steps to Reproduce
1. Ensure a user with `username = "validuser"` already exists in the SQLite database.
2. Send a registration request with the following payload:

   json
   {
     "username": "validuser",
     "password": "ValidPass1"
   }
   

3. Observe the HTTP response status code and body.

## Test Data
| Field | Value |
| :--- | :--- |
| username | `validuser` (already exists) |
| password | `ValidPass1` |

## Expected Result
- **HTTP Status:** `409 Conflict`
- **Response Body:** Error message `"Username already exists"`
- No new user record should be created in the database.

## Actual Result
- **HTTP Status:** `201 Created`
- A duplicate user record is created (or the request is incorrectly treated as a successful registration).
- The uniqueness validation rule for `username` is not enforced.

## Severity
**High** — Violates a core data-integrity constraint (username uniqueness) and permits duplicate accounts, which can lead to authentication ambiguity and data corruption.

## Priority
**High** — Must be fixed before release, as it directly contradicts PRD §3.1.

## Impact
- Duplicate usernames can exist in the database, breaking the login flow (PRD §3.2), which assumes unique credential matching.
- Users may be unable to log in reliably if multiple records share the same username.
- Downstream features relying on unique user identity (e.g., `user_id` mapping) may behave unpredictably.

## Possible Cause (Hypothesis)
- The backend registration handler does not perform a pre-insert uniqueness check on `username`.
- The database schema may be missing a `UNIQUE` constraint on the `username` column.
- The conflict branch (returning `409` with `"Username already exists"`) may be missing or unreachable in the Flask route logic.

## Suggested Fix
1. Add a `UNIQUE` constraint to the `username` column in the SQLite schema.
2. In the Flask registration handler, query for an existing user with the submitted `username` before insertion.
3. If a match is found, return:
   json
   { "error": "Username already exists" }
   
   with HTTP status `409`.
4. Add a regression test (extend TC-REG-024) to assert the `409` response on duplicate registration.

## Attachments / Evidence
- Request payload: `{'username': 'validuser', 'password': 'ValidPass1'}`
- Expected status: `409`
- Actual status: `201`