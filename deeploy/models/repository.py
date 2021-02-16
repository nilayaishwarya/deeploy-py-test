from typing import List

from pydantic import BaseModel

from .commit import Commit


class Repository(BaseModel):
    id: str
    name: str
    status: int
    isArchived: bool
    workspaceId: str
    isPublic: bool
    gitSSHPullLink: str
    createdAt: str
    updatedAt: str
    commits: List[Commit]
