# Bug Report: TC-REG-017 — Registration accepts payload with unexpected `Content-Type`, returns 201 instead of 415

## Summary
During execution of test case **TC-REG-017**, a registration request was submitted with the payload `{'username': 'validuser05', 'password': 'ValidPass1'}`. The API returned **HTTP 201 (Created)** instead of the expected **HTTP 415 (Unsupported Media Type)**.

## Test Case Details
| Field | Value |
| :--- | :--- |
| Test Case ID | TC-REG-017 |
| Related Requirement | PRD §3.1 Registration Rules |
| Endpoint | Registration endpoint (POST) |
| Payload | `{'username': 'validuser05', 'password': 'ValidPass1'}` |
| Expected Status | `415 Unsupported Media Type` |
| Actual Status | `201 Created` |

## Steps to Reproduce
1. Start the Flask backend and React frontend.
2. Send a `POST` request to the registration endpoint with the payload:
   json
   {
     "username": "validuser05",
     "password": "ValidPass1"
   }
   
3. Observe the HTTP response status code.

## Expected Behavior
The server should reject the request with **HTTP 415 Unsupported Media Type**, since the request payload is not sent with a supported `Content-Type` (e.g., `application/json`). The registration should not be processed.

## Actual Behavior
The server accepted the request and returned **HTTP 201 Created**, indicating that a new user account (`validuser05`) was successfully registered despite the malformed/unsupported request format.

## Impact
- **Severity**: Medium
- **Priority**: High
- The API does not enforce `Content-Type` validation on the registration endpoint.
- Malformed or non-JSON requests can create user accounts, potentially leading to:
  - Data integrity issues in the SQLite database.
  - Bypassing of client-side validation.
  - Inconsistent behavior between frontend (React/Ant Design) and backend (Flask).
- May mask other validation bugs (e.g., username uniqueness, password rules) if the request body is not parsed correctly.

## Environment
- **Frontend**: React + Ant Design
- **Backend**: Flask + SQLite
- **Test Type**: API / Negative test (invalid `Content-Type`)

## Suggested Fix
1. In the Flask registration route, explicitly validate the incoming request's `Content-Type` header.
2. If the header is missing or not `application/json`, return:
   python
   return jsonify({"error": "Unsupported Media Type"}), 415
   
3. Ensure the request body is parsed via `request.get_json()` only after the `Content-Type` check passes.
4. Add regression tests to cover:
   - Missing `Content-Type`
   - `Content-Type: text/plain`
   - `Content-Type: application/xml`
   - Malformed JSON body

## Attachments / Logs
- Request payload: `{'username': 'validuser05', 'password': 'ValidPass1'}`
- Expected status: `415`
- Actual status: `201`
- (Attach server logs and network trace if available.)