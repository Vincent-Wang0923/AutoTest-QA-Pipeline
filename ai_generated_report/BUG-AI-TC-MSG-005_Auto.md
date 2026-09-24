# Bug Report: Short Username Is Not Blocked by Frontend Validation and a Registration Request Is Sent

## Title
Registration with a 5-character username submits a request to `/api/register` instead of being blocked by frontend validation with the message "Username must be at least 6 characters".

## Requirement
Per PRD section 3.1 (Registration Rules), the `username` field must have a minimum length of 6 characters. When the length rule is violated, the expected error message is "Username must be at least 6 characters".

## Preconditions
- The application is running with the React frontend and Flask backend.
- The `/register` page is reachable.
- No account with the username `user5` is required for this test, since the input is expected to be rejected before submission.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user5` (5 characters).
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button.

## Expected Result
- Frontend validation blocks the submission.
- No request is sent to `/api/register`.
- The message "Username must be at least 6 characters" is displayed.

## Actual Result
- The frontend did not block the submission.
- A request was sent to `/api/register`.
- The expected validation message was not observed as the blocking behavior.

## Captured Request and Response Evidence
- Expected request on submit: none (`expected_request: false`).
- Observed behavior: a request was sent to `/api/register`.
- No response body or status code was captured in the provided evidence.

## User Impact
Users can submit a username that violates the documented minimum length rule, so the registration form does not enforce the specified constraint at the frontend. This prevents the required validation message from being shown and allows invalid input to reach the backend.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-005.png`