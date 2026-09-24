# Duplicate Registration Flow Cannot Reach Login Step Due to Missing Username Field on Login Page

## Requirement
Per PRD section 3.2 (Login Rules), a user with valid credentials must be able to log in: credentials matching database records return HTTP 200, return `user_id`, and display "Login successful". Per section 3.1, a duplicate username registration must return HTTP 409 with the message "Username already exists".

## Preconditions
- Application is running and reachable at `http://localhost:5000`.
- The username `flow2_1790257235` is not yet registered at the start of the test.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `flow2_1790257235` and `password` with `Pass1234`.
3. Submit the Register button (POST `/api/register`).
4. Navigate to `/register` again.
5. Fill `username` with `flow2_1790257235` and `password` with `Pass1234`.
6. Submit the Register button (POST `/api/register`).
7. Navigate to `/login`.
8. Attempt to fill the `username` field with `flow2_1790257235`.

## Expected Result
- Step 3: HTTP 201, registration succeeds, path becomes `/`.
- Step 6: HTTP 409 with message "Username already exists", path remains `/register`.
- Step 7: Login page loads at `/login`.
- Step 8: The `username` field is present and can be filled, allowing the login flow to continue and ultimately return HTTP 200 with "Login successful".

## Actual Result
- Step 3: HTTP 201, response body `{"message": "Registration successful", "status": "success"}`, path becomes `/`. Matches expectation.
- Step 6: HTTP 409, response body `{"message": "Username already exists", "status": "error"}`, visible message "Username already exists", path remains `/register`. Matches expectation.
- Step 7: Navigation to `/login` succeeds; actual path is `/login`.
- Step 8: Filling the `username` field fails. The locator `get_by_label("Username", exact=True)` times out after 5000ms. The test aborts before the login submission, so the login step is never executed.

## Captured Request and Response Evidence
- First registration (step 3):
  - URL: `http://localhost:5000/api/register`
  - Method: POST
  - Content-Type: `application/json`
  - Body: `{"username": "flow2_1790257235", "password": "Pass1234"}`
  - Status: 201
  - Response body: `{"message": "Registration successful", "status": "success"}`
- Duplicate registration (step 6):
  - URL: `http://localhost:5000/api/register`
  - Method: POST
  - Content-Type: `application/json`
  - Body: `{"username": "flow2_1790257235", "password": "Pass1234"}`
  - Status: 409
  - Response body: `{"message": "Username already exists", "status": "error"}`
  - Visible messages: `["Username already exists"]`
- Login step (step 8): no request was issued. The failure occurred during the fill action, before submission.

## Error
```
Locator.fill: Timeout 5000ms exceeded.
Call log:
  - waiting for get_by_label("Username", exact=True)
```

## User Impact
After a duplicate-registration attempt, a user who navigates to the login page cannot enter a username because the expected `Username` field is not found by the label locator. The login flow cannot be completed, so the user cannot authenticate with the original password. This blocks the end-to-end flow described in the test case and prevents verification of the login success path.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-FLOW-02.png`