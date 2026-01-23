from pydactic import BaseModel

class UrlCheckResponse(BaseModel):
    url: str
    is_malware: bool
    safe: bool
