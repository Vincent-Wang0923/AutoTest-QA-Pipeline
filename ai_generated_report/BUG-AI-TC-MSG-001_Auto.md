# Registration Fails with HTTP 409 for a New Username

## Requirement
Per PRD section 3.1, registration must create an account when the username is at least 6 characters and unique. A successful registration is expected to return HTTP 201 and display "Registration successful".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is intended to be a new, unique account.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button, which calls `POST /api/register`.

## Expected Result
- The request to `POST /api/register` returns HTTP 201.
- The response includes the message "Registration successful".
- The user is redirected to `/`.

## Actual Result
- The request to `POST /api/register` returns HTTP 409.
- The test case status is Fail with the error: "Expected HTTP 201, received HTTP 409."
- No success message is shown, and the expected redirect to `/` does not occur.

## Captured Request and Response Evidence
- Action: submit `Register` button
- Endpoint: `POST /api/register`
- Expected status: 201
- Actual status: 409
- Expected message: "Registration successful"
- Expected path after submit: `/`
- Actual path after submit: not reached (remained on `/register`)

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration. The account is not created, the success message is not displayed, and the user is not redirected to the home page.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-001.png`