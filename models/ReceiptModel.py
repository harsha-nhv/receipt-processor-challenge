from pydantic import BaseModel, Field

class ItemModel(BaseModel):

    description: str = Field(
        alias = "shortDescription",
        description = "description about item",
        example = "Gluten Free",
        title = "shortDescription"
    )

    price: str = Field(
        alias = "price",
        description = "Item price",
        example = "50",
        title = "price"
    )

class ReceiptModel(BaseModel):

    retailer: str = Field(
        alias = "retailer",
        description = "name of the retailer",
        example = "Walgreens",
        title = "retailer"
    )

    purchaseDate: str = Field(
        alias = "purchaseDate",
        description = "purchased date",
        example = "2025-03-21",
        title = "purchaseDate"
    )

    purchaseTime: str = Field(
        alias = "purchaseTime",
        description = "purchase time",
        example = "08:13",
        title = "purchaseTime"
    )

    totalAmount: str = Field(
        alias = "total",
        description = "purchased amount",
        example = "2.65",
        title = "total"
    )

    items: list[ItemModel]