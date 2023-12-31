# generated by datamodel-codegen:
#   filename:  api-docs/models/MarketTransaction.json
#   timestamp: 2023-10-21T17:38:30+00:00

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, conint
from typing_extensions import Literal


class MarketTransaction(BaseModel):
    waypointSymbol: str = Field(
        ..., description='The symbol of the waypoint where the transaction took place.'
    )
    shipSymbol: str = Field(
        ..., description='The symbol of the ship that made the transaction.'
    )
    tradeSymbol: str = Field(..., description='The symbol of the trade good.')
    type: Literal['PURCHASE', 'SELL'] = Field(
        ..., description='The type of transaction.'
    )
    units: conint(ge=0) = Field(
        ..., description='The number of units of the transaction.'
    )
    pricePerUnit: conint(ge=0) = Field(
        ..., description='The price per unit of the transaction.'
    )
    totalPrice: conint(ge=0) = Field(
        ..., description='The total price of the transaction.'
    )
    timestamp: datetime = Field(..., description='The timestamp of the transaction.')
