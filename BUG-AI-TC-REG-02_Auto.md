# Bug Report: Login Form Username Field Not Found After Successful Registration

## Title
Login page does not expose a "Username" field labeled exactly "Username", blocking login after successful registration.

## Requirement
Per PRD section 3.2 (Login Rules), a user must be able to submit credentials that match database records and receive HTTP 200 with the message "Login successful". Test case TC-REG-02 verifies that a newly registered account can subsequently log in.

## Preconditions
- Application is running with the React frontend and Flask/SQLite backend.
- The username `login_1790257235` is not already registered.
- Browser session is active.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the username field with `login_1790257235`.
3. Fill the password field with `Pass1234`.
4. Submit the registration form.
5. Navigate to `/login`.
6. Attempt to fill the username field with `login_1790257235`.
7. Attempt to fill the password field with `Pass1234`.
8. Submit the login form.

## Expected Result
- Step 4: POST to `/api/register` returns HTTP 201, and the app navigates to `/`.
- Step 6: The login page provides a username input that can be located by the label "Username" and accepts the value.
- Step 8: POST to `/api/login` returns HTTP 200 with the message "Login successful", and the app navigates to `/`.

## Actual Result
- Step 4 succeeded: POST to `/api/register` returned HTTP 201 with body `{"message": "Registration successful", "status": "success"}`, and the app navigated to `/`.
- Step 5 succeeded: navigation to `/login` completed.
- Step 6 failed: the locator `get_by_label("Username", exact=True)` timed out after 5000 ms. The username field on the login page could not be located by that label, so the login flow could not proceed. Steps 7 and 8 were not executed.

## Captured Request and Response Evidence
Registration request (from evidence):
- Endpoint: `/api/register`
- Method: POST
- Content-Type: `application/json`
- Body: `{"username": "login_1790257235", "password": "Pass1234"}`
- Status: 201
- Response body: `{"message": "Registration successful", "status": "success"}`

Login request: not captured, because the failure occurred before the login form could be filled and submitted.

## User Impact
A user who successfully registers cannot complete the subsequent login step through the UI, because the username input on the login page is not discoverable by its expected label. This blocks the end-to-end registration-to-login flow defined in TC-REG-02.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-02.png`