# Bug Report: TC-LOG-04 Login with Empty Password Fails Due to Locator Timeout

## Requirement
Login Rules (PRD 3.2): Credentials must match database records. Fail: HTTP 401, show "Invalid credentials". Registration Rules (PRD 3.1) define the password field as required with the null-case message "Password required".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The `/login` page is reachable.
- A user account exists for the username used in the test.

## Reproduction Steps
1. Navigate to `/login`.
2. Fill the "Username" field with value `ok_1790257235`.
3. Clear the "Password" field.
4. Submit by clicking the "Login" button.

## Expected Result
- The form accepts input into the "Username" field.
- On submit with an empty password, no request is sent (`expected_request: false`).
- The message "Password required" is displayed.

## Actual Result
- The test failed during the fill step. The locator `get_by_label("Username", exact=True)` timed out after 5000ms.
- Error: `Locator.fill: Timeout 5000ms exceeded.`
- The only completed action was navigation, which reached `/login` as expected.
- The username was never entered, the password was never cleared, and the form was never submitted. No validation message was observed.

## Captured Request and Response Evidence
- No HTTP request or response was captured. The failure occurred before submission, and the test case specifies `expected_request: false`.

## User Impact
The test could not verify the empty-password validation path. Because the "Username" field could not be located by its label, the intended validation behavior for an empty password remains unverified for this scenario.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-04.png`