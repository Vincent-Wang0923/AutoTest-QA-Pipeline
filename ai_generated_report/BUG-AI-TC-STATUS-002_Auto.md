# Bug Report: Registration Returns HTTP 201 Instead of Expected HTTP 200

## Requirement
Per the test case TC-STATUS-002, the first registration submission is expected to return HTTP 200 with the message "Registration successful". The second submission with the same username is expected to return HTTP 409 with the message "Username already exists".

## Preconditions
- The application is running with the React frontend and Flask/SQLite backend.
- The username `s409_1790258466` does not already exist in the database.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the username field with `s409_1790258466`.
3. Fill the password field with `Passw0rd!`.
4. Submit the form via the "Register" button, which calls `/api/register`.
5. Navigate to `/register` again.
6. Fill the username field with `s409_1790258466`.
7. Fill the password field with `Passw0rd!`.
8. Submit the form via the "Register" button, which calls `/api/register`.

## Expected Result
- Step 4: The request to `/api/register` returns HTTP 200 with the message "Registration successful".
- Step 8: The request to `/api/register` returns HTTP 409 with the message "Username already exists".

## Actual Result
- Step 4: The request to `/api/register` returned HTTP 201 instead of the expected HTTP 200. The test failed with the error: "Expected HTTP 200, received HTTP 201."
- The execution did not proceed to the duplicate registration step, so the HTTP 409 behavior was not verified.

## Captured Request and Response Evidence
- Endpoint: `/api/register`
- Method: POST (form submission)
- Request payload (first submission): `username=s409_1790258466`, `password=Passw0rd!`
- Expected status: 200
- Actual status: 201

## User Impact
The frontend expects HTTP 200 for a successful registration. Receiving HTTP 201 may cause the frontend to treat the response as unexpected, potentially preventing the success message "Registration successful" from being displayed and blocking the user from proceeding. The duplicate registration path (HTTP 409) could not be validated because the test stopped at the first assertion failure.

## Evidence File
`C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STATUS-002.png`