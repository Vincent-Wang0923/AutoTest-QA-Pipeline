# Bug Report: Registration Fails with HTTP 409 During Login Success Test

## Title
Registration step returns HTTP 409 instead of HTTP 201, blocking verification of the "Login successful" message.

## Requirement
Per PRD Section 3.2 (Login Rules), a successful login must return HTTP 200, return the user_id, and show "Login successful". The test case TC-MSG-002 verifies this message by first registering a new user (expected HTTP 201 with "Registration successful") and then logging in with those credentials.

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The registration and login endpoints are reachable.
- The test uses username `user_1790259369` and password `Passw0rd!`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the username field with `user_1790259369`.
3. Fill the password field with `Passw0rd!`.
4. Submit the Register button, which posts to `/api/register`.
5. Observe the response status and message.
6. Navigate to `/`.
7. Fill the username field with `user_1790259369`.
8. Fill the password field with `Passw0rd!`.
9. Submit the Login button, which posts to `/api/login`.

## Expected Result
- Step 4: `/api/register` returns HTTP 201 with the message "Registration successful", and the app navigates to `/`.
- Step 9: `/api/login` returns HTTP 200 with the message "Login successful".

## Actual Result
- Step 4: `/api/register` returned HTTP 409 instead of the expected HTTP 201. The test failed at this point with the error: "Expected HTTP 201, received HTTP 409."
- Steps 6 through 9 were not executed because the test aborted after the registration failure. The login success message was therefore not verified.

## Captured Request and Response Evidence
- Action: submit Register button.
- Endpoint: `/api/register`.
- Request body: username `user_1790259369`, password `Passw0rd!`.
- Expected status: 201.
- Actual status: 409.
- Expected message: "Registration successful".
- Actual message: not captured in the evidence.

## User Impact
A new user attempting to register with the username `user_1790259369` receives an HTTP 409 response instead of a successful registration. Because registration does not complete, the user cannot proceed to log in and cannot see the "Login successful" message. The login success flow remains unverified for this test case.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-002.png`