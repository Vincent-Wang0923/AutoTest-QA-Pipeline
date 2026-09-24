# QA Test Report: React + Flask Authentication POC

## Executive Summary

A total of 25 test cases were executed against the registration and login flows of the React + Flask target system. Results: 23 passed, 2 failed.

The two failures (TC-REG-03 and TC-MSG-01) share the same root behavior: the frontend does not block submission of a username shorter than 6 characters, and instead sends the request to `/api/register`. Both failures relate to the same missing client-side length validation. All other functional, boundary, exception, navigation, mapping, endpoint, status-code, and message-text checks passed.

No environment or automation failures were observed. Both failures are product failures.

## Execution Matrix

| ID | Type | Scenario | Status |
| :--- | :--- | :--- | :--- |
| TC-REG-01 | Functional | Successful registration with valid username and password | Pass |
| TC-REG-02 | Boundary | Registration with username of exactly 6 characters (minimum allowed) | Pass |
| TC-REG-03 | Boundary | Registration with username of 5 characters (below minimum) | Fail |
| TC-REG-04 | Exception | Registration with empty username | Pass |
| TC-REG-05 | Exception | Registration with empty password | Pass |
| TC-REG-06 | Exception | Duplicate registration with same username | Pass |
| TC-LOG-01 | Functional | Successful login after registration | Pass |
| TC-LOG-02 | Exception | Login with unregistered username | Pass |
| TC-LOG-03 | Exception | Login with correct username but wrong password | Pass |
| TC-LOG-04 | Exception | Login with empty password | Pass |
| TC-NAV-01 | Functional | Browser back navigation from login to registration preserves form state | Pass |
| TC-NAV-02 | Functional | Browser refresh on login page does not auto-submit credentials | Pass |
| TC-MAP-01 | Functional | Frontend field names map correctly to backend payload on registration | Pass |
| TC-MAP-02 | Functional | Frontend field names map correctly to backend payload on login | Pass |
| TC-EP-01 | Functional | Registration form targets /api/register endpoint | Pass |
| TC-EP-02 | Functional | Login form targets /api/login endpoint | Pass |
| TC-STAT-01 | Functional | Frontend handles HTTP 201 on registration as success | Pass |
| TC-STAT-02 | Functional | Frontend handles HTTP 409 on duplicate registration as conflict | Pass |
| TC-STAT-03 | Functional | Frontend handles HTTP 200 on login as success | Pass |
| TC-STAT-04 | Functional | Frontend handles HTTP 401 on login as failure | Pass |
| TC-MSG-01 | Functional | Registration length error message matches PRD text | Fail |
| TC-MSG-02 | Functional | Registration duplicate error message matches PRD text | Pass |
| TC-MSG-03 | Functional | Registration empty-password error message matches PRD text | Pass |
| TC-MSG-04 | Functional | Login failure message matches PRD text | Pass |
| TC-MSG-05 | Functional | Login success message matches PRD text | Pass |

## Bug Summary

Two failures were recorded. Both are product failures; neither is attributable to automation or environment issues.

**BUG-01: Username length validation is not enforced on the frontend (TC-REG-03)**
- Scenario: Registration with a 5-character username (`66519`), below the PRD minimum of 6 characters.
- Expected: Frontend validation blocks the request to `/api/register`.
- Actual: A request was sent to `/api/register`. The test recorded the failure message: "Expected frontend validation to block /api/register, but a request was sent."
- Evidence: `evidence\TC-REG-03.png`.
- PRD reference: Section 3.1, username validation rule "Min length: 6 chars" with error message "Username must be at least 6 characters".

**BUG-02: Registration length error message is not produced (TC-MSG-01)**
- Scenario: Registration with a 5-character username (`66519`), checking that the PRD length error message is shown.
- Expected: Frontend validation blocks the request and the PRD message "Username must be at least 6 characters" is displayed.
- Actual: A request was sent to `/api/register`, so the expected validation message was not produced. The test recorded the failure message: "Expected frontend validation to block /api/register, but a request was sent."
- Evidence: `evidence\TC-MSG-01.png`.
- PRD reference: Section 3.1, username length error message.

Both bugs describe the same underlying behavior from two angles: the missing client-side minimum-length check on the username field. TC-REG-03 verifies the blocking behavior; TC-MSG-01 verifies the associated message. They are reported separately because they are separate test cases with separate assertions.

## React-to-Flask Integration Coverage

Integration behavior between the React frontend and the Flask backend was verified and passed in the following areas:

- **Endpoint targeting**: The registration form posts to `/api/register` (TC-EP-01) and the login form posts to `/api/login` (TC-EP-02). Both used `POST` with `Content-Type: application/json`.
- **Payload mapping**: Frontend field names map correctly to backend payloads for registration (TC-MAP-01) and login (TC-MAP-02). Request bodies contained `username` and `password` as entered.
- **Status code handling**: The frontend treats HTTP 201 as registration success (TC-STAT-01), HTTP 409 as duplicate-registration conflict with the message "Username already exists" (TC-STAT-02), HTTP 200 as login success with `user_id` returned (TC-STAT-03), and HTTP 401 as login failure with "Invalid credentials" (TC-STAT-04).
- **Backend responses**: Registration returned 201 with `{"message": "Registration successful", "status": "success"}`; duplicate registration returned 409 with `{"message": "Username already exists", "status": "error"}`; login returned 200 with `user_id`; failed login returned 401 with `{"message": "Invalid credentials", "status": "error"}`.
- **Client-side gating**: Empty username (TC-REG-04) and empty password (TC-REG-05) on registration produced zero requests, and empty password on login (TC-LOG-04) produced zero requests, confirming the frontend blocks these submissions before reaching Flask.

The integration gap is limited to the username minimum-length rule, which is not enforced on the frontend before the request is sent.

## QA Conclusion

The system meets the PRD requirements for registration success, minimum-length boundary acceptance at exactly 6 characters, empty-field handling, duplicate-username conflict handling, login success and failure, navigation behavior, payload mapping, endpoint targeting, HTTP status handling, and message text for all tested messages except the username length message.

Two product defects remain open, both concerning the missing frontend enforcement of the username minimum length of 6 characters and its associated error message. These should be fixed and retested before the POC is considered complete against the PRD. All other 23 test cases passed, and no automation or environment failures were encountered.