# generated by datamodel-codegen:
#   filename:  api-docs/models/ShipRequirements.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ShipRequirements(BaseModel):
    power: Optional[int] = Field(
        None, description="The amount of power required from the reactor."
    )
    crew: Optional[int] = Field(
        None, description="The number of crew required for operation."
    )
    slots: Optional[int] = Field(
        None, description="The number of module slots required for installation."
    )
