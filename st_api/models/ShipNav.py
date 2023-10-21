# generated by datamodel-codegen:
#   filename:  api-docs/models/ShipNav.json
#   timestamp: 2023-10-21T17:38:30+00:00

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, RootModel, constr
from typing_extensions import Literal


class WaypointType(
    RootModel[
        Literal[
            'PLANET',
            'GAS_GIANT',
            'MOON',
            'ORBITAL_STATION',
            'JUMP_GATE',
            'ASTEROID_FIELD',
            'NEBULA',
            'DEBRIS_FIELD',
            'GRAVITY_WELL',
        ]
    ]
):
    root: Literal[
        'PLANET',
        'GAS_GIANT',
        'MOON',
        'ORBITAL_STATION',
        'JUMP_GATE',
        'ASTEROID_FIELD',
        'NEBULA',
        'DEBRIS_FIELD',
        'GRAVITY_WELL',
    ] = Field(..., description='The type of waypoint.')


class ShipNavStatus(RootModel[Literal['IN_TRANSIT', 'IN_ORBIT', 'DOCKED']]):
    root: Literal['IN_TRANSIT', 'IN_ORBIT', 'DOCKED'] = Field(
        ..., description='The current status of the ship'
    )


class ShipNavFlightMode(RootModel[Literal['DRIFT', 'STEALTH', 'CRUISE', 'BURN']]):
    root: Literal['DRIFT', 'STEALTH', 'CRUISE', 'BURN'] = Field(
        ...,
        description="The ship's set speed when traveling between waypoints or systems.",
    )


class ShipNavRouteWaypoint(BaseModel):
    symbol: constr(min_length=1) = Field(..., description='The symbol of the waypoint.')
    type: WaypointType
    systemSymbol: constr(min_length=1) = Field(
        ..., description='The symbol of the system the waypoint is in.'
    )
    x: int = Field(..., description='Position in the universe in the x axis.')
    y: int = Field(..., description='Position in the universe in the y axis.')


class ShipNavRoute(BaseModel):
    destination: ShipNavRouteWaypoint
    departure: ShipNavRouteWaypoint = Field(
        ..., description='Deprecated. Use origin instead.'
    )
    origin: ShipNavRouteWaypoint
    departureTime: datetime = Field(
        ..., description="The date time of the ship's departure."
    )
    arrival: datetime = Field(
        ...,
        description="The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.",
    )


class ShipNav(BaseModel):
    systemSymbol: str = Field(
        ..., description="The system symbol of the ship's current location."
    )
    waypointSymbol: str = Field(
        ...,
        description="The waypoint symbol of the ship's current location, or if the ship is in-transit, the waypoint symbol of the ship's destination.",
    )
    route: ShipNavRoute
    status: ShipNavStatus
    flightMode: ShipNavFlightMode
