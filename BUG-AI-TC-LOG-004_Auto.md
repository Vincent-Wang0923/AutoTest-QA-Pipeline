# Bug Report: Missing "Username is required" Validation Message on Login with Empty Username

## Requirement
Per the PRD, login requires credentials to match database records. The test case TC-LOG-004 specifies that submitting the login form with an empty username and a filled password must not trigger a request and must display the message "Username is required".

## Preconditions
- The application is running and reachable at the root path `/`.
- The login form is available on the root page.

## Reproduction Steps
1. Navigate to `/`.
2. Fill the `password` field with value `Passw0rd!`.
3. Leave the `username` field empty.
4. Submit the form using the `Login` button.

## Expected Result
- No network request is sent (per test case `expected_request: false`).
- The message "Username is required" is displayed.

## Actual Result
- The message "Username is required" was not displayed.
- The test failed with a locator timeout: `Locator.wait_for: Timeout 5000ms exceeded` while waiting for `get_by_text("Username is required", exact=True)` to become visible.

## Captured Request and Response Evidence
- No request or response was captured. The test case specifies `expected_request: false`, and the execution evidence records only the `navigate` and `fill` actions, with no submit or network activity logged.

## User Impact
A user who submits the login form with an empty username receives no visible validation feedback indicating that the username field is required, leaving the reason for the failed submission unclear.

## Evidence
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-004.png`