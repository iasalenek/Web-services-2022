from pydantic import BaseModel


class Item(BaseModel):
    """Try pydantic BaseModel."""

    name: str
    descriotion: str | None = None
    price: float
    tax: float | None = None
