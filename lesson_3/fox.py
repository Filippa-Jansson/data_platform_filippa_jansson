from pydantic import BaseModel

class FoxSchema(BaseModel):
    image: str
    link: str