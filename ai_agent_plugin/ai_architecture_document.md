# AI QA Agent Plugin - Architecture Document

### 1. Background & Goal
The goal of this plugin is to build a fully automated QA pipeline. Instead of writing test scripts or test cases by hand, this Agent uses the Product Requirements Document (PRD) as its only input. It acts as a virtual QA team that independently reads requirements, designs test cases, executes them, and reports bugs.

### 2. How It Works (Workflow)
The Agent is driven by a Python script that coordinates LLM API calls and local network requests in 5 steps:

*   **Step 1: Test Case Generation (LLM)**
    The Agent reads the target system's `PRD_and_Requirements.md` to understand business rules and boundary conditions. It then automatically writes a complete test suite in Markdown format (`Test_Cases_Auto.md`).
*   **Step 2: Data Extraction (LLM)**
    The Agent parses the newly generated test cases and converts the text into a machine-readable JSON array, extracting exact parameters like `username`, `password`, and `expected_status`.
*   **Step 3: Execution (Python/Requests)**
    Operating purely in Python, the script loops through the JSON array. It sends real HTTP POST requests with the generated payloads directly to the local Flask backend.
*   **Step 4: Bug Reporting (LLM)**
    The Agent compares the expected status code with the actual API response. If a bug is found (e.g., expected `400 Bad Request` but received `201 Created`), the Agent sends the failure context back to the LLM to automatically generate a detailed bug ticket (`BUG-AI-{id}_Auto.md`).
*   **Step 5: Final Summary (LLM)**
    Once all tests finish, the Agent calculates the pass/fail metrics and generates a final executive summary (`Test_Report_Auto.md`) with a release recommendation.

### 3. Tech Stack
*   **Core Script:** Python 3 + `requests` (handles file I/O and API payload delivery).
*   **AI Engine:** OpenAI-compatible API (DeepSeek) for natural language processing and structured data extraction.
*   **Target Application:** Local Flask + SQLite backend, React + Ant Design frontend (intentionally seeded with logic bugs to validate the Agent).
*   **Data Formats:** Markdown (for human-readable inputs/outputs) and JSON (for internal script data passing).

### 4. Limitations & Future Plans
While this fully automated approach works great as a Proof of Concept (POC), real-world enterprise environments require more safety constraints. LLMs are generative and can sometimes "hallucinate" or over-extrapolate rules—for example, automatically executing security stress tests (like SQL injection) even if not explicitly requested in the PRD.

To bridge the gap between this prototype and a production-ready tool, future iterations should reintroduce a **Human-in-the-loop (HITL)** step. The pipeline would pause after Step 1, allowing a human QA engineer to review, modify, and approve the AI-generated test cases before execution. This hybrid approach combines the heavy-lifting speed of AI with the necessary oversight of human engineering.