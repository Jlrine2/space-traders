# generated by datamodel-codegen:
#   filename:  api-docs/models/ConnectedSystem.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, constr


class SystemType(Enum):
    NEUTRON_STAR = "NEUTRON_STAR"
    RED_STAR = "RED_STAR"
    ORANGE_STAR = "ORANGE_STAR"
    BLUE_STAR = "BLUE_STAR"
    YOUNG_STAR = "YOUNG_STAR"
    WHITE_DWARF = "WHITE_DWARF"
    BLACK_HOLE = "BLACK_HOLE"
    HYPERGIANT = "HYPERGIANT"
    NEBULA = "NEBULA"
    UNSTABLE = "UNSTABLE"


class ConnectedSystem(BaseModel):
    symbol: constr(min_length=1) = Field(..., description="The symbol of the system.")
    sectorSymbol: constr(min_length=1) = Field(
        ..., description="The sector of this system."
    )
    type: SystemType
    factionSymbol: Optional[str] = Field(
        None,
        description="The symbol of the faction that owns the connected jump gate in the system.",
    )
    x: int = Field(..., description="Position in the universe in the x axis.")
    y: int = Field(..., description="Position in the universe in the y axis.")
    distance: int = Field(
        ..., description="The distance of this system to the connected Jump Gate."
    )
