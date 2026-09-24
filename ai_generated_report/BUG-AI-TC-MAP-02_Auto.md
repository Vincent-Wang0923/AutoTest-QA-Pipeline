# Login Form Username Field Not Found After Registration

## Requirement
Login rules (PRD 3.2): credentials must match database records; success returns HTTP 200, returns user_id, and shows "Login successful". The login form must accept a username and password so the frontend field names map correctly to the backend payload.

## Preconditions
- Application is running at http://localhost:5000.
- A user account is created via the registration flow before attempting login.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `map2_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the Register button (endpoint `/api/register`).
5. Navigate to `/login`.
6. Attempt to fill the `username` field with `map2_1790257235`.

## Expected Result
- The login page exposes a username input that can be located and filled.
- Submitting valid credentials sends a POST to `/api/login` with body `{"username": "map2_1790257235", "password": "Pass1234"}`, returns HTTP 200, displays "Login successful", and navigates to `/`.

## Actual Result
- Step 6 fails. The username field cannot be located on the login page.
- Error: `Locator.fill: Timeout 5000ms exceeded.` while waiting for `get_by_label("Username", exact=True)`.
- The test aborts before the login submit action, so no `/api/login` request is sent and no login response is observed.

## Captured Request and Response Evidence
Registration step (completed successfully):
- Endpoint: `/api/register`
- Method: POST
- Content-Type: `application/json`
- Request body: `{"username": "map2_1790257235", "password": "Pass1234"}`
- Status: 201
- Response body: `{"message": "Registration successful", "status": "success"}`
- Visible messages: none
- Resulting path: `/`

Login step:
- Not executed. The username field could not be located, so no request to `/api/login` was captured.

Navigation evidence:
- `/register` reached as expected.
- `/login` reached as expected.

## User Impact
A user who has just registered cannot enter a username on the login page, blocking the login flow and preventing verification of the "Login successful" outcome defined in PRD 3.2.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MAP-02.png`