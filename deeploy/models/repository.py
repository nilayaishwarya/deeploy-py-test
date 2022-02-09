from typing import Optional

from pydantic import BaseModel

from deeploy.common.functions import to_lower_camel


class Repository(BaseModel):
    id: str
    name: str
    status: int
    isArchived: bool
    workspaceId: str
    isPublic: Optional[bool]
    remotePath: str
    createdAt: str
    updatedAt: str

    class Config:
        alias_generator = to_lower_camel
