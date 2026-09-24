# Bug Report: TC-LOG-005 - Login with Empty Password Does Not Show Expected Validation Message

## Requirement
Per PRD section 3.2 (Login Rules), credentials must match database records. The generated test case TC-LOG-005 specifies that submitting the login form with a username and an empty password should not trigger a request (`expected_request: false`) and should display the message "Password is required".

## Preconditions
- The application is running and reachable at the root path `/`.
- The login form is available on the root page.
- A username value is available for input (`logep_1790261464`).

## Reproduction Steps
1. Navigate to `/`.
2. Fill the `username` field with the value `logep_1790261464`.
3. Leave the `password` field empty.
4. Submit the form using the `Login` button.
5. Observe whether the message "Password is required" is displayed.

## Expected Result
- No login request is sent (`expected_request: false`).
- The message "Password is required" is displayed on the page.

## Actual Result
- The expected message "Password is required" was not displayed.
- The test failed with a locator timeout: `Locator.wait_for: Timeout 5000ms exceeded` while waiting for `get_by_text("Password is required", exact=True)` to become visible.
- The navigation step completed successfully (`expected_path: /`, `actual_path: /`), and the username field was filled as specified.

## Captured Request and Response Evidence
- No network request or response was captured in the provided evidence. The test case specified `expected_request: false`, and the evidence log contains only the `navigate` and `fill` actions. No request/response data is available to report.

## User Impact
A user who submits the login form with an empty password does not receive the expected "Password is required" feedback. The absence of this message leaves the user without the specified validation guidance for the empty password field.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-005.png`