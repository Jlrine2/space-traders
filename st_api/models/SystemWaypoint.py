# generated by datamodel-codegen:
#   filename:  api-docs/models/SystemWaypoint.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, constr


class WaypointType(Enum):
    PLANET = "PLANET"
    GAS_GIANT = "GAS_GIANT"
    MOON = "MOON"
    ORBITAL_STATION = "ORBITAL_STATION"
    JUMP_GATE = "JUMP_GATE"
    ASTEROID_FIELD = "ASTEROID_FIELD"
    NEBULA = "NEBULA"
    DEBRIS_FIELD = "DEBRIS_FIELD"
    GRAVITY_WELL = "GRAVITY_WELL"


class WaypointOrbital(BaseModel):
    symbol: constr(min_length=1) = Field(
        ..., description="The symbol of the orbiting waypoint."
    )


class SystemWaypoint(BaseModel):
    symbol: str = Field(..., description="The symbol of the waypoint.")
    type: WaypointType
    x: int = Field(
        ...,
        description="Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.",
    )
    y: int = Field(
        ...,
        description="Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.",
    )
    orbitals: List[WaypointOrbital] = Field(
        ..., description="Waypoints that orbit this waypoint."
    )
    orbits: Optional[constr(min_length=1)] = Field(
        None,
        description="The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.",
    )
