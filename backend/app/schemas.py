from pydantic import BaseModel
from typing import List, Dict

class UrlResponse(BaseModel):
    urls: List[str]

class ContentResponse(BaseModel):
    contents: Dict[str, Dict[str, str]]
