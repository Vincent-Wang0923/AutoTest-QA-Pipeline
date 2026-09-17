# Bug Report

**Issue ID:** BUG-POC-001
**Status:** Open
**Severity:** P1 (Critical)
**Module:** Backend API (`/api/register`)

## 1. Summary
Registration API allows usernames under 6 characters to be saved.

## 2. Steps to Reproduce
1. Start frontend and backend servers.
2. Go to `http://localhost:3000/register`.
3. Enter `admin` in the Username field (5 chars).
4. Enter `123456` in the Password field.
5. Click Register.

## 3. Actual Result
No error thrown. UI shows "Registration successful". Network tab shows HTTP 201. DB confirms the 5-char account was created.

## 4. Expected Result
Per PRD 3.1, the system should block the request, show "Username must be at least 6 characters", and return an error status.

## 5. Root Cause
* Backend: `/api/register` lacks `len(username) < 6` check.
* Frontend: `<Form.Item>` config is missing the `min: 6` rule.