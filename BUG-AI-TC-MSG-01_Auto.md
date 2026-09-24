# Bug Report: Registration Length Validation Does Not Block Submission

## Title
Registration form submits a request to `/api/register` when the username is shorter than 6 characters, instead of blocking submission with the required error message.

## Requirement
Per PRD section 3.1 (Registration Rules), the `username` field must be at least 6 characters. When this rule is violated, the expected error message is: "Username must be at least 6 characters".

## Preconditions
- The application is running with the React frontend and Flask backend.
- The `/register` page is reachable.
- No account with the tested username exists.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `66519` (5 characters).
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button.

## Expected Result
- Frontend validation blocks the submission.
- No request is sent to `/api/register`.
- The error message "Username must be at least 6 characters" is displayed.

## Actual Result
- The frontend did not block the submission.
- A request was sent to `/api/register`.
- The expected validation error message was not confirmed as displayed.

## Captured Request and Response Evidence
The execution evidence records the following actions and outcomes:
- `navigate` to `/register`: expected path `/register`, actual path `/register`.
- `fill` `username` = `66519`.
- `fill` `password` = `Passw0rd!`.
- The test failed with the error: "Expected frontend validation to block /api/register, but a request was sent."

No request payload or response body was captured in the provided evidence.

## User Impact
Users can submit a username that violates the documented minimum length rule. The registration flow does not enforce the specified client-side validation, so the required error message is not shown and an invalid submission reaches the backend.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-01.png`