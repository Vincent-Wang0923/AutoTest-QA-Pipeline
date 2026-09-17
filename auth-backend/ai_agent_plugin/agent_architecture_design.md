# AI QA Agent Plugin - POC Design Document

## 1. Why We Built This (Design Purpose)
Writing automated test scripts by hand takes a lot of time and effort. The goal of this plugin is to use an LLM (Large Language Model) to read requirements, run tests, and report bugs automatically, creating a fully automated QA loop without human intervention. 

This current version is a Proof of Concept (POC). We built a simple React + Flask login/register system as a target to prove that this workflow actually works.

## 2. Core Workflow
The Agent runs in 6 main steps:

*   **Phase 1: Reading the PRD (Knowledge Ingestion)**
    *   The Agent reads `PRD_and_Requirements.md`.
    *   Goal: Let the AI understand the basic business rules of the system (for example, "the username must be at least 6 characters").
*   **Phase 2: Understanding Test Cases (Data Structuring)**
    *   The Agent reads `Test_Cases.md` and uses a prompt to turn the Markdown table into a structured JSON list.
    *   Goal: Get the exact test data (Test ID, Payload like `{"username": "admin"}`, and expected HTTP status code).
*   **Phase 3: Running the Tests (Action Execution)**
    *   The Agent switches to standard Python code. It uses the `requests` library to send real HTTP POST requests to the local Flask backend using the data extracted in Phase 2.
*   **Phase 4: Checking the Results (Dynamic Assertion)**
    *   The Agent compares the real response code from the backend with the expected status code.
    *   If they match, the test passes. If they don't (for example, the system accepted a short username and returned 201 instead of 400), it catches the bug.
*   **Phase 5: Writing the Report (Report Generation)**
    *   The Agent calls the LLM again. It gives the LLM the PRD rules, the test data, and the wrong response, asking it to write a complete Markdown bug report just like a real QA engineer would.
*   **Phase 6: Saving the Bug (Bug Tracking)**
    *   The script saves the AI-generated Markdown report into the local `reports/` folder. 
    *   *Note: In a future official version, this step would be replaced by automatically creating a ticket in Jira or GitHub Issues.*

## 3. Tech Stack
*   **Controller:** Python 3 + `requests` (handles the local logic, file reading, and API calls).
*   **AI Engine:** OpenAI-compatible API (cost-effective and great at processing structured data).
*   **Target System:** Flask + SQLite (Backend) / React + Ant Design (Frontend).
*   **Data Format:** Markdown (easy for humans and AI to read) and JSON (for passing data in code).

## 4. Future Plans
Right now, this POC can successfully find backend API logic bugs and generate reports for them. In the future, we plan to add frontend UI testing frameworks (like Cypress) to the loop. We also want to explore if the AI can not only find the bug, but directly locate the exact broken code file and suggest a fix.