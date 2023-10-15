# generated by datamodel-codegen:
#   filename:  api-docs/models/ShipReactor.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, RootModel, conint


class Symbol(Enum):
    REACTOR_SOLAR_I = "REACTOR_SOLAR_I"
    REACTOR_FUSION_I = "REACTOR_FUSION_I"
    REACTOR_FISSION_I = "REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I = "REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I = "REACTOR_ANTIMATTER_I"


class ShipCondition(RootModel[conint(ge=0, le=100)]):
    root: conint(ge=0, le=100) = Field(
        ...,
        description="Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new.",
    )


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


class ShipReactor(BaseModel):
    symbol: Symbol = Field(..., description="Symbol of the reactor.")
    name: str = Field(..., description="Name of the reactor.")
    description: str = Field(..., description="Description of the reactor.")
    condition: Optional[ShipCondition] = None
    powerOutput: conint(ge=1) = Field(
        ...,
        description="The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.",
    )
    requirements: ShipRequirements
