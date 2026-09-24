# Bug Report: Registration Fails with HTTP 409 for a New Username

## Title
Registration of a new account returns HTTP 409 instead of HTTP 201, blocking the login flow.

## Requirement
Per PRD section 3.1, registration requires a unique username of at least 6 characters and a non-empty password. A successful registration is expected to return HTTP 201 with the message "Registration successful" and navigate to "/". The test case TC-LOG-001 expects the registration step to return HTTP 201 before proceeding to login.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at "/register".
- The username `user_1790259369` is intended to be a new, unique account.

## Reproduction Steps
1. Navigate to "/register".
2. Fill the "username" field with `user_1790259369`.
3. Fill the "password" field with `Passw0rd!`.
4. Submit the registration form via the "Register" button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application navigates to "/".
- The subsequent login step with the same credentials returns HTTP 200 with "Login successful".

## Actual Result
- The registration request returned HTTP 409 instead of the expected HTTP 201.
- The test case TC-LOG-001 failed with the error: "Expected HTTP 201, received HTTP 409."
- The login step was not reached.

## Captured Request and Response Evidence
- Action: submit "Register" button, endpoint `/api/register`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- Observed error: "Expected HTTP 201, received HTTP 409."

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete account creation, and therefore cannot proceed to log in. The registration flow is blocked at the first step.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-001.png`