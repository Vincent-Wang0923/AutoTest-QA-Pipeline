# Test Cases Document: `/register` API

## Overview
This document outlines the test cases for the `/register` API endpoint of the React+Flask target system. The endpoint is responsible for account creation and must enforce the validation rules defined in the PRD (Section 3.1).

## Endpoint Details
- **Method**: `POST`
- **Path**: `/register`
- **Content-Type**: `application/json`
- **Request Body**: `{ "username": <string>, "password": <string> }`

## Test Cases

| ID | Type | Scenario | Steps | Payload (username/password) | Expected Status Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-REG-001 | Functional | Successful registration with valid unique username and non-empty password | 1. Send POST to `/register` with valid payload <br> 2. Verify response body contains new user_id | `"validuser01" / "SecurePass123"` | 201 |
| TC-REG-002 | Functional | Successful registration with minimum-length username (exactly 6 chars) | 1. Send POST to `/register` with 6-char username <br> 2. Verify user is created | `"user01" / "Passw0rd!"` | 201 |
| TC-REG-003 | Functional | Successful registration with long username and complex password | 1. Send POST to `/register` with long username <br> 2. Verify user is created | `"averylongusername12345" / "C0mpl3x!Pass#2024"` | 201 |
| TC-REG-004 | Functional | Registration fails when username already exists | 1. Register `"existinguser"` first <br> 2. Send POST to `/register` with same username <br> 3. Verify error message "Username already exists" | `"existinguser" / "AnotherPass1"` | 409 |
| TC-REG-005 | Functional | Registration fails when password is empty string | 1. Send POST to `/register` with empty password <br> 2. Verify error message "Password required" | `"validuser02" / ""` | 400 |
| TC-REG-006 | Functional | Registration fails when password field is missing | 1. Send POST to `/register` with only username <br> 2. Verify error message "Password required" | `"validuser03" / <omitted>` | 400 |
| TC-REG-007 | Functional | Registration fails when username field is missing | 1. Send POST to `/register` with only password <br> 2. Verify validation error returned | `<omitted> / "SomePass123"` | 400 |
| TC-REG-008 | Boundary | Username length is 5 characters (one below minimum) | 1. Send POST to `/register` with 5-char username <br> 2. Verify error message "Username must be at least 6 characters" | `"user1" / "ValidPass1"` | 400 |
| TC-REG-009 | Boundary | Username length is exactly 6 characters (minimum boundary) | 1. Send POST to `/register` with 6-char username <br> 2. Verify user is created | `"user12" / "ValidPass1"` | 201 |
| TC-REG-010 | Boundary | Username length is 7 characters (just above minimum) | 1. Send POST to `/register` with 7-char username <br> 2. Verify user is created | `"user123" / "ValidPass1"` | 201 |
| TC-REG-011 | Boundary | Username length is 0 (empty string) | 1. Send POST to `/register` with empty username <br> 2. Verify validation error returned | `"" / "ValidPass1"` | 400 |
| TC-REG-012 | Boundary | Username length is 1 character | 1. Send POST to `/register` with 1-char username <br> 2. Verify error message "Username must be at least 6 characters" | `"a" / "ValidPass1"` | 400 |
| TC-REG-013 | Boundary | Password length is 1 character (minimum non-empty) | 1. Send POST to `/register` with 1-char password <br> 2. Verify user is created (no min length rule for password) | `"validuser04" / "x"` | 201 |
| TC-REG-014 | Boundary | Username with maximum reasonable length (e.g., 255 chars) | 1. Send POST to `/register` with 255-char username <br> 2. Verify system handles gracefully | `"a"*255 / "ValidPass1"` | 201 or 400 |
| TC-REG-015 | Boundary | Username with whitespace only (6 spaces) | 1. Send POST to `/register` with whitespace username <br> 2. Verify validation behavior | `"      " / "ValidPass1"` | 400 |
| TC-REG-016 | Exception | Malformed JSON body | 1. Send POST to `/register` with invalid JSON <br> 2. Verify 400 error returned | `{invalid-json}` | 400 |
| TC-REG-017 | Exception | Missing Content-Type header | 1. Send POST to `/register` without `application/json` header <br> 2. Verify 415 or 400 error | `"validuser05" / "ValidPass1"` | 415 |
| TC-REG-018 | Exception | Username provided as integer instead of string | 1. Send POST to `/register` with numeric username <br> 2. Verify type validation error | `123456 / "ValidPass1"` | 400 |
| TC-REG-019 | Exception | Password provided as integer instead of string | 1. Send POST to `/register` with numeric password <br> 2. Verify type validation error | `"validuser06" / 123456` | 400 |
| TC-REG-020 | Exception | Username provided as null | 1. Send POST to `/register` with null username <br> 2. Verify validation error | `null / "ValidPass1"` | 400 |
| TC-REG-021 | Exception | Password provided as null | 1. Send POST to `/register` with null password <br> 2. Verify error message "Password required" | `"validuser07" / null` | 400 |
| TC-REG-022 | Exception | Username contains SQL injection payload | 1. Send POST to `/register` with SQLi string <br> 2. Verify input is sanitized and no DB error | `"'; DROP TABLE users;--" / "ValidPass1"` | 400 |
| TC-REG-023 | Exception | Username contains XSS payload | 1. Send POST to `/register` with script tag <br> 2. Verify input is sanitized | `"<script>alert(1)</script>" / "ValidPass1"` | 400 |
| TC-REG-024 | Exception | Duplicate registration attempt with case variation | 1. Register `"ValidUser"` <br> 2. Attempt register `"validuser"` <br> 3. Verify uniqueness handling (case sensitivity per spec) | `"validuser" / "ValidPass1"` | 409 or 201 |
| TC-REG-025 | Exception | Empty request body | 1. Send POST to `/register` with `{}` <br> 2. Verify both field validations trigger | `{}` | 400 |
| TC-REG-026 | Exception | Extra unexpected fields in payload | 1. Send POST to `/register` with additional fields <br> 2. Verify extra fields are ignored and user is created | `"validuser08" / "ValidPass1" / "role":"admin"` | 201 |
| TC-REG-027 | Exception | Concurrent registration with same username | 1. Fire two simultaneous POST requests with same username <br> 2. Verify only one succeeds, other returns 409 | `"raceuser" / "ValidPass1"` (x2) | 201 & 409 |
| TC-REG-028 | Exception | Username with special/unicode characters | 1. Send POST to `/register` with unicode username <br> 2. Verify handling per spec | `"üserñame" / "ValidPass1"` | 201 or 400 |

## Notes
- **Status Code Assumptions**: The PRD does not explicitly define HTTP status codes for registration. The following conventions are assumed:
  - `201 Created` — successful registration
  - `400 Bad Request` — validation failure (length, empty, type)
  - `409 Conflict` — username already exists
  - `415 Unsupported Media Type` — wrong/missing Content-Type
- Test cases TC-REG-014, TC-REG-024, and TC-REG-028 have ambiguous expected outcomes because the PRD does not specify max length, case sensitivity, or character set rules. These should be clarified with the product owner.
- All tests should verify the response body contains the appropriate error message as specified in the PRD (Section 3.1).