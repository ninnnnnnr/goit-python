from pydantic import BaseModel


class FirsSource(BaseModel):
    id: int
    text: str
    url: str
    time: str

    class Config:
        orm_mode = True


class SecondSource(BaseModel):
    id: int
    text: str
    url: str
    time: str

    class Config:
        orm_mode = True
