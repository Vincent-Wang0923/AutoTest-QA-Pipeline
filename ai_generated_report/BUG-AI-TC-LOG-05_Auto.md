# Bug Report: TC-LOG-05 - Login with empty username fails due to missing Username field locator

## Requirement
Login Rules (PRD Section 3.2): Credentials must match database records. Fail: HTTP 401, show "Invalid credentials". The test case TC-LOG-05 additionally expects that submitting the login form with an empty username and a filled password triggers the message "Username required" and does not send a request.

## Preconditions
- The application is running with the React frontend and Flask backend.
- The `/login` page is reachable.
- The test navigates to `/login` before interacting with the form.

## Reproduction Steps
1. Navigate to `/login`.
2. Clear the `username` field.
3. Fill the `password` field with `Pass1234`.
4. Submit the form using the `Login` button.

## Expected Result
- The `username` field is located and cleared successfully.
- On submit, no request is sent (`expected_request: false`).
- The message "Username required" is displayed.

## Actual Result
- The test failed during the `clear` action on the `username` field.
- Error: `Locator.clear: Timeout 5000ms exceeded.`
- Call log: `waiting for get_by_label("Username", exact=True)`.
- The only completed action was navigation, which succeeded (`expected_path: /login`, `actual_path: /login`).
- The form was never submitted, so no request/response was captured and no validation message was observed.

## Captured Request and Response Evidence
- No HTTP request or response was captured. Execution stopped before the submit step because the `username` field locator could not be resolved.

## User Impact
The test case cannot verify the empty-username login behavior. It is unknown from this execution whether the application displays "Username required" or blocks the request when the username is empty. The validation path for this scenario remains unverified.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-05.png`