# Bug Report: TC-REG-06 - Empty Password Registration Test Fails with Endpoint Error

## Requirement
Per PRD section 3.1, the password field is required and cannot be empty. Submitting the registration form with an empty password must be rejected with the error message "Password required".

## Preconditions
- The registration page is reachable at `/register`.
- The registration form is available for input.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with value `nopass_1790257235`.
3. Clear the `password` field.
4. Submit the form by clicking the `Register` button.

## Expected Result
- No request is sent to the backend (`expected_request: false`).
- The form displays the validation message "Password required".

## Actual Result
- The test case failed with the error `'endpoint'`.
- Execution stopped after the `clear` action on the `password` field.
- The `submit` action was not executed, so no validation message was observed and no request behavior could be confirmed.

## Captured Request and Response Evidence
- No HTTP request or response was captured. The test aborted before the submit step, so the expected absence of a request could not be verified.

## User Impact
The empty-password validation path could not be verified. It is unknown whether a user submitting an empty password receives the required "Password required" message or whether the form incorrectly proceeds. This leaves the required validation behavior unconfirmed.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-06.png`