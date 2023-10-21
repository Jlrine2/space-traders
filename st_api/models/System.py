# generated by datamodel-codegen:
#   filename:  api-docs/models/System.json
#   timestamp: 2023-10-21T17:38:30+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, RootModel, constr
from typing_extensions import Literal


class SystemType(
    RootModel[
        Literal[
            'NEUTRON_STAR',
            'RED_STAR',
            'ORANGE_STAR',
            'BLUE_STAR',
            'YOUNG_STAR',
            'WHITE_DWARF',
            'BLACK_HOLE',
            'HYPERGIANT',
            'NEBULA',
            'UNSTABLE',
        ]
    ]
):
    root: Literal[
        'NEUTRON_STAR',
        'RED_STAR',
        'ORANGE_STAR',
        'BLUE_STAR',
        'YOUNG_STAR',
        'WHITE_DWARF',
        'BLACK_HOLE',
        'HYPERGIANT',
        'NEBULA',
        'UNSTABLE',
    ] = Field(..., description='The type of waypoint.')


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


class WaypointOrbital(BaseModel):
    symbol: constr(min_length=1) = Field(
        ..., description='The symbol of the orbiting waypoint.'
    )


class FactionSymbols(
    RootModel[
        Literal[
            'COSMIC',
            'VOID',
            'GALACTIC',
            'QUANTUM',
            'DOMINION',
            'ASTRO',
            'CORSAIRS',
            'OBSIDIAN',
            'AEGIS',
            'UNITED',
            'SOLITARY',
            'COBALT',
            'OMEGA',
            'ECHO',
            'LORDS',
            'CULT',
            'ANCIENTS',
            'SHADOW',
            'ETHEREAL',
        ]
    ]
):
    root: Literal[
        'COSMIC',
        'VOID',
        'GALACTIC',
        'QUANTUM',
        'DOMINION',
        'ASTRO',
        'CORSAIRS',
        'OBSIDIAN',
        'AEGIS',
        'UNITED',
        'SOLITARY',
        'COBALT',
        'OMEGA',
        'ECHO',
        'LORDS',
        'CULT',
        'ANCIENTS',
        'SHADOW',
        'ETHEREAL',
    ] = Field(..., description='The symbol of the faction.', examples=['COSMIC'])


class SystemWaypoint(BaseModel):
    symbol: str = Field(..., description='The symbol of the waypoint.')
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
        ..., description='Waypoints that orbit this waypoint.'
    )
    orbits: Optional[constr(min_length=1)] = Field(
        None,
        description='The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.',
    )


class SystemFaction(BaseModel):
    symbol: FactionSymbols


class System(BaseModel):
    symbol: constr(min_length=1) = Field(..., description='The symbol of the system.')
    sectorSymbol: constr(min_length=1) = Field(
        ..., description='The symbol of the sector.'
    )
    type: SystemType
    x: int = Field(
        ..., description='Relative position of the system in the sector in the x axis.'
    )
    y: int = Field(
        ..., description='Relative position of the system in the sector in the y axis.'
    )
    waypoints: List[SystemWaypoint] = Field(
        ..., description='Waypoints in this system.'
    )
    factions: List[SystemFaction] = Field(
        ..., description='Factions that control this system.'
    )
