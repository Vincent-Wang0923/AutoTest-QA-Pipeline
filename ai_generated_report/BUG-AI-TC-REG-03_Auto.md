# Bug Report: Registration with 5-Character Username Sends Request to /api/register Instead of Being Blocked by Frontend Validation

## Requirement
Registration username must be at least 6 characters. When the username is shorter than 6 characters, the frontend must block submission and display the message "Username must be at least 6 characters" (PRD Section 3.1).

## Preconditions
- The application is running with the React frontend and Flask backend.
- The user is on the /register page.
- No account with the username "66519" is required for this test, since the input is expected to be rejected before submission.

## Reproduction Steps
1. Navigate to /register.
2. Fill the username field with "66519" (5 characters).
3. Fill the password field with "Passw0rd!".
4. Click the "Register" button.

## Expected Result
- The frontend blocks the submission; no request is sent to /api/register.
- The message "Username must be at least 6 characters" is displayed.

## Actual Result
- A request was sent to /api/register despite the username being below the minimum length.
- The expected frontend validation message was not confirmed as the blocking behavior.

## Captured Request and Response Evidence
- The execution evidence records that a request was sent to /api/register when none was expected.
- No response details were captured in the provided evidence.

## User Impact
Users can submit a username that violates the minimum length rule, so the frontend does not enforce the documented validation and the expected error message is not shown at the point of submission.

## Evidence File
C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-03.png