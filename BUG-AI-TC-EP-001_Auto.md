# Registration Fails with HTTP 409 for a New Username

## Requirement
Registration must accept a valid username and password and return HTTP 201 with the message "Registration successful", then navigate to "/". Usernames must be unique; a duplicate username returns HTTP 409 with "Username already exists".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is expected to be available for a new account.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which sends the request to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application navigates to `/`.

## Actual Result
- The request to `/api/register` returns HTTP 409.
- The test case status is Fail with the error: "Expected HTTP 201, received HTTP 409."
- No navigation to `/` is recorded.

## Captured Request and Response Evidence
- Action: submit, button "Register", endpoint `/api/register`, expected request: true, expected status: 201.
- Observed status: 409.
- Expected messages: ["Registration successful"]; no success message was observed.
- Expected path after submit: `/`; actual path after submit is not recorded as `/`.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration and does not reach the post-registration page. The registration flow is blocked for this input.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-EP-001.png`