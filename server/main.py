from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class HelloWorld(BaseModel):
    message: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/hello-world", response_model=HelloWorld)
async def hello_world() -> HelloWorld:
    return HelloWorld(message="Hello world")


@app.get("/items/{item_id}", response_model=Item)
# パスパラメータではない関数パラメータを宣言すると、それらは自動的に "クエリ" パラメータとして解釈されます。
# Unionを持ちることで、オプショナルなクエリを設定できる
async def read_item(
    item_id, skip: int = 0, bool: bool = False, option: Union[str, None] = None
) -> Item:
    if option is None:
        return Item(name=item_id + str(skip) + str(bool), price=12.9)
    return Item(name=item_id + str(skip) + str(bool) + option, price=12.9)


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
