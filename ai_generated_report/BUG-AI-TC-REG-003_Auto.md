# Bug Report: Username shorter than 6 characters is accepted during registration

## Requirement
Registration rule 3.1 states that the username must have a minimum length of 6 characters. A username shorter than 6 characters must be rejected with the error message "Username must be at least 6 characters".

## Preconditions
- The registration page is reachable at `/register`.
- The registration endpoint `/api/register` is available.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with a 5-character value: `reg5_1790261464`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` is rejected with HTTP status 400.
- The response contains the message "Username must be at least 6 characters".
- The user remains on `/register`.

## Actual Result
- The request to `/api/register` returned HTTP status 201.
- The username of 5 characters was accepted instead of being rejected.
- The expected validation error message was not returned.

## Captured Request and Response Evidence
- Action: submit `Register` button to endpoint `/api/register`.
- Expected status: 400.
- Actual status: 201.
- Expected message: "Username must be at least 6 characters".
- Observed error: "Expected HTTP 400, received HTTP 201."

## User Impact
Users can register with a username that violates the minimum length rule, allowing accounts to be created with invalid usernames and bypassing the specified validation constraint.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-REG-003.png`