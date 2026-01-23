URL Reputation Lookup Service

Overview

This project implements a small HTTP API that checks requested URLs against a dataset of known malicious URLs and returns whether the URL is malicious or safe.

The service is designed to be called synchronously by an HTTP proxy before allowing outbound connections.

API

Lookup Endpoint

GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

Example:

GET /urlinfo/1/www.evil.com:80/download?file=virus.exe

Example response:

{
"malicious": true
}

Goals
• Simple and readable implementation
• Easy to run locally on macOS or Linux
• Basic automated tests
• Clean Git workflow

Installation & Usage

1. Clone the repository
   git clone <your-repo-url>
   cd URL_lookup_service
   
2. Create a Python virtual environment
   python3 -m venv .venv
   source .venv/bin/activate   # On Linux/macOS
   # .venv\Scripts\activate    # On Windows
  
3. Install dependencies
   pip install --upgrade pip
   pip install -r requirements.txt

4. Run the application
   uvicorn src.main:app --reload
   
The API will run at: http://127.0.0.1:8000￼
Open http://127.0.0.1:8000/docs￼ to view the Swagger UI.

5. Run tests
  in terminal insert: pytest

Development Notes

This project may use AI-assisted tools (such as GitHub Copilot). All generated code is reviewed and understood by the author.
