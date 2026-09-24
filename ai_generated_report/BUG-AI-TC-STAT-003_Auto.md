# Duplicate Registration Fails on First Submission with HTTP 409

## Requirement
Registration rules (PRD 3.1): username must be unique. A first-time registration with a valid, unused username is expected to succeed (HTTP 201, "Registration successful", redirect to `/`). A duplicate registration with an existing username is expected to fail with HTTP 409 and the message "Username already exists".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `user_1790259369` is not yet registered in the database.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill `username` with `user_1790259369`.
3. Fill `password` with `Passw0rd!`.
4. Submit the form via the "Register" button (endpoint `/api/register`).
5. Navigate to `/register` again.
6. Fill `username` with `user_1790259369`.
7. Fill `password` with `Passw0rd!`.
8. Submit the form via the "Register" button (endpoint `/api/register`).

## Expected Result
- Step 4 (first submission): HTTP 201, message "Registration successful", redirect to `/`.
- Step 8 (second submission): HTTP 409, message "Username already exists", remain on `/register`.

## Actual Result
The first submission (step 4) returned HTTP 409 instead of the expected HTTP 201. The test failed with the error: "Expected HTTP 201, received HTTP 409." The duplicate-registration step was not reached because the initial registration did not succeed.

## Captured Request and Response Evidence
- Action: submit, button "Register", endpoint `/api/register`
- Expected status: 201
- Actual status: 409
- Expected message: "Registration successful"
- Actual message: not captured (execution stopped at the status mismatch)

## User Impact
A user attempting to register with a valid, previously unused username receives a conflict response on the first attempt, preventing account creation and blocking the intended registration flow.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STAT-003.png`