# Bug Report: Login with Non-Existent Username Does Not Return Expected 401 Response

## Requirement
Per PRD section 3.2 (Login Rules): when credentials do not match database records, the system must fail with HTTP 401 and display "Invalid credentials".

## Preconditions
- The application is running and reachable at the root path `/`.
- The username `missing_1790257888` does not exist in the database.
- The login form is accessible.

## Reproduction Steps
1. Navigate to `/`.
2. Fill the `username` field with `missing_1790257888`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the login form via the `Login` button, which posts to `/login`.

## Expected Result
- The `/login` request is sent.
- The server responds with HTTP status 401.
- The message "Invalid credentials" is displayed.
- The user remains on path `/`.

## Actual Result
- The test failed with the error: `Timeout 10000ms exceeded while waiting for event "response"`.
- No response event was captured for the `/login` request within the 10000ms timeout.
- The navigation and both field-fill actions completed successfully, but the expected response was never observed.
- As a result, the expected HTTP 401 status and the "Invalid credentials" message were not verified.

## Captured Request and Response Evidence
- Actions completed before failure:
  - `navigate` to `/` (expected path `/`, actual path `/`).
  - `fill` `username` = `missing_1790257888`.
  - `fill` `password` = `Passw0rd!`.
- Expected request: submit to endpoint `/login` (`expected_request: true`).
- Expected status: 401.
- Expected message: "Invalid credentials".
- Observed: no response event received; timeout after 10000ms.

## User Impact
A user attempting to log in with a non-existent username does not receive the required failure response within the expected time. The login attempt does not produce the specified HTTP 401 outcome or the "Invalid credentials" message, so the user cannot confirm whether the login failed as defined by the requirement.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-003.png`