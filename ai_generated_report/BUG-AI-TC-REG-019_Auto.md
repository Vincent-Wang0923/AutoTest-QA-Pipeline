# Bug Report: TC-REG-019 — Registration accepts payload that should return HTTP 400

## Summary
During execution of test case **TC-REG-019**, the registration endpoint returned **HTTP 201 (Created)** instead of the expected **HTTP 400 (Bad Request)** when submitting the payload `{'username': 'validuser06', 'password': '123456'}`.

## Test Case Details
| Field | Value |
| :--- | :--- |
| Test Case ID | TC-REG-019 |
| Module | Registration |
| Payload Injected | `{'username': 'validuser06', 'password': '123456'}` |
| Expected Status | `400` |
| Actual Status | `201` |

## Steps to Reproduce
1. Launch the React frontend and Flask backend of the target system.
2. Navigate to the **Registration** page.
3. Submit the following payload to the registration endpoint:
   json
   {
     "username": "validuser06",
     "password": "123456"
   }
   
4. Observe the HTTP response status code returned by the backend.

## Expected Behavior
Per **PRD Section 3.1 (Registration Rules)**, the registration endpoint should validate the incoming payload against the defined rules and reject invalid input with **HTTP 400**.

For the payload `{'username': 'validuser06', 'password': '123456'}`:
- `username` = `validuser06` → length is 11 characters (≥ 6) and must be unique.
- `password` = `123456` → non-empty.

If the payload violates any rule (e.g., duplicate username, invalid length, or empty password), the API must respond with **HTTP 400** and the corresponding error message defined in the PRD:
- `"Username already exists"`
- `"Username must be at least 6 characters"`
- `"Password required"`

## Actual Behavior
The backend returned **HTTP 201 (Created)**, indicating the account was successfully created despite the payload being expected to fail validation. This suggests one or more of the following:

- The uniqueness check for `username` is not enforced (e.g., `validuser06` already exists in the SQLite database).
- The length validation for `username` is not applied.
- The empty-password validation is bypassed.
- The endpoint is not returning the correct HTTP status code on validation failure.

## Impact
- **Severity:** High
- **Priority:** High
- **Affected Area:** Registration flow / backend validation
- **Risk:** Duplicate or invalid accounts may be created, violating PRD rules and compromising data integrity. Downstream login behavior (PRD Section 3.2) may also be affected if duplicate usernames exist.

## Environment
- **Frontend:** React + Ant Design
- **Backend:** Flask + SQLite
- **Test Type:** API / Integration
- **Test Case:** TC-REG-019

## Attachments / Evidence
- Request payload: `{'username': 'validuser06', 'password': '123456'}`
- Expected response: `HTTP 400`
- Actual response: `HTTP 201`

## Suggested Fix
1. Verify that the registration endpoint enforces **username uniqueness** against the SQLite `users` table before insertion.
2. Confirm that **minimum length (6 chars)** validation is applied to `username`.
3. Confirm that **non-empty password** validation is applied.
4. Ensure the API returns **HTTP 400** with the exact error messages defined in PRD Section 3.1 when validation fails.
5. Add/expand automated tests to cover duplicate username, short username, and empty password scenarios.