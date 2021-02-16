from pydantic import BaseModel


class Commit(BaseModel):
    id: str
    branchName: str
    commit: str
    uploadMethod: int
    s3Link: str
    status: int
    createdAt: str
    updatedAt: str
