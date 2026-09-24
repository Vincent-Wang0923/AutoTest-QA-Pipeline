# Bug Report: Login Form Username Field Not Accessible by Label

## Title
Login page username input cannot be located by its label, blocking the "non-existent username" login test.

## Requirement
Per PRD section 3.2 (Login Rules), submitting credentials that do not match database records must return HTTP 401 and display "Invalid credentials". The login form must expose a username input so this flow can be exercised.

## Preconditions
- Application is running with the React frontend and Flask backend.
- User is not authenticated.
- No account exists with username `missing_1790257235`.

## Reproduction Steps
1. Navigate to `/login`.
2. Attempt to fill the username field using the accessible label "Username" (exact match).
3. Attempt to fill the password field with `Pass1234`.
4. Submit the login form via the "Login" button.

## Expected Result
- The username field is locatable by the label "Username".
- The form submits to `/api/login`.
- The backend responds with HTTP 401.
- The message "Invalid credentials" is displayed.
- The user remains on `/login`.

## Actual Result
- The username field could not be located by `get_by_label("Username", exact=True)`.
- The action failed with: `Locator.fill: Timeout 5000ms exceeded.`
- The test aborted before any credentials were entered or submitted.
- No request to `/api/login` was made, and no response was received.

## Captured Request and Response Evidence
- No HTTP request was captured. The failure occurred during element location, before form submission.
- Expected request (not sent): `POST /api/login` with username `missing_1790257235` and password `Pass1234`.
- Expected response (not received): HTTP 401 with message "Invalid credentials".

## User Impact
Users and automated clients relying on the accessible label "Username" cannot target the username input. The login flow for non-existent usernames cannot be completed or verified through this locator, preventing validation of the PRD-specified 401 behavior.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-LOG-03.png`