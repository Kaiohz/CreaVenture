from pydantic import BaseModel, Field


class BinaryModel(BaseModel):
    binary: str = Field(description="yes or no")
