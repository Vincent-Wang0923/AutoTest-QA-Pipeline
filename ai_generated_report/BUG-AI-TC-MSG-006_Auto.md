# Bug Report: Registration returns HTTP 201 instead of HTTP 200

## Title
Registration endpoint returns HTTP 201 while the test case expects HTTP 200.

## Requirement
Per the generated test case TC-MSG-006, the registration submission to `/api/register` is expected to return HTTP 200 with the message "Registration successful". The PRD does not explicitly specify the registration success status code; the expected status is defined by the test case.

## Preconditions
- The application is running and reachable.
- The username `msg6_1790258466` is not already registered.
- The registration page is accessible at `/register`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `msg6_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the "Register" button, which posts to `/api/register`.

## Expected Result
- The registration request returns HTTP 200.
- The response contains the message "Registration successful".
- Execution proceeds to the login step of TC-MSG-006.

## Actual Result
- The registration request returned HTTP 201.
- The test case failed with the error: "Expected HTTP 200, received HTTP 201."
- The execution did not proceed to the login step; only the navigation and fill actions were recorded before failure.

## Captured Request and Response Evidence
- Endpoint: `/api/register`
- Method: POST (via "Register" button submit)
- Request payload: `username=msg6_1790258466`, `password=Passw0rd!`
- Expected status: 200
- Actual status: 201
- Expected message: "Registration successful"

## User Impact
The registration flow does not conform to the status code defined in the test case, which blocks verification of the subsequent login failure message scenario (TC-MSG-006). Whether end users are affected cannot be determined from the available evidence, since the response body and UI behavior after the 201 response were not captured.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-006.png`