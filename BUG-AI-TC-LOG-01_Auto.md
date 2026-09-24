# Login Form Username Field Not Found After Successful Registration

## Requirement
Per PRD section 3.2 (Login Rules), a user with valid credentials must be able to log in: the system returns HTTP 200, displays "Login successful", and navigates to `/`. The login form must expose a `Username` field so credentials can be entered.

## Preconditions
- Application is running at `http://localhost:5000`.
- No existing account with username `ok_1790257235`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `ok_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the `Register` button.
5. Navigate to `/login`.
6. Attempt to fill the `Username` field with `ok_1790257235`.

## Expected Result
- Step 4: Registration succeeds (HTTP 201), user is redirected to `/`.
- Step 5: Login page loads at `/login`.
- Step 6: The `Username` field is located and filled, allowing the login flow to continue and ultimately return HTTP 200 with the message "Login successful".

## Actual Result
- Step 4: Registration succeeded. The request was sent to `http://localhost:5000/api/register` as `POST` with `Content-Type: application/json` and body `{"username": "ok_1790257235", "password": "Pass1234"}`. The response status was `201` with body `{"message": "Registration successful", "status": "success"}`. The app navigated to `/`.
- Step 5: Navigation to `/login` succeeded (`actual_path` = `/login`).
- Step 6: The test failed with `Locator.fill: Timeout 5000ms exceeded.` while waiting for `get_by_label("Username", exact=True)`. The `Username` input could not be located on the login page, so the login submission step was never reached.

## Captured Request and Response Evidence
Registration request:
- URL: `http://localhost:5000/api/register`
- Method: `POST`
- Content-Type: `application/json`
- Body: `{"username": "ok_1790257235", "password": "Pass1234"}`
- Status: `201`
- Response body: `{"message": "Registration successful", "status": "success"}`

Login request: not captured. The test failed before the login form could be filled and submitted.

## User Impact
A user who has just registered successfully cannot complete login because the `Username` field is not present or not discoverable on the `/login` page. The end-to-end registration-to-login flow is blocked at the login step.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-01.png`