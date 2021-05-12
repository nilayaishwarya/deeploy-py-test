from typing import Optional, List, Any

from pydantic import BaseModel

class DockerReference(BaseModel):
    image: str
    port: Optional[int]

class ModelReference(BaseModel):
    docker: Optional[DockerReference]
    blob: Optional[str]

class ModelReferenceJson(BaseModel):
    reference: ModelReference
