# Bug Report: Empty Username Submission Does Not Show "Username is required"

## Title
Submitting the registration form with an empty username does not display the expected "Username is required" message.

## Requirement
Per PRD section 3.1, the `username` field is required. The test case TC-REG-004 expects that when the username is left empty and the form is submitted, the message "Username is required" is displayed and no request is sent.

## Preconditions
- The application is running with the React frontend and Flask backend.
- The registration page is reachable at `/register`.

## Reproduction Steps
1. Navigate to `/register`.
2. Leave the `username` field empty.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form using the "Register" button.

## Expected Result
- No request is sent (`expected_request: false`).
- The message "Username is required" is displayed.

## Actual Result
- The message "Username is required" was not displayed.
- The test failed while waiting for the text "Username is required" to become visible, timing out after 5000ms.

## Captured Request and Response Evidence
- No request or response was captured. The test case specified `expected_request: false`, and the failure occurred at the message assertion step before any request evidence could be recorded.

## User Impact
A user who submits the registration form without entering a username receives no visible indication that the username field is required, leaving the form in an unclear state.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-004.png`