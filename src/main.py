from fastapi import FastAPI

app = FastAPI()

@app.get("/health")

def health():
    return {"status": "ok"}


@app.get("/urlinfo/1/{hostname_and_port}/{original_path:path}")




def url_info(hostname_and_port: str, original_path: str):
    query = request.url.query
    if query:
        full_url = f"http://{hostname_and_port}/{original_path}?{query}"
    else:
        full_url = f"http://{hostname_and_port}/{original_path}"
    
    result = check_url_safety(full_url)

    return {
        "hostname_and_port": hostname_and_port,
        "path": original_path,
        **result,
        "is_malware": False,
        "safe": True,
    }
