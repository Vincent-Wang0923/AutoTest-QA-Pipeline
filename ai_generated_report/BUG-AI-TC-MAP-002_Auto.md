# Bug Report: Registration Fails with HTTP 409 for a New Username

## Title
Registration returns HTTP 409 instead of HTTP 201 when submitting a new username during the TC-MAP-002 login mapping flow.

## Requirement
Per PRD Section 3.1, registration requires a unique username of at least 6 characters and a non-empty password. A successful registration is expected to return HTTP 201 with the message "Registration successful" and redirect to "/". The test case TC-MAP-002 expects the registration step to succeed so the subsequent login step can be validated.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is intended to be a new account for this test run.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form using the "Register" button, which posts to `/api/register`.

## Expected Result
- The registration request is sent to `/api/register`.
- The backend responds with HTTP 201.
- The UI displays "Registration successful".
- The application navigates to `/`.
- The test then proceeds to the login step.

## Actual Result
- The registration request returned HTTP 409.
- The expected HTTP 201 was not received.
- The test case failed at the registration step with the error: "Expected HTTP 201, received HTTP 409."
- The subsequent login step was not reached.

## Captured Request and Response Evidence
- Action: submit "Register" to endpoint `/api/register`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- Observed error: `Expected HTTP 201, received HTTP 409.`

The evidence log records the following completed actions before failure:
- navigate to `/register` (expected `/register`, actual `/register`)
- fill `username` = `user_1790259369`
- fill `password` = `Passw0rd!`

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration and cannot proceed to log in. The registration flow is blocked at the point of submission, preventing the account creation and the downstream login validation covered by TC-MAP-002.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MAP-002.png`