from fastapi import FastAPI, Request

from src.core import check_url_safety

app = FastAPI()

@app.get("/health")

def health():
    return {"status": "ok"}


@app.get("/urlinfo/1/{hostname_and_port}/{original_path:path}")

#If the time allows me i would like to add a function that normalizes the url before checking it

def url_info(hostname_and_port: str, original_path: str, request: Request):
    query = request.url.query

    if query:
        full_url = f"http://{hostname_and_port}/{original_path}?{query}"
    else:
        full_url = f"http://{hostname_and_port}/{original_path}"

    result = check_url_safety(full_url)

    logger.info(f"Checked URL: {full_url} - Result: {result}")

    return {
        "hostname_and_port": hostname_and_port,
        "path": original_path,
        **result,
        "is_malware": False,
        "safe": True,
    }
