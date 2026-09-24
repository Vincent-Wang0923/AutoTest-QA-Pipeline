# Bug Report: Registration Fails with HTTP 409 for a New Username During Login Exception Test

## Requirement
Per PRD section 3.1, registration with a unique username of at least 6 characters and a non-empty password must succeed. Per PRD section 3.2, login with credentials that do not match database records must return HTTP 401 and display "Invalid credentials".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `user_1790259369` is intended to be newly registered as part of this test case.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form (button: `Register`, endpoint: `/api/register`).
5. Navigate to `/`.
6. Fill the `username` field with `user_1790259369`.
7. Fill the `password` field with `WrongPass1`.
8. Submit the login form (button: `Login`, endpoint: `/api/login`).

## Expected Result
- Step 4: The registration request returns HTTP 201 with the message "Registration successful", and the app navigates to `/`.
- Step 8: The login request returns HTTP 401 with the message "Invalid credentials", and the app remains on `/`.

## Actual Result
- Step 4: The registration request returned HTTP 409 instead of the expected HTTP 201. The test case failed at this step with the error: "Expected HTTP 201, received HTTP 409."
- Steps 5 through 8 were not executed because the test aborted after the registration failure.

## Captured Request and Response Evidence
- Action: navigate to `/register` — expected path `/register`, actual path `/register`.
- Action: fill `username` = `user_1790259369` — completed.
- Action: fill `password` = `Passw0rd!` — completed.
- Action: submit `Register` to `/api/register` — expected status 201, actual status 409.
- No request or response payload was captured in the provided evidence.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration and receives an HTTP 409 response instead of the expected success response. Because registration did not succeed, the subsequent login-with-wrong-password scenario could not be validated in this run.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-002.png`