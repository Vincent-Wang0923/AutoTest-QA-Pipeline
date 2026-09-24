# Login Page Username Field Not Found After Successful Registration

## Requirement
Login Rules (PRD 3.2): Credentials must match database records. On success, the system returns HTTP 200, returns user_id, and shows "Login successful".

## Preconditions
- Application is running at http://localhost:5000.
- No existing account with username `ep2_1790257235`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `ep2_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the Register button.
5. Navigate to `/login`.
6. Fill `username` with `ep2_1790257235`.
7. Fill `password` with `Pass1234`.
8. Submit the Login button.

## Expected Result
- Step 4: POST to `/api/register` returns HTTP 201.
- Step 5: `/login` page loads with a `Username` input field.
- Step 8: POST to `/api/login` returns HTTP 200, the message "Login successful" is displayed, and the user is routed to `/`.

## Actual Result
- Step 4: POST to `/api/register` returned HTTP 201 with body `{"message": "Registration successful", "status": "success"}`.
- Step 5: Navigation to `/login` succeeded (actual path `/login`).
- Step 6: Filling the `Username` field failed. The locator `get_by_label("Username", exact=True)` timed out after 5000ms because no matching element was found on the login page.
- Steps 7 and 8 were not reached. No login request was sent, and no success message or redirect was observed.

## Captured Request and Response Evidence
Registration submission:
- URL: `http://localhost:5000/api/register`
- Method: POST
- Content-Type: `application/json`
- Body: `{"username": "ep2_1790257235", "password": "Pass1234"}`
- Status: 201
- Response body: `{"message": "Registration successful", "status": "success"}`

Login submission:
- Not captured. The test aborted before the login form could be filled and submitted.

## User Impact
After a successful registration, a user cannot enter credentials on the login page because the Username input is not reachable via its label. The login flow cannot be completed, so the user cannot authenticate and reach the post-login page.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-EP-02.png`