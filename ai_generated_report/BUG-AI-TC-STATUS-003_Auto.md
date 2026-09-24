# Bug Report: Registration returns HTTP 201 instead of expected HTTP 200

## Requirement
Per the test case TC-STATUS-003, the registration endpoint `/api/register` is expected to return HTTP 200 with the message "Registration successful" when a valid username and password are submitted. The subsequent login flow depends on successful registration.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `s200l_1790258466` is not already registered.
- The password `Passw0rd!` satisfies the registration rules (non-empty).

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `s200l_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which calls `/api/register`.
5. Observe the HTTP status code returned by the registration request.

## Expected Result
- The `/api/register` request returns HTTP 200.
- The response includes the message "Registration successful".
- The test proceeds to the login step at `/`.

## Actual Result
- The `/api/register` request returned HTTP 201 instead of HTTP 200.
- The test case failed with the error: "Expected HTTP 200, received HTTP 201."
- The execution stopped after the registration submission; the login steps were not reached.

## Captured Request and Response Evidence
- Action: `submit` on button "Register", endpoint `/api/register`.
- Expected request: true.
- Expected status: 200.
- Observed status: 201.
- Expected message: "Registration successful" (not confirmed in the captured evidence because the status mismatch caused the failure).

## User Impact
The registration flow does not conform to the specified contract for the `/api/register` endpoint. Any client or test that asserts HTTP 200 on successful registration will treat a successful account creation as a failure, blocking the login verification path defined in TC-STATUS-003.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STATUS-003.png`