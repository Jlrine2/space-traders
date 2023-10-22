from typing import Optional

from pydantic import BaseModel

from .base_api import BaseApi
from ..models.Agent import Agent
from ..models.Chart import Chart
from ..models.Cooldown import Cooldown
from ..models.Contract import Contract
from ..models.Ship import Ship
from ..models.ShipFuel import ShipFuel
from ..models.ShipCargo import ShipCargo
from ..models.ShipMount import ShipMount
from ..models.ShipNav import ShipNav
from ..models.MarketTransaction import MarketTransaction
from ..models.ShipyardShip import ShipyardShip
from ..models.ShipyardTransaction import ShipyardTransaction
from ..models.Survey import Survey
from ..models.System import System
from ..models.Waypoint import Waypoint
from ..models.Extraction import Extraction


class AgentShipTransaction(BaseModel):
    agent: Agent
    ship: Ship
    transaction: ShipyardTransaction


class TradeUnits(BaseModel):
    tradeSymbol: str
    units: int


class CargoCooldownProducedConsumed(BaseModel):
    cargo: ShipCargo
    cooldown: Cooldown
    produced: TradeUnits
    consumed: TradeUnits


class WaypointChart(BaseModel):
    chart: Chart
    waypoint: Waypoint


class CooldownSurvey(BaseModel):
    cooldown: Cooldown
    survey: Survey


class CooldownNav(BaseModel):
    cooldown: Cooldown
    nav: ShipNav


class CooldownExtraction(BaseModel):
    cooldown: Cooldown
    extraction: Extraction


class FuelNav(BaseModel):
    fuel: ShipFuel
    nav: ShipNav


class AgentCargoTransaction(BaseModel):
    agent: Agent
    cargo: ShipCargo
    transaction: MarketTransaction


class CooldownSystems(BaseModel):
    cooldown: Cooldown
    systems: list[System]


class CooldownWaypoints(BaseModel):
    cooldown: Cooldown
    waypoints: list[Waypoint]


class CooldownShips(BaseModel):
    cooldown: Cooldown
    waypoints: list[Ship]


class AgentFuelTransaction(BaseModel):
    agent: Agent
    fuel: ShipFuel
    transaction: MarketTransaction


class AgentMountsCargoTransaction(BaseModel):
    agent: Agent
    mounts: list[ShipMount]
    cargo: ShipCargo
    transaction: MarketTransaction


class FleetApi(BaseApi):
    def __init__(self, session, base_url, meta_callback) -> None:
        super().__init__(session, base_url, meta_callback=meta_callback)

    def list_ships(self, limit=10, page=1) -> list[Ship]:
        resp = self._get(f"my/ships", {"limit": limit, "page": page})
        return self._parse(resp, Ship)

    def purchase_ship(self, ship_type: str, waypoint: str) -> AgentShipTransaction:
        resp = self._post(
            f"my/ships/", {"shipType": ship_type, "waypointSymbol": waypoint}
        )
        return self._parse(resp, AgentShipTransaction)

    def get_ship(self, ship_symbol) -> Ship:
        resp = self._get(f"my/ships/{ship_symbol}")
        return self._parse(resp, Ship)

    def get_ship_cargo(self, ship_symbol: str) -> ShipCargo:
        resp = self._get(f"my/ships/{ship_symbol}/cargo")
        return self._parse(resp, ShipCargo)

    def orbit_ship(self, ship_symbol: str) -> ShipNav:
        resp = self._post(f"my/ships/{ship_symbol}/orbit")
        return self._parse(resp, ShipNav, nesting=["nav"])

    def ship_refine(
        self, ship_symbol: str, produce: str
    ) -> CargoCooldownProducedConsumed:
        resp = self._post(f"my/ships/{ship_symbol}/orbit", {"produce": produce})
        return self._parse(resp, CargoCooldownProducedConsumed)

    def create_chart(self, ship_symbol: str) -> WaypointChart:
        resp = self._post(f"my/ships/{ship_symbol}/chart")
        return self._parse(resp, WaypointChart)

    def get_ship_cooldown(self, ship_symbol: str) -> Cooldown:
        resp = self._get(f"my/ships/{ship_symbol}/cooldown")
        return self._parse(resp, Cooldown)

    def dock_ship(self, ship_symbol: str) -> ShipNav:
        resp = self._post(f"my/ships/{ship_symbol}/dock")
        return self._parse(resp, ShipNav, nesting=['nav'])

    def create_survey(self, ship_symbol: str) -> CooldownSurvey:
        resp = self._post(f"my/ships/{ship_symbol}/chart")
        return self._parse(resp, CooldownSurvey)

    def extract_resources(self, ship_symbol: str) -> CooldownExtraction:
        resp = self._post(
            f"my/ships/{ship_symbol}/extract"
        )
        return self._parse(resp, CooldownExtraction)

    def jettison_cargo(self, ship_symbol: str) -> ShipCargo:
        resp = self._post(f"my/ships/{ship_symbol}/jettison")
        return self._parse(resp, ShipCargo)

    def jump_ship(self, ship_symbol: str, system: str) -> CooldownNav:
        resp = self._post(f"my/ships/{ship_symbol}/jump", {"systemSymbol": system})
        return self._parse(resp, CooldownNav)

    def navigate_ship(self, ship_symbol: str, waypoint: str) -> FuelNav:
        resp = self._post(
            f"my/ships/{ship_symbol}/navigate", {"waypointSymbol": waypoint}
        )
        return self._parse(resp, FuelNav)

    def patch_ship_nav(self, ship_symbol: str, flight_mode: str) -> ShipNav:
        resp = self._patch(f"my/ships/{ship_symbol}/nav", {"flightMode": flight_mode})
        return self._parse(resp, ShipNav)

    def get_ship_nav(self, ship_symbol: str) -> ShipNav:
        resp = self._get(f"my/ships/{ship_symbol}/nav")
        return self._parse(resp, ShipNav)

    def warp_ship(self, ship_symbol: str, waypoint: str) -> FuelNav:
        resp = self._post(f"my/ships/{ship_symbol}/warp", {"waypointSymbol": waypoint})
        return self._parse(resp, FuelNav)

    def sell_cargo(
        self, ship_symbol: str, symbol: str, units: int
    ) -> AgentCargoTransaction:
        resp = self._post(
            f"my/ships/{ship_symbol}/sell", {"symbol": symbol, "units": units}
        )
        return self._parse(resp, AgentCargoTransaction)

    def scan_systems(self, ship_symbol: str) -> CooldownSystems:
        resp = self._post(f"my/ships/{ship_symbol}/scan/systems")
        return self._parse(resp, CooldownSystems)

    def scan_waypoints(self, ship_symbol: str) -> CooldownWaypoints:
        resp = self._post(f"my/ships/{ship_symbol}/scan/waypoints")
        return self._parse(resp, CooldownWaypoints)

    def scan_ships(self, ship_symbol: str) -> CooldownShips:
        resp = self._post(f"my/ships/{ship_symbol}/scan/ships")
        return self._parse(resp, CooldownShips)

    def refuel_ship(self, ship_symbol: str, units: int) -> AgentFuelTransaction:
        resp = self._post(f"my/ships/{ship_symbol}/refuel", {"units": units})
        return self._parse(resp, AgentFuelTransaction)

    def purchase_cargo(
        self, ship_symbol: str, symbol: str, units: int
    ) -> AgentCargoTransaction:
        resp = self._post(
            f"my/ships/{ship_symbol}/purchase", {"symbol": symbol, "units": units}
        )
        return self._parse(resp, AgentCargoTransaction)

    def transfer_cargo(
        self, ship_symbol: str, trade_symbol: str, dest_ship: str, units: int
    ) -> ShipCargo:
        resp = self._post(
            f"my/ships/{ship_symbol}/transfer",
            {"symbol": trade_symbol, "units": units, "shipSymbol": dest_ship},
        )
        return self._parse(resp, ShipCargo, nesting=["cargo"])

    def negotiate_contract(self, ship_symbol: str) -> Contract:
        resp = self._post(f"my/ships/{ship_symbol}/negotiate/contract")
        return self._parse(resp, Contract, nesting=["contract"])

    def get_mounts(self, ship_symbol: str) -> ShipMount:
        resp = self._get(f"my/ships/{ship_symbol}/mounts")
        return self._parse(resp, ShipMount)

    def install_mount(
        self, ship_symbol: str, mount: str
    ) -> AgentMountsCargoTransaction:
        resp = self._post(f"my/ships/{ship_symbol}/mounts/install", {"symbol": mount})
        return self._parse(resp, AgentMountsCargoTransaction)

    def remove_mount(self, ship_symbol: str, mount: str) -> AgentMountsCargoTransaction:
        resp = self._post(f"my/ships/{ship_symbol}/mounts/remove", {"symbol": mount})
        return self._parse(resp, AgentMountsCargoTransaction)
