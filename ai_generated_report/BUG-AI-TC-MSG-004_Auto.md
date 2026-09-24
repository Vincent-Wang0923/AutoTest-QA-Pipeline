# Bug Report: Short Username Triggers Backend Request Instead of Frontend Validation

## Title
Registration form submits `/api/register` when username is shorter than 6 characters, instead of blocking submission with the required validation message.

## Requirement
Per PRD section 3.1 (Registration Rules), the `username` field must be at least 6 characters. When this rule is violated, the frontend must display the error message: "Username must be at least 6 characters".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The `/register` page is reachable.
- No account with the tested username exists (not required for this validation case, but noted for context).

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with the value `64234` (5 characters).
3. Fill the `password` field with the value `Passw0rd!`.
4. Click the `Register` button.

## Expected Result
- The frontend validation blocks the submission.
- No HTTP request is sent to `/api/register`.
- The message "Username must be at least 6 characters" is displayed to the user.

## Actual Result
- The frontend validation did not block the submission.
- A request was sent to `/api/register`.
- The expected validation message was not confirmed as displayed.

## Captured Request and Response Evidence
The execution evidence records the following actions and outcomes:
- `navigate` to `/register`: expected path `/register`, actual path `/register`.
- `fill` `username` = `64234`.
- `fill` `password` = `Passw0rd!`.
- The test case specified `expected_request: false` for the submit action, but the observed result states: "Expected frontend validation to block /api/register, but a request was sent."

No response payload or status code was captured in the provided evidence.

## User Impact
Users can submit a username that violates the documented minimum length rule. Because the frontend does not block the request or show the required message, users receive no immediate feedback on the invalid input and the invalid value reaches the backend.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-004.png`