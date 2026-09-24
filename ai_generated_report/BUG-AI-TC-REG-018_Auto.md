# Bug Report: TC-REG-018 — Registration accepts non-unique username

## Summary
During execution of test case **TC-REG-018**, the registration endpoint returned **HTTP 201 (Created)** when it was expected to return **HTTP 400 (Bad Request)**. The payload used a `username` value that violates the uniqueness constraint defined in the PRD (Section 3.1), yet the account was successfully created.

## Test Case Details

| Field | Value |
| :--- | :--- |
| **Test Case ID** | TC-REG-018 |
| **Title** | Registration with duplicate username should be rejected |
| **Component** | Registration API / Frontend Registration Form |
| **Severity** | High |
| **Priority** | High |
| **Type** | Functional / Negative Test |

## Environment
- **Frontend**: React + Ant Design
- **Backend**: Flask
- **Database**: SQLite
- **Endpoint**: `POST /api/register` (assumed)

## Steps to Reproduce
1. Ensure a user with `username = "123456"` already exists in the database.
2. Send a registration request with the following payload:
   json
   {
     "username": "123456",
     "password": "ValidPass1"
   }
   
3. Observe the HTTP response status and body.

## Test Data (Payload Injected)
json
{
  "username": "123456",
  "password": "ValidPass1"
}


## Expected Result
- **HTTP Status**: `400 Bad Request`
- **Response Body**: Error message `"Username already exists"` (per PRD Section 3.1 — *"Must be unique"*).
- **Database**: No new record should be inserted.
- **UI**: Registration form should display the conflict error to the user.

## Actual Result
- **HTTP Status**: `201 Created`
- **Response Body**: *(Account creation success response — user record returned/created)*
- **Database**: A duplicate user record with `username = "123456"` was created.
- **UI**: No error displayed; user is treated as successfully registered.

## PRD Reference
> **3.1 Registration Rules**
> | Field | Type | Required | Validation Rules | Error Message |
> | :--- | :--- | :--- | :--- | :--- |
> | username | String | Yes | Min length: 6 chars <br> **Must be unique** | Conflict: **"Username already exists"** <br> Length: "Username must be at least 6 characters" |

The system failed to enforce the **uniqueness** constraint on the `username` field.

## Impact
- **Data Integrity**: Multiple accounts can share the same username, breaking the uniqueness guarantee required by the PRD.
- **Authentication Risk**: Login flow (Section 3.2) relies on matching credentials against database records; duplicate usernames can cause ambiguous or incorrect credential resolution.
- **Security**: Potential for account impersonation or confusion during login.

## Suspected Root Cause
- Backend registration handler in Flask is not performing a pre-insert uniqueness check (`SELECT ... WHERE username = ?`) before committing the new record.
- The SQLite schema may be missing a `UNIQUE` constraint on the `username` column, so the database does not reject the duplicate insert.
- Frontend validation (Ant Design) does not appear to block submission of an already-registered username.

## Suggested Fix
1. Add a `UNIQUE` constraint to the `username` column in the SQLite schema.
2. In the Flask registration route, check for an existing user before insertion and return:
   json
   { "error": "Username already exists" }
   
   with HTTP status `400`.
3. Handle the database `IntegrityError` (if the unique constraint is added) and map it to the same `400` response.
4. Optionally, add client-side validation in the React/Ant Design form to surface the conflict early.

## Attachments
- Request payload: `{"username": "123456", "password": "ValidPass1"}`
- Expected status: `400`
- Actual status: `201`