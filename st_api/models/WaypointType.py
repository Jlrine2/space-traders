# generated by datamodel-codegen:
#   filename:  api-docs/models/WaypointType.json
#   timestamp: 2023-10-21T17:38:30+00:00

from __future__ import annotations

from pydantic import Field, RootModel
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
