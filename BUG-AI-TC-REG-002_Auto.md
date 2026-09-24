# Bug Report: Registration Fails with HTTP 409 for New Username

## Requirement
Per PRD section 3.1, registration with a unique username of at least 6 characters and a non-empty password must succeed. Per the test case TC-REG-002, a successful registration is expected to return HTTP 201 with the message "Registration successful" and redirect to "/".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `user_1790259369` is not already present in the database.
- The registration page is reachable at `/register`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application redirects to `/`.

## Actual Result
- The request to `/api/register` returns HTTP 409.
- The test case status is "Fail" with the error: "Expected HTTP 201, received HTTP 409."
- No success message or redirect to `/` was observed.

## Captured Request and Response Evidence
- Action: submit "Register" to endpoint `/api/register`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- No response body or message was captured in the provided evidence.

## User Impact
A new user attempting to register with the username `user_1790259369` cannot complete registration. The flow stops at the registration step, so the subsequent login with the newly created account cannot be performed.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-002.png`