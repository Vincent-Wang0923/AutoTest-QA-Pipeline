# Test Cases

**Module:** Auth
**Reference:** Target System PRD v1.0

## Test Scenarios

| ID | Type | Scenario | Steps | Data | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **001** | Functional testing | Valid registration | 1. Go to `/register`<br>2. Fill username/password<br>3. Submit | `username`: testuser<br>`password`: pwd123 | HTTP 201, prompt success, data saved. |
| **002** | Boundary testing | Username length < 6 | 1. Go to `/register`<br>2. Fill short username<br>3. Submit | `username`: **admin**<br>`password`: pwd123 | **HTTP 400, prompt "Username must be at least 6 characters", data rejected.** |
| **003** | Exception testing | Duplicate username | 1. Go to `/register`<br>2. Fill existing username<br>3. Submit | `username`: testuser<br>`password`: 999999 | HTTP 409, prompt "Username already exists". |
| **004** | Functional testing | Valid login | 1. Go to `/`<br>2. Fill registered credentials<br>3. Submit | `username`: testuser<br>`password`: pwd123 | HTTP 200, prompt success, return `user_id`. |