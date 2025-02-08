from pydantic import BaseModel, Field


class CountryModel(BaseModel):
    code: str = Field(description="The country code example US")
