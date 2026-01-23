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

Running Locally

Instructions will be added after the initial implementation.

Development Notes

This project may use AI-assisted tools (such as GitHub Copilot). All generated code is reviewed and understood by the author.
