# Bug Report: Registration returns HTTP 201 instead of expected HTTP 200

## Requirement
Per the test case TC-FLOW-001, the registration submission to `/api/register` is expected to return HTTP 200 with the message "Registration successful". The PRD does not explicitly specify the registration success status code, but the test case defines HTTP 200 as the expected status for this endpoint.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `e2e_1790258466` is not already registered.
- The `/register` page is reachable.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `e2e_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which posts to `/api/register`.

## Expected Result
- The `/api/register` request returns HTTP 200.
- The response includes the message "Registration successful".
- The flow proceeds to the login step.

## Actual Result
- The `/api/register` request returns HTTP 201.
- The test case fails with the error: "Expected HTTP 200, received HTTP 201."
- The subsequent login step was not executed because the flow halted at the registration assertion.

## Captured Request and Response Evidence
- Request: POST to `/api/register` with `username=e2e_1790258466` and `password=Passw0rd!`.
- Response: HTTP 201 (expected HTTP 200).
- The execution log records the following completed actions before failure:
  - navigate to `/register` (actual path `/register`)
  - fill `username` = `e2e_1790258466`
  - fill `password` = `Passw0rd!`

## User Impact
The end-to-end register-then-login flow cannot be validated as specified. Any client or test that asserts HTTP 200 on successful registration will treat a successful account creation as a failure, blocking verification of the login step and the surfacing of `user_id`.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-FLOW-001.png`