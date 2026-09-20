import os
import json
import requests
from openai import OpenAI

client=OpenAI(
    api_key="sk-41b3f5226a67482c9f62cf84a8d37ba9", 
    base_url="https://api.deepseek.com"
)

os.makedirs("../ai_generated_report", exist_ok=True)
api_url="http://localhost:5000/api/register"

print("Reading PRD and analyzing test strategy.")
with open("../docs/PRD_and_Requirements.md", "r", encoding="utf-8") as f:
    prd_content = f.read()

tc_generation_prompt = f"""
You are a Senior QA Automation Engineer. Read the following PRD:
{prd_content}

Generate a comprehensive Test Cases document in Markdown format for the '/register' API.
Include Functional, Boundary, and Exception testing.
Use a table with columns: ID, Type, Scenario, Steps, Payload (username/password), Expected Status Code.
Output ONLY the Markdown text.
"""

tc_response=client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": tc_generation_prompt}],
    temperature=0.3
)

ai_generated_tcs=tc_response.choices[0].message.content.strip().replace("```markdown", "").replace("```", "")

with open("../ai_generated_report/Test_Cases_Auto.md", "w", encoding="utf-8") as f:
    f.write(ai_generated_tcs)

print("Generated Test_Cases_Auto.md.")
print("Parsing test cases into execution instructions.")

parse_prompt=f"""
Based on these test cases you just wrote:
{ai_generated_tcs}

Extract all test cases into a JSON array. Each object must have:
- "id" (string)
- "username" (string)
- "password" (string)
- "expected_status" (integer)
Output ONLY valid JSON.
"""

json_response=client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": parse_prompt}],
    temperature=0.1
)

raw_json=json_response.choices[0].message.content.strip().replace("```json", "").replace("```", "")
test_cases_list=json.loads(raw_json)

print("Executing automated API tests.")
execution_results=[]

for tc in test_cases_list:
    payload={"username": tc["username"], "password": tc["password"]}
    try:
        res=requests.post(api_url, json=payload)
        actual_status=res.status_code
        status="Pass" if actual_status == tc['expected_status'] else "Fail"
        
        execution_results.append({
            "id": tc["id"],
            "payload": payload,
            "expected": tc['expected_status'],
            "actual": actual_status,
            "status": status
        })
        
        if status == "Fail":
            print(f"Defect found in {tc['id']}, generating bug report.")
            
            bug_prompt = f"""
            Write a Bug Report in Markdown for test case {tc['id']}.
            PRD Rules: {prd_content}
            Payload injected: {payload}
            Expected Status: {tc['expected_status']}
            Actual Status: {actual_status}
            Output ONLY Markdown text.
            """
            
            bug_res = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": bug_prompt}],
                temperature=0.3
            )
            
            bug_report = bug_res.choices[0].message.content.strip().replace("```markdown", "").replace("```", "")
            
            with open(f"../ai_generated_report/BUG-AI-{tc['id']}_Auto.md", "w", encoding="utf-8") as f:
                f.write(bug_report)
                
    except Exception as e:
        print(f"Error on {tc['id']}: {e}")

print("Generating global test report.")

report_prompt = f"""
You are the QA Lead. Based on the following execution results, write a comprehensive Test Report in Markdown.
Execution Results: {json.dumps(execution_results)}
Include: Executive Summary, Test Execution Matrix (Table), Bug Summary, and QA Sign-off conclusion.
Output ONLY Markdown text.
"""

report_res=client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": report_prompt}],
    temperature=0.3
)

final_report=report_res.choices[0].message.content.strip().replace("```markdown", "").replace("```", "")

with open("../ai_generated_report/Test_Report_Auto.md", "w", encoding="utf-8") as f:
    f.write(final_report)

print("Generated Test_Report_Auto.md.")
print("Test execution completed.")