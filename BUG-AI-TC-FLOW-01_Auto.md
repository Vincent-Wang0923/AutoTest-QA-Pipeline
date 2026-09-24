# Bug Report: Login form Username field not found after successful registration

## Requirement
Login Rules (PRD 3.2): Credentials must match database records. On success, the system returns HTTP 200, returns `user_id`, and shows "Login successful".

## Preconditions
- Application is running at `http://localhost:5000`.
- Username `e2e_1790257235` is not yet registered.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `e2e_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the `Register` button.
5. Navigate to `/login`.
6. Attempt to fill the `Username` field (locator: `get_by_label("Username", exact=True)`).

## Expected Result
- Registration returns HTTP 201 and redirects to `/`.
- Navigating to `/login` renders a login form containing a `Username` field.
- The `Username` field is fillable, allowing the login step to proceed.

## Actual Result
- Registration succeeded: HTTP 201, response body `{"message": "Registration successful", "status": "success"}`, redirect to `/`.
- Navigation to `/login` succeeded (`actual_path: /login`).
- The `Username` field could not be located. The fill action failed with:
  `Locator.fill: Timeout 5000ms exceeded. waiting for get_by_label("Username", exact=True)`
- The login step could not be executed, so the end-to-end flow did not complete.

## Captured Request and Response Evidence
Registration request:
- URL: `http://localhost:5000/api/register`
- Method: POST
- Content-Type: `application/json`
- Body: `{"username": "e2e_1790257235", "password": "Pass1234"}`

Registration response:
- Status: 201
- Body: `{"message": "Registration successful", "status": "success"}`

Login request: not captured (blocked by the locator timeout before submission).

## User Impact
After a successful registration, users cannot complete login because the `Username` input on the `/login` page is not reachable by its label. The end-to-end register-then-login flow is blocked.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-FLOW-01.png`