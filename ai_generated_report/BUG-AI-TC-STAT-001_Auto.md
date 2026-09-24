# Bug Report: Registration Returns HTTP 409 for a New Username

## Title
Registration with a new username returns HTTP 409 instead of HTTP 201.

## Requirement
Per the PRD Registration Rules (Section 3.1), a username must be unique and have a minimum length of 6 characters. A successful registration is expected to return HTTP 201 and display "Registration successful", then navigate to "/". The conflict message "Username already exists" is reserved for the case where the username is not unique.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at "/register".
- The username `user_1790259369` is not already present in the database.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 201.
- The message "Registration successful" is displayed.
- The application navigates to `/`.

## Actual Result
- The request to `/api/register` returns HTTP 409.
- The expected HTTP 201 was not received.
- The scenario status is Fail.

## Captured Request and Response Evidence
- Endpoint: `/api/register`
- Method: POST (via "Register" button)
- Request payload: `username=user_1790259369`, `password=Passw0rd!`
- Expected status: 201
- Actual status: 409
- Expected message: "Registration successful"

## User Impact
A user attempting to register with a new, valid username cannot complete registration. The frontend receives a conflict response instead of a success response, so the "Registration successful" message and navigation to "/" do not occur.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-001.png`