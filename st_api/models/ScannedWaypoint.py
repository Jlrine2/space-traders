# generated by datamodel-codegen:
#   filename:  api-docs/models/ScannedWaypoint.json
#   timestamp: 2023-10-15T19:00:16+00:00

from __future__ import annotations

from datetime import datetime
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


class FactionSymbols(Enum):
    COSMIC = "COSMIC"
    VOID = "VOID"
    GALACTIC = "GALACTIC"
    QUANTUM = "QUANTUM"
    DOMINION = "DOMINION"
    ASTRO = "ASTRO"
    CORSAIRS = "CORSAIRS"
    OBSIDIAN = "OBSIDIAN"
    AEGIS = "AEGIS"
    UNITED = "UNITED"
    SOLITARY = "SOLITARY"
    COBALT = "COBALT"
    OMEGA = "OMEGA"
    ECHO = "ECHO"
    LORDS = "LORDS"
    CULT = "CULT"
    ANCIENTS = "ANCIENTS"
    SHADOW = "SHADOW"
    ETHEREAL = "ETHEREAL"


class Symbol(Enum):
    UNCHARTED = "UNCHARTED"
    MARKETPLACE = "MARKETPLACE"
    SHIPYARD = "SHIPYARD"
    OUTPOST = "OUTPOST"
    SCATTERED_SETTLEMENTS = "SCATTERED_SETTLEMENTS"
    SPRAWLING_CITIES = "SPRAWLING_CITIES"
    MEGA_STRUCTURES = "MEGA_STRUCTURES"
    OVERCROWDED = "OVERCROWDED"
    HIGH_TECH = "HIGH_TECH"
    CORRUPT = "CORRUPT"
    BUREAUCRATIC = "BUREAUCRATIC"
    TRADING_HUB = "TRADING_HUB"
    INDUSTRIAL = "INDUSTRIAL"
    BLACK_MARKET = "BLACK_MARKET"
    RESEARCH_FACILITY = "RESEARCH_FACILITY"
    MILITARY_BASE = "MILITARY_BASE"
    SURVEILLANCE_OUTPOST = "SURVEILLANCE_OUTPOST"
    EXPLORATION_OUTPOST = "EXPLORATION_OUTPOST"
    MINERAL_DEPOSITS = "MINERAL_DEPOSITS"
    COMMON_METAL_DEPOSITS = "COMMON_METAL_DEPOSITS"
    PRECIOUS_METAL_DEPOSITS = "PRECIOUS_METAL_DEPOSITS"
    RARE_METAL_DEPOSITS = "RARE_METAL_DEPOSITS"
    METHANE_POOLS = "METHANE_POOLS"
    ICE_CRYSTALS = "ICE_CRYSTALS"
    EXPLOSIVE_GASES = "EXPLOSIVE_GASES"
    STRONG_MAGNETOSPHERE = "STRONG_MAGNETOSPHERE"
    VIBRANT_AURORAS = "VIBRANT_AURORAS"
    SALT_FLATS = "SALT_FLATS"
    CANYONS = "CANYONS"
    PERPETUAL_DAYLIGHT = "PERPETUAL_DAYLIGHT"
    PERPETUAL_OVERCAST = "PERPETUAL_OVERCAST"
    DRY_SEABEDS = "DRY_SEABEDS"
    MAGMA_SEAS = "MAGMA_SEAS"
    SUPERVOLCANOES = "SUPERVOLCANOES"
    ASH_CLOUDS = "ASH_CLOUDS"
    VAST_RUINS = "VAST_RUINS"
    MUTATED_FLORA = "MUTATED_FLORA"
    TERRAFORMED = "TERRAFORMED"
    EXTREME_TEMPERATURES = "EXTREME_TEMPERATURES"
    EXTREME_PRESSURE = "EXTREME_PRESSURE"
    DIVERSE_LIFE = "DIVERSE_LIFE"
    SCARCE_LIFE = "SCARCE_LIFE"
    FOSSILS = "FOSSILS"
    WEAK_GRAVITY = "WEAK_GRAVITY"
    STRONG_GRAVITY = "STRONG_GRAVITY"
    CRUSHING_GRAVITY = "CRUSHING_GRAVITY"
    TOXIC_ATMOSPHERE = "TOXIC_ATMOSPHERE"
    CORROSIVE_ATMOSPHERE = "CORROSIVE_ATMOSPHERE"
    BREATHABLE_ATMOSPHERE = "BREATHABLE_ATMOSPHERE"
    JOVIAN = "JOVIAN"
    ROCKY = "ROCKY"
    VOLCANIC = "VOLCANIC"
    FROZEN = "FROZEN"
    SWAMP = "SWAMP"
    BARREN = "BARREN"
    TEMPERATE = "TEMPERATE"
    JUNGLE = "JUNGLE"
    OCEAN = "OCEAN"
    STRIPPED = "STRIPPED"


class WaypointTrait(BaseModel):
    symbol: Symbol = Field(..., description="The unique identifier of the trait.")
    name: str = Field(..., description="The name of the trait.")
    description: str = Field(..., description="A description of the trait.")


class Chart(BaseModel):
    waypointSymbol: Optional[str] = Field(
        None, description="The symbol of the waypoint."
    )
    submittedBy: Optional[str] = Field(
        None, description="The agent that submitted the chart for this waypoint."
    )
    submittedOn: Optional[datetime] = Field(
        None, description="The time the chart for this waypoint was submitted."
    )


class WaypointFaction(BaseModel):
    symbol: FactionSymbols


class ScannedWaypoint(BaseModel):
    symbol: constr(min_length=1) = Field(..., description="Symbol of the waypoint.")
    type: WaypointType
    systemSymbol: constr(min_length=1) = Field(..., description="Symbol of the system.")
    x: int = Field(..., description="Position in the universe in the x axis.")
    y: int = Field(..., description="Position in the universe in the y axis.")
    orbitals: List[WaypointOrbital] = Field(
        ..., description="List of waypoints that orbit this waypoint."
    )
    faction: Optional[WaypointFaction] = None
    traits: List[WaypointTrait] = Field(..., description="The traits of the waypoint.")
    chart: Optional[Chart] = None
