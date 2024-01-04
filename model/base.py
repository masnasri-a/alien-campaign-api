from pydantic import BaseModel
class BasePagination(BaseModel):
    page: int = 1
    limit: int = 10
    search: str = ""