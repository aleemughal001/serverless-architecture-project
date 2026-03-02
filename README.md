# 🚀 Serverless REST API Demo (AWS Lambda + API Gateway)

## 🎯 Goal
Build a simple **serverless REST API** using AWS services:
- **API Gateway** receives an HTTP request
- **Lambda** runs Python code
- Lambda calls an external public API (**JSONPlaceholder**)
- Response is returned back to the client (Postman)

---

## 🧱 Architecture (High-Level Flow)

Postman (Client)
   |
   v
API Gateway (HTTP endpoint)
   |
   v
AWS Lambda (Python handler)
   |
   v
External API (https://jsonplaceholder.typicode.com/todos/1)
   |
   v
JSON Response back to Postman

---

## 🧰 Tech Stack
- AWS Lambda (Python)
- AWS Lambda Layer (requests dependency)
- API Gateway (REST API)
- Postman (testing)

---

## 📁 Repository Files
- `lambda_function.py` → Lambda handler code
- `config.py` → stores the base URL (configuration)
- `README.md` → this documentation

---

## ✅ Step-by-Step: What I Did

### 1) Created the Lambda Function Code
Created `lambda_function.py`:

```python
import json
import requests
from config import base_url

def lambda_handler(event, context):
    res = requests.get(url=base_url + 'todos/1')
    return {
        "statusCode": res.status_code,
        "body": json.dumps(res.json())
    }


