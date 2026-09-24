# Bug Report: Login Form Username Field Not Accessible by Label

## Requirement
Per PRD section 3.2 (Login Rules), the login flow must accept credentials and, on failure, return HTTP 401 and display "Invalid credentials". The test case TC-STAT-02 verifies that the frontend handles an HTTP 401 response on login by showing the failure message.

## Preconditions
- The application is running and reachable.
- The `/login` page is available.
- A login attempt is made with credentials that do not match any database record.

## Reproduction Steps
1. Navigate to `/login`.
2. Fill the `username` field with `bad_1790257235`.
3. Fill the `password` field with `WrongPass`.
4. Submit the form via the `Login` button, which posts to `/api/login`.

## Expected Result
- The request to `/api/login` is sent.
- The backend responds with HTTP 401.
- The frontend displays the message "Invalid credentials".
- The user remains on `/login`.

## Actual Result
The test failed before the login request could be submitted. The automation could not locate the username input field:

```
Locator.fill: Timeout 5000ms exceeded.
Call log:
  - waiting for get_by_label("Username", exact=True)
```

The only recorded action was navigation to `/login`, which succeeded (actual path `/login`). No request to `/api/login` was captured, and no response or message was observed.

## Captured Request and Response Evidence
No HTTP request or response evidence was captured. Execution stopped at the field interaction step, before form submission.

## User Impact
The login form's username input is not resolvable by its accessible label. Users relying on assistive technologies or label-based navigation may be unable to identify or interact with the username field. Automated verification of the login failure path (HTTP 401 handling) cannot proceed.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-02.png`