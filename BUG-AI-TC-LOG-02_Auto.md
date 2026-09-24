# Login with Wrong Password Fails Before Credential Submission

## Requirement
Per PRD section 3.2 (Login Rules), submitting a login with credentials that do not match database records must return HTTP 401 and display "Invalid credentials".

## Preconditions
- A registered account exists with username `wp_1790257235` and password `Pass1234`.
- The application is reachable at `http://localhost:5000`.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `wp_1790257235`.
3. Fill `password` with `Pass1234`.
4. Submit the Register button (endpoint `/api/register`).
5. Navigate to `/login`.
6. Fill `username` with `wp_1790257235`.
7. Fill `password` with `WrongPass`.
8. Submit the Login button (endpoint `/api/login`).

## Expected Result
- A POST request is sent to `/api/login`.
- The server responds with HTTP 401.
- The message "Invalid credentials" is displayed.
- The user remains on `/login`.

## Actual Result
The test failed during step 6. The automation could not locate the Username input field on the login page:

```
Locator.fill: Timeout 5000ms exceeded.
Call log:
  - waiting for get_by_label("Username", exact=True)
```

Because the username field could not be filled, the password field was not filled, the Login button was not submitted, and no request was sent to `/api/login`. The expected 401 response and "Invalid credentials" message were never produced or verified.

## Captured Request and Response Evidence
Only the registration request from step 4 was captured. No login request or response exists in the evidence.

- Endpoint: `/api/register`
- Method: POST
- Content-Type: `application/json`
- Request body: `{"username": "wp_1790257235", "password": "Pass1234"}`
- Status: 201
- Response body: `{"message": "Registration successful", "status": "success"}`
- Visible messages: none
- Resulting path: `/`

Navigation to `/login` succeeded (actual path `/login`), but no further actions were recorded.

## User Impact
A user attempting to log in with an incorrect password cannot complete the login attempt in this flow. The login form's Username field is not reachable by the expected label, so the credential check defined in the PRD cannot be exercised or confirmed. Whether the failure is limited to the test locator or reflects a real UI defect is not determinable from the captured evidence.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-02.png`