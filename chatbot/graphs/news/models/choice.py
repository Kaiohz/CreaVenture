from pydantic import BaseModel, Field


class ChoiceModel(BaseModel):
    choice: str = Field(description="The choice betwween Headlines or Specific news")
