# Bug Report: Registration Returns HTTP 201 Instead of Expected HTTP 200

## Requirement
Per the test case TC-STATUS-004, the registration endpoint `/api/register` is expected to return HTTP 200 with the message "Registration successful" upon a valid submission. The subsequent login attempt with incorrect credentials is expected to return HTTP 401 with the message "Invalid credentials".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `s401_1790258466` does not already exist in the database.
- The registration page is reachable at `/register`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `s401_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form (button: "Register", endpoint: `/api/register`).
5. Observe the HTTP status code returned by the registration request.

## Expected Result
- The registration request to `/api/register` returns HTTP 200.
- The response includes the message "Registration successful".
- The test proceeds to the login step, where submitting `s401_1790258466` with password `WrongPass1` returns HTTP 401 with the message "Invalid credentials".

## Actual Result
- The registration request returned HTTP 201 instead of the expected HTTP 200.
- Execution halted at the registration step with the error: "Expected HTTP 200, received HTTP 201."
- The login step (HTTP 401 handling) was not reached, so the original scenario objective was not validated.

## Captured Request and Response Evidence
- Endpoint invoked: `/api/register`
- Method: POST (form submission via "Register" button)
- Request payload fields: `username=s401_1790258466`, `password=Passw0rd!`
- Expected status: 200
- Actual status: 201
- Expected message: "Registration successful"
- Observed message: not captured in the provided evidence

## User Impact
The registration flow does not conform to the status code defined in the test case. Because the test aborts at the registration step, the intended verification of the frontend's handling of an HTTP 401 login response could not be completed. Whether the frontend correctly displays "Invalid credentials" on a failed login remains unverified.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STATUS-004.png`