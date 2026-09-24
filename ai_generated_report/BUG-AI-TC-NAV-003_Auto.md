# Bug Report: Registration Fails with HTTP 409 for a New Username During TC-NAV-003

## Requirement
Per PRD Section 3.1 (Registration Rules), a username must be unique and at least 6 characters. A registration request with a valid, non-duplicate username is expected to succeed. The test case TC-NAV-003 expects the registration endpoint `/api/register` to return HTTP 201 with the message "Registration successful" and to navigate to `/`.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration page is reachable at `/register`.
- The username `user_1790259369` is intended to be a new, unique account for this test run.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form via the "Register" button, which calls `/api/register`.
5. Observe the HTTP response status and message.

## Expected Result
- The registration request to `/api/register` returns HTTP 201.
- The response message is "Registration successful".
- The application navigates to `/`.

## Actual Result
- The registration request returned HTTP 409 instead of the expected HTTP 201.
- The test case status is Fail with the error: "Expected HTTP 201, received HTTP 409."
- The execution stopped at the registration step; subsequent login and back-navigation steps were not reached.

## Captured Request and Response Evidence
- Action: submit "Register" to endpoint `/api/register`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- No response body or message was captured in the provided evidence.

## User Impact
A user attempting to register with the username `user_1790259369` cannot complete registration. Because the flow halts at registration, the user cannot proceed to login or to the post-login back-navigation behavior that TC-NAV-003 was designed to verify.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-NAV-003.png`