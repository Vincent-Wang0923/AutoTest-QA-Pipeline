# Product Requirements Document (PRD)

## 1. Overview
This PRD defines a minimal React+Flask target system used to validate the AI QA Plugin POC. It contains basic authentication flows with specific constraints to serve as a testing sandbox.

## 2. Scope
* **Registration**: Account creation with specific validation rules.
* **Login**: Standard credential verification.

## 3. Rules

### 3.1 Registration Rules
| Field | Type | Required | Validation Rules | Error Message |
| :--- | :--- | :--- | :--- | :--- |
| username | String | Yes | Min length: 6 chars <br> Must be unique | Conflict: "Username already exists" <br> Length: "Username must be at least 6 characters" |
| password | String | Yes | Cannot be empty | Null: "Password required" |

### 3.2 Login Rules
* Credentials must match database records.
* Success: HTTP 200, return user_id, show "Login successful".
* Fail: HTTP 401, show "Invalid credentials".

## 4. Tech Stack
* **Frontend**: React, Ant Design
* **Backend**: Flask, SQLite