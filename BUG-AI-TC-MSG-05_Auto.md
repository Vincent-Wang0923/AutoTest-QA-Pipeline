# Login Success Message Not Verified Due to Missing Username Field Locator

## Requirement
Per PRD section 3.2 (Login Rules), a successful login must return HTTP 200, return the user_id, and show the message "Login successful".

## Preconditions
- The application is running and reachable at http://localhost:5000.
- The registration and login pages are available.
- No existing account with username `msg4_1790257235`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `msg4_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the Register button (endpoint `/api/register`).
5. Navigate to `/login`.
6. Attempt to fill the `username` field with `msg4_1790257235`.
7. Fill `password` with `Pass1234`.
8. Submit the Login button (endpoint `/api/login`).

## Expected Result
- Step 4: Registration succeeds with HTTP 201.
- Step 6: The `username` field on the login page is located and filled.
- Step 8: Login returns HTTP 200, and the message "Login successful" is displayed.

## Actual Result
- Step 4: Registration succeeded. The request was sent to `http://localhost:5000/api/register` as POST with content type `application/json` and body `{"username": "msg4_1790257235", "password": "Pass1234"}`. The response status was 201 with body `{"message": "Registration successful", "status": "success"}`. No visible messages were shown, and the path changed to `/`.
- Step 5: Navigation to `/login` succeeded (actual path `/login`).
- Step 6: The `username` field could not be located. The action failed with: `Locator.fill: Timeout 5000ms exceeded. Call log: - waiting for get_by_label("Username", exact=True)`.
- Steps 7 and 8 were not executed because the test aborted at step 6. The login request to `/api/login` was never sent, and the "Login successful" message was not verified.

## Captured Request and Response Evidence
Registration request:
- URL: `http://localhost:5000/api/register`
- Method: POST
- Content-Type: `application/json`
- Body: `{"username": "msg4_1790257235", "password": "Pass1234"}`
- Status: 201
- Response body: `{"message": "Registration successful", "status": "success"}`

Login request:
- Not captured. The test failed before the login submission step.

## User Impact
The login success message required by the PRD could not be validated because the login page's username input was not reachable by the expected label. Users attempting to log in through the same locator path would be unable to complete the login flow, and the required "Login successful" confirmation cannot be confirmed.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-05.png`