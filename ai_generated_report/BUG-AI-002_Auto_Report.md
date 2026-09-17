# Bug Report

## Bug ID
BUG-002

## Title
Registration with existing username returns HTTP 409 instead of expected HTTP 400

## Severity
Medium

## Priority
High

## Environment
- **Frontend**: React, Ant Design
- **Backend**: Flask, SQLite
- **Test Case**: 002
- **Endpoint**: Registration API

## Description
During execution of test case 002, a registration request was submitted with a username that already exists in the system. According to the expected behavior defined for the test case, the server should respond with HTTP status **400**. However, the server returned HTTP status **409 (Conflict)**.

While the PRD specifies that a duplicate username should trigger the error message *"Username already exists"*, the test case explicitly expects a **400** status code. This mismatch between the expected and actual status code indicates either a deviation from the test case specification or an inconsistency between the PRD and the test case definition.

## Preconditions
- The application (React frontend + Flask backend + SQLite DB) is running.
- A user with the username `admin` already exists in the database.

## Steps to Reproduce
1. Navigate to the registration page.
2. Enter the following credentials:
   - **Username**: `admin`
   - **Password**: `pwd123`
3. Submit the registration form.
4. Observe the HTTP response status code.

## Test Data (Payload)
json
{
  "username": "admin",
  "password": "pwd123"
}


## Expected Result
- **HTTP Status**: `400`
- The registration should be rejected due to the duplicate username.

## Actual Result
- **HTTP Status**: `409`
- The registration is rejected, but with a `409 Conflict` status code instead of the expected `400`.

## Impact
- Automated test case 002 fails due to the status code mismatch.
- API consumers relying on the documented `400` response for validation errors may not handle `409` correctly.
- Potential inconsistency between the PRD (which implies a conflict scenario) and the test case specification (which expects `400`).

## Suggested Fix
- Confirm the intended status code with the product/QA team:
  - If **400** is correct, update the backend to return `400` for duplicate username validation errors.
  - If **409** is correct, update test case 002 and the PRD to reflect `409 Conflict` as the expected status code for duplicate usernames.

## Attachments
- Request payload: `{'username': 'admin', 'password': 'pwd123'}`
- Expected status: `400`
- Actual status: `409`