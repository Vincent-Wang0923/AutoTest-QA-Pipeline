# Bug Report: Registration Returns HTTP 201 Instead of Expected HTTP 200

## Requirement
Per the test case TC-REG-001, a successful registration with a valid unique username and password must return HTTP 200 with the message "Registration successful".

## Preconditions
- The application is running with the React frontend and Flask backend.
- The username `user_1790258466` does not already exist in the database.
- The registration page is reachable at `/register`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which calls `POST /api/register`.

## Expected Result
- The registration request returns HTTP status 200.
- The response includes the message "Registration successful".

## Actual Result
- The registration request returns HTTP status 201.
- The test case status is Fail with the error: "Expected HTTP 200, received HTTP 201."

## Captured Request and Response Evidence
- Action: navigate to `/register` — expected path `/register`, actual path `/register`.
- Action: fill `username` with `user_1790258466`.
- Action: fill `password` with `Passw0rd!`.
- Action: submit "Register" to endpoint `/api/register`.
- Observed response status: HTTP 201 (expected HTTP 200).

## User Impact
The registration flow does not conform to the specified success contract. Any client or test that asserts HTTP 200 on successful registration will treat a valid registration as a failure, which can block downstream flows that depend on the documented success response.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-001.png`