# Bug Report: Registration Fails with HTTP 409 for a New Username

## Title
Registration request returns HTTP 409 instead of HTTP 201 when submitting a username that should be unique.

## Requirement
Per PRD section 3.1, registration requires a unique username with a minimum length of 6 characters. A successful registration is expected to return HTTP 201 and the message "Registration successful". The test case TC-MAP-001 expects the frontend username field to map to the backend `username` field and produce a successful registration.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The `/register` route is reachable.
- The username `user_1790259369` is intended to be a new, unique value.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form using the `Register` button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The response includes the message "Registration successful".
- The application navigates to `/`.

## Actual Result
- The request to `/api/register` returns HTTP 409.
- The test case status is Fail with the error: "Expected HTTP 201, received HTTP 409."
- The observed navigation to `/register` and field entries completed, but the submission did not produce the expected success response.

## Captured Request and Response Evidence
- Action sequence observed:
  - navigate to `/register` (actual path `/register`)
  - fill `username` = `user_1790259369`
  - fill `password` = `Passw0rd!`
- Submit action: button `Register`, endpoint `/api/register`, expected request `true`, expected status `201`, expected messages `["Registration successful"]`, expected path `/`.
- Observed response status: HTTP 409.
- No response body or message content was captured in the provided evidence.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration and does not receive the expected success confirmation or navigation to `/`. The 409 response indicates the backend rejected the request, preventing account creation for this input.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MAP-001.png`