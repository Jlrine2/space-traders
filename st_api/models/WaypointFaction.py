# generated by datamodel-codegen:
#   filename:  api-docs/models/WaypointFaction.json
#   timestamp: 2023-10-21T17:38:30+00:00

from __future__ import annotations

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Literal


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


class WaypointFaction(BaseModel):
    symbol: FactionSymbols
