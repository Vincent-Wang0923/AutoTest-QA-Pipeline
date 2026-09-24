# Bug Report: Registration Returns HTTP 201 Instead of HTTP 200

## Title
Registration endpoint returns HTTP 201 on successful account creation, but the test case expects HTTP 200.

## Requirement
Per the generated test case TC-FLOW-002, the registration submission to `/api/register` is expected to return HTTP status 200 with the message "Registration successful". The PRD (Section 3.1) defines registration validation rules and error messages but does not specify the success status code.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `flow2_1790258466` has not been registered previously.
- The browser is on the `/register` page.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `flow2_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button, which posts to `/api/register`.
5. Observe the HTTP response status.

## Expected Result
- The request to `/api/register` returns HTTP status 200.
- The response includes the message "Registration successful".

## Actual Result
- The request to `/api/register` returns HTTP status 201.
- The test case failed with the error: "Expected HTTP 200, received HTTP 201."

## Captured Request and Response Evidence
The execution evidence records the following completed actions prior to the failure:
- `navigate` to `/register` (expected path `/register`, actual path `/register`).
- `fill` field `username` with value `flow2_1790258466`.
- `fill` field `password` with value `Passw0rd!`.

The submission step to `/api/register` produced HTTP 201 instead of the expected HTTP 200. No response body content beyond the status code is captured in the provided evidence.

## User Impact
The registration flow does not conform to the status code defined in the test case. Any client logic that checks for HTTP 200 on registration success would treat a 201 response as unexpected, potentially preventing the user from proceeding to login even though the account may have been created.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-FLOW-002.png`