from pydantic import BaseModel, Field


class TopicModel(BaseModel):
    topic: str = Field(description="The topic of the question")
