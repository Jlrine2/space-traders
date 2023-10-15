# generated by datamodel-codegen:
#   filename:  api-docs/models/ShipCargoItem.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from pydantic import BaseModel, Field, conint


class ShipCargoItem(BaseModel):
    symbol: str = Field(
        ..., description="The unique identifier of the cargo item type."
    )
    name: str = Field(..., description="The name of the cargo item type.")
    description: str = Field(..., description="The description of the cargo item type.")
    units: conint(ge=1) = Field(
        ..., description="The number of units of the cargo item."
    )
