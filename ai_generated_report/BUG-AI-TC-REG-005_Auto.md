# Bug Report: Registration with 5-Character Username Sends Request Instead of Showing Validation Error

## Requirement
Per PRD Section 3.1 (Registration Rules), the `username` field must have a minimum length of 6 characters. When the length constraint is violated, the frontend must display the error message "Username must be at least 6 characters" and must not submit the registration request.

## Preconditions
- The application is running and reachable.
- The `/register` page is accessible.
- No account with the username `64234` is required for this test, since the input is expected to be blocked before submission.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with the value `64234` (5 characters).
3. Fill the `password` field with the value `Passw0rd!`.
4. Click the `Register` button.

## Expected Result
- The frontend blocks submission and does not send a request to `/api/register`.
- The message "Username must be at least 6 characters" is displayed.

## Actual Result
- The frontend did not block the submission; a request was sent to `/api/register`.
- The expected validation message was not confirmed as displayed.
- Test case TC-REG-005 status: Fail.

## Captured Request and Response Evidence
- Expected request: none (submission should be blocked by frontend validation).
- Observed: a request was sent to `/api/register`.
- The execution evidence does not include the request payload, response status, or response body.

## User Impact
Users can submit a username that violates the documented minimum length rule, and the required validation message is not enforced at the frontend. This allows invalid input to reach the backend and prevents the user from receiving the specified guidance.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-005.png`