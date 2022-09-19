from fastapi import APIRouter

from app.schema import Item

router = APIRouter()


@router.get("/")
def reed_root():
    """Hello world.

    Returns:
        dict: {"hello": "world!"}
    """
    return {"hello": "world!"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    """Entry poiny with path parameter.

    Args:
        item_id (int): path parameter

    Returns:
        dict: {"item_id": item_id}
    """
    return {"item_id": item_id}


@router.get("/items/")
async def read_user(user_id: str, q: str | None = None):
    """Entry poiny with query parameter.

    Args:
        user_id (str): required query parameter
        q (str | None, optional): optional query parameter

    Returns:
        dict: {"user_id": user_id} and {"q": q} if q is not None
    """
    result = {"user_id": user_id}
    if q:
        result.update({"q": q})
    return result


@router.post("/items/")
async def create_item(item: Item):
    """Entery point with request body.

    Args:
        item (Item): pydentic BaseModel

    Returns:
        dict: BaseModel dict
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
