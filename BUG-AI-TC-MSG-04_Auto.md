# Bug Report: TC-MSG-04 Login Form Username Field Not Found

## Title
Login page username input cannot be located by label "Username", blocking verification of the invalid credentials message.

## Requirement
Per PRD section 3.2 (Login Rules), submitting credentials that do not match database records must return HTTP 401 and display "Invalid credentials". The test case TC-MSG-04 verifies that this message text matches the PRD.

## Preconditions
- Application is running with the React frontend and Flask backend.
- The login page is reachable at path `/login`.
- A test account context exists for the invalid-credentials scenario (username `msg3_1790257235` used with an incorrect password).

## Reproduction Steps
1. Navigate to `/login`.
2. Locate the username input field by label "Username" (exact match).
3. Fill the username field with `msg3_1790257235`.
4. Fill the password field with `WrongPass`.
5. Submit the form via the "Login" button, which posts to `/api/login`.

## Expected Result
- The request to `/api/login` is sent.
- The backend responds with HTTP 401.
- The page remains on `/login`.
- The message "Invalid credentials" is displayed.

## Actual Result
- Navigation to `/login` succeeded (actual path `/login`).
- The test failed before any input could be entered: the locator `get_by_label("Username", exact=True)` timed out after 5000ms.
- No request to `/api/login` was issued, and no response or message was observed.

## Captured Request and Response Evidence
- No HTTP request or response was captured. Execution stopped at the username field lookup, before form submission.
- The only recorded action is the successful navigation to `/login`.

## User Impact
The automated flow cannot reach the login submission step, so the invalid-credentials message behavior defined in the PRD is unverified. If the same locator issue reflects the actual UI, users relying on labeled input fields (including assistive technology) may be unable to identify the username field.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-04.png`