# Bug Report: Registration Fails with HTTP 409 for a New Username

## Title
Registration returns HTTP 409 instead of HTTP 201 when creating a new account, blocking the login flow.

## Requirement
Per PRD section 3.1, registration with a unique username of at least 6 characters and a non-empty password must succeed. Per section 3.2, login requires credentials that match database records and returns HTTP 200 with "Login successful" on success.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `user_1790259369` is intended to be a new, unique account.
- The registration and login pages are reachable.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form via the `Register` button, which calls `/api/register`.
5. Observe the response status and message.
6. Navigate to `/`.
7. Fill the `username` field with `user_1790259369`.
8. Fill the `password` field with `Passw0rd!`.
9. Submit the login form via the `Login` button, which calls `/api/login`.

## Expected Result
- Step 4: `/api/register` returns HTTP 201 with the message "Registration successful", and the app navigates to `/`.
- Step 9: `/api/login` returns HTTP 200 with the message "Login successful".

## Actual Result
- Step 4: `/api/register` returned HTTP 409 instead of the expected HTTP 201. The test failed with the error: "Expected HTTP 201, received HTTP 409."
- The registration did not complete successfully, so the subsequent login steps could not be validated.

## Captured Request and Response Evidence
- Action: submit registration form, button `Register`, endpoint `/api/register`.
- Expected status: HTTP 201.
- Actual status: HTTP 409.
- Expected message: "Registration successful".
- Actual message: not captured in the provided evidence.
- The execution evidence records only the navigate and fill actions prior to the failure; no request or response body was captured.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete account creation. Because registration fails, the user cannot proceed to log in with those credentials, blocking the end-to-end registration and login flow defined in the PRD.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-002.png`