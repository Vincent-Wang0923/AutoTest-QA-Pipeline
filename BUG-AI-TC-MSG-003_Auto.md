# Login Failure Message Test Fails Due to Registration Returning HTTP 409

## Requirement
Per PRD section 3.2 (Login Rules), a login attempt with credentials that do not match database records must return HTTP 401 and display "Invalid credentials". The test case TC-MSG-003 also requires a precondition step: registering a new user via `/api/register` must return HTTP 201 with the message "Registration successful".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `user_1790259369` is intended to be newly registered as part of the test setup.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `user_1790259369`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the registration form (button "Register", endpoint `/api/register`).
5. Navigate to `/`.
6. Fill the `username` field with `user_1790259369`.
7. Fill the `password` field with `WrongPass1`.
8. Submit the login form (button "Login", endpoint `/api/login`).

## Expected Result
- Step 4: HTTP 201 with message "Registration successful", redirect to `/`.
- Step 8: HTTP 401 with message "Invalid credentials", path remains `/`.

## Actual Result
The test failed at the registration step. The observed error is:

```
Expected HTTP 201, received HTTP 409.
```

The execution stopped before the login step could be performed, so the "Invalid credentials" message was not verified.

## Captured Request and Response Evidence
The evidence records the following actions completed before failure:

| Action | Field | Value |
| :--- | :--- | :--- |
| navigate | path | `/register` |
| fill | username | `user_1790259369` |
| fill | password | `Passw0rd!` |

- Expected path after navigate: `/register`; actual path: `/register`.
- Registration submit returned HTTP 409 instead of the expected HTTP 201.

The HTTP 409 response corresponds to the PRD registration rule for a non-unique username ("Username already exists"), indicating the username `user_1790259369` already exists in the database at the time of execution.

## User Impact
The login failure message requirement could not be validated because the test setup could not create a fresh account. This blocks verification of the "Invalid credentials" behavior for the login flow.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-MSG-003.png`