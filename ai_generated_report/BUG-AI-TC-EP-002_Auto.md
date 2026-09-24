# Bug Report: Registration Fails with HTTP 409 for a New Username

## Requirement
Per PRD section 3.1, registration must succeed for a valid, unique username of at least 6 characters and a non-empty password. The test case TC-EP-002 expects the registration request to `/api/register` to return HTTP 201 with the message "Registration successful".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is intended to be a new, unique account.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form (button: `Register`, endpoint: `/api/register`).

## Expected Result
- The registration request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application navigates to `/`.

## Actual Result
- The registration request returned HTTP 409 instead of the expected HTTP 201.
- Execution stopped at the registration step; the subsequent login steps were not reached.
- Reported error: "Expected HTTP 201, received HTTP 409."

## Captured Request and Response Evidence
- Action: submit registration form.
- Endpoint: `/api/register`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- Observed message: not captured in the provided evidence.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete account creation, so the login flow that depends on this account cannot be executed. The test scenario TC-EP-002 fails at the registration step.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-EP-002.png`