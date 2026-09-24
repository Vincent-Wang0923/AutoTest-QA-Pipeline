# Bug Report: Registration Fails with HTTP 409 for a New Username

## Title
Registration returns HTTP 409 instead of HTTP 201 when submitting a new username, blocking the failed-login test flow.

## Requirement
Per PRD Section 3.1, registration with a valid unique username (minimum 6 characters) and a non-empty password must succeed. The expected success response is HTTP 201 with the message "Registration successful". The conflict message "Username already exists" applies only when the username is not unique.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is intended to be a new, unique account for this test run.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form using the `Register` button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application navigates to `/`.
- The subsequent login step with an incorrect password returns HTTP 401 and displays "Invalid credentials".

## Actual Result
- The registration request returned HTTP 409 instead of the expected HTTP 201.
- Execution stopped at the registration step, so the login failure path (HTTP 401 / "Invalid credentials") was not reached.
- The reported error is: "Expected HTTP 201, received HTTP 409."

## Captured Request and Response Evidence
- Endpoint: `/api/register`
- Method: POST (triggered by the `Register` button)
- Request payload fields: `username = user_1790259369`, `password = Passw0rd!`
- Expected status: 201
- Actual status: 409
- Expected message: "Registration successful"
- Observed message: not captured in the provided evidence; the only recorded discrepancy is the status code.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration and cannot proceed to the login flow. Because the test case depends on a successful registration before verifying the failed-login behavior, the HTTP 401 handling on the frontend remains unverified.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-004.png`