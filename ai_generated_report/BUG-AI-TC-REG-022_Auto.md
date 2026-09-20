# Bug Report: TC-REG-022 — SQL Injection via `username` Field Allows Account Creation and Potential Table Drop

## Summary
During execution of test case **TC-REG-022**, a SQL injection payload was submitted in the `username` field of the registration form. The system returned **HTTP 201 (Created)** instead of the expected **HTTP 400 (Bad Request)**, indicating that the input was not properly sanitized/validated and was likely passed to the database layer in an unsafe manner.

## Test Case Details
| Field | Value |
| :--- | :--- |
| **Test Case ID** | TC-REG-022 |
| **Feature** | Registration |
| **Test Type** | Negative / Security (SQL Injection) |
| **Endpoint** | `POST /register` (Registration API) |

## Test Data
json
{
  "username": "'; DROP TABLE users;--",
  "password": "ValidPass1"
}


## Steps to Reproduce
1. Navigate to the Registration page of the application.
2. Enter the payload `'; DROP TABLE users;--` into the **username** field.
3. Enter a valid password (e.g., `ValidPass1`) into the **password** field.
4. Submit the registration form.
5. Observe the HTTP response status and the resulting state of the database.

## Expected Result
- **HTTP Status:** `400 Bad Request`
- The username `'; DROP TABLE users;--` violates the PRD rule requiring a **minimum length of 6 characters** *and* contains invalid characters (per PRD §3.1, usernames should be validated as strings with defined constraints).
- The application should reject the input with an appropriate validation error message (e.g., `"Username must be at least 6 characters"` or a generic invalid-character error).
- **No database mutation should occur.** The `users` table must remain intact.

## Actual Result
- **HTTP Status:** `201 Created`
- The registration request was accepted and a new account was created with the malicious username.
- The SQL payload was not sanitized, indicating a **SQL Injection vulnerability** in the registration flow.
- **Risk:** The injected payload `'; DROP TABLE users;--` may have executed against the SQLite database, potentially dropping the `users` table and causing a denial of service for all authentication functionality.

## Severity
**Critical**

## Priority
**P0 — Immediate**

## Environment
| Component | Version / Detail |
| :--- | :--- |
| Frontend | React + Ant Design |
| Backend | Flask |
| Database | SQLite |
| Test Case | TC-REG-022 |

## Impact
- **Security:** Direct SQL Injection vector allowing arbitrary SQL execution.
- **Data Integrity:** Potential loss of the entire `users` table, breaking registration and login for all users.
- **Availability:** If the table was dropped, the application becomes unusable for authentication flows.
- **Compliance:** Violates PRD §3.1 validation rules (username length and uniqueness checks are bypassed).

## Root Cause (Hypothesis)
The Flask backend likely constructs SQL queries using string concatenation or f-string interpolation instead of parameterized queries (e.g., `cursor.execute("INSERT INTO users VALUES ('" + username + "')")`). Additionally, server-side validation for username length and character set is missing or bypassed.

## Recommended Fix
1. **Use parameterized queries / prepared statements** for all database operations:
   python
   cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
   
2. **Enforce server-side validation** per PRD §3.1:
   - Minimum length of 6 characters.
   - Reject inputs containing SQL metacharacters (`'`, `;`, `--`, etc.) or use a strict allowlist regex (e.g., `^[a-zA-Z0-9_]{6,}$`).
3. **Return HTTP 400** with the appropriate error message when validation fails.
4. **Add automated regression tests** for SQL injection payloads across all input fields.
5. **Audit other endpoints** (e.g., login) for the same vulnerability class.

## Attachments / Evidence
- Request payload: `{'username': "'; DROP TABLE users;--", 'password': 'ValidPass1'}`
- Response status: `201 Created`
- Expected status: `400 Bad Request`

## Status
**Open — Awaiting Fix**