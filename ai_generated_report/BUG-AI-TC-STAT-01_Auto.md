# Login Success Message Not Verified: Username Field Not Found on Login Page

## Requirement
Per PRD section 3.2 (Login Rules), a successful login must return HTTP 200, return the user_id, and show "Login successful".

## Preconditions
- Application is running and reachable at `http://localhost:5000`.
- Registration and login pages are available.
- Test user credentials: username `s200_1790257235`, password `Pass1234`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `s200_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the `Register` button (POST `/api/register`).
5. Navigate to `/login`.
6. Attempt to fill the `username` field with `s200_1790257235`.
7. Attempt to fill the `password` field with `Pass1234`.
8. Submit the `Login` button (POST `/api/login`).

## Expected Result
- The login form exposes a `Username` field that can be filled.
- Submitting valid credentials sends POST `/api/login` and receives HTTP 200.
- The page shows the message "Login successful" and navigates to `/`.

## Actual Result
- Step 6 failed. The locator `get_by_label("Username", exact=True)` timed out after 5000ms while waiting for the field on the login page.
- The test aborted with error: `Locator.fill: Timeout 5000ms exceeded.`
- The login submission (POST `/api/login`) was never executed, so the HTTP 200 response and "Login successful" message were not verified.

## Captured Request and Response Evidence
Registration step (completed successfully before the failure):
- Endpoint: POST `http://localhost:5000/api/register`
- Content-Type: `application/json`
- Request body: `{"username": "s200_1790257235", "password": "Pass1234"}`
- Status: `201`
- Response body: `{"message": "Registration successful", "status": "success"}`
- Visible messages: none
- Resulting path: `/`

Login step:
- No request captured. The `username` field could not be located on `/login`, so the form was not submitted.

Navigation evidence:
- `/register` navigated to `/register` (as expected).
- `/login` navigated to `/login` (as expected).

## User Impact
A user who has registered successfully cannot complete login through the UI because the `Username` input on the login page is not reachable by its label. The success path defined in PRD section 3.2 (HTTP 200, "Login successful") cannot be exercised or confirmed.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-01.png`