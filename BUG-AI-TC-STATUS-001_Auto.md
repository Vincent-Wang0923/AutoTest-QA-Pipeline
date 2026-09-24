# Registration Returns HTTP 201 Instead of HTTP 200

## Requirement
The registration flow is expected to return HTTP 200 on success. Per the generated test case TC-STATUS-001, the frontend submits to `/api/register` and expects a 200 response with the message "Registration successful".

## Preconditions
- The application is running with the React frontend and Flask backend.
- The `/register` page is reachable.
- The username `s200_1790258466` is not already registered.

## Reproduction Steps
1. Navigate to `/register`.
2. Fill the `username` field with `s200_1790258466`.
3. Fill the `password` field with `Passw0rd!`.
4. Submit the form via the `Register` button, which posts to `/api/register`.

## Expected Result
- The request to `/api/register` returns HTTP 200.
- The frontend displays "Registration successful".

## Actual Result
- The request to `/api/register` returns HTTP 201.
- The test case fails with the error: "Expected HTTP 200, received HTTP 201."

## Captured Request and Response Evidence
- Endpoint: `/api/register`
- Method: POST (form submission via Register button)
- Request payload: `username=s200_1790258466`, `password=Passw0rd!`
- Expected status: 200
- Actual status: 201
- Expected message: "Registration successful"

## User Impact
The frontend status handling for registration does not match the backend response. Because the test asserts HTTP 200, the registration success path is treated as a failure, which can prevent the success message from being shown and block the expected post-registration flow.

## Evidence File
- Screenshot: `C:\Users\17268\Desktop\实习\Week6\ai_generated_report\evidence\TC-STATUS-001.png`