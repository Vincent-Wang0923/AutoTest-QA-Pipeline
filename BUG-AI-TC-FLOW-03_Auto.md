# Bug Report: Login Form Username Field Not Found After Failed Login Attempt

## Requirement
Per PRD section 3.2 (Login Rules), the login form must accept username and password credentials, return HTTP 401 with "Invalid credentials" on failure, and HTTP 200 with "Login successful" on success. The test case TC-FLOW-03 requires the login form to remain usable after a failed login attempt so the user can retry with correct credentials.

## Preconditions
- Application is running at `http://localhost:5000`.
- A user account `flow3_1790257235` with password `Pass1234` has been registered successfully (confirmed by the registration step in the evidence).

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `flow3_1790257235` and `password` with `Pass1234`.
3. Submit the Register button. Registration succeeds (HTTP 201, path `/`).
4. Navigate to `/login`.
5. Attempt to fill the `username` field using the label locator `get_by_label("Username", exact=True)`.

## Expected Result
- The login form exposes a `Username` field that can be located and filled.
- The test proceeds to submit invalid credentials (expecting HTTP 401 with "Invalid credentials"), then submits valid credentials (expecting HTTP 200 with "Login successful" and redirect to `/`).

## Actual Result
- The test fails at step 5. The locator `get_by_label("Username", exact=True)` times out after 5000ms while waiting for the element.
- The failure occurs immediately after navigating to `/login`, before any login submission is attempted.
- The failed-login and successful-login steps defined in TC-FLOW-03 were never executed.

Error message:
```
Locator.fill: Timeout 5000ms exceeded.
Call log:
  - waiting for get_by_label("Username", exact=True)
```

## Captured Request and Response Evidence
The only network activity captured was the registration request. No login request was captured because the test aborted before submission.

Registration request:
- Endpoint: `POST http://localhost:5000/api/register`
- Content-Type: `application/json`
- Body: `{"username": "flow3_1790257235", "password": "Pass1234"}`
- Status: `201`
- Response body: `{"message": "Registration successful", "status": "success"}`

Navigation evidence:
- `/register` reached as expected.
- `/login` reached as expected.
- No further actions executed.

## User Impact
A user who navigates to the login page cannot locate the username input by its accessible label. This blocks the login flow entirely, including the retry-after-failure scenario described in TC-FLOW-03. Users are unable to authenticate through the labeled form field.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-FLOW-03.png`