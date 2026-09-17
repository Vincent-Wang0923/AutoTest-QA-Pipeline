import os
import json
import requests
from openai import OpenAI

client = OpenAI(
    api_key="sk-41b3f5226a67482c9f62cf84a8d37ba9", 
    base_url="https://api.deepseek.com"
)

with open("../docs/PRD_and_Requirements.md", "r", encoding="utf-8") as f:
    prd_content = f.read()

with open("../docs/Test_Cases.md", "r", encoding="utf-8") as f:
    test_cases_content = f.read()

print("Agent is reading all test cases...")
parse_prompt = f"""
Read the Test Cases document:
{test_cases_content}

Extract all test cases related to the '/register' API.
Output ONLY a valid JSON array. Each object in the array must have:
- "id" (string, e.g., "001")
- "username" (string)
- "password" (string)
- "expected_status" (integer, e.g., 201, 400, 409)

Do not include markdown tags.
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": parse_prompt}],
    temperature=0.1
)

raw_output = response.choices[0].message.content.strip().replace("```json", "").replace("```", "")
test_cases_list = json.loads(raw_output)

os.makedirs("../ai_generated_report", exist_ok=True)
api_url = "http://localhost:5000/api/register"

for tc in test_cases_list:
    print(f"\n--- Running Test Case: {tc['id']} ---")
    
    payload = {"username": tc["username"], "password": tc["password"]}
    print(f"Payload: {payload}")
    
    try:
        res = requests.post(api_url, json=payload)
        print(f"Expected: {tc['expected_status']}, Actual: {res.status_code}")
        
        if res.status_code != tc['expected_status']:
            print(f"Bug found in {tc['id']}! Writing report...")
            
            report_prompt = f"""
            You are a QA. Write a Bug Report in Markdown for test case {tc['id']}.
            
            PRD: {prd_content}
            
            Execution Info:
            - Payload: {payload}
            - Expected Status: {tc['expected_status']}
            - Actual Status: {res.status_code}
            
            Output ONLY Markdown text.
            """
            
            report_res = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": report_prompt}],
                temperature=0.3
            )
            
            ai_generated_report = report_res.choices[0].message.content.strip().replace("```markdown", "").replace("```", "")
            
            report_path = f"../ai_generated_report/BUG-AI-{tc['id']}_Auto_Report.md"
            
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(ai_generated_report)
                
            print(f"Report saved to -> {report_path}")
        else:
            print("Pass! System works fine.")
            
    except Exception as e:
        print(f"Error connecting to backend: {e}")