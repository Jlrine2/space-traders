from pydantic import BaseModel

from .base_api import BaseApi
from ..models.System import System
from ..models.JumpGate import JumpGate
from ..models.Market import Market
from ..models.Shipyard import Shipyard
from ..models.Waypoint import Waypoint


class SystemsApi(BaseApi):
    def __init__(self, session, base_url, meta_callback) -> None:
        super().__init__(session, base_url, meta_callback=meta_callback)

    def list_systems(self, limit=10, page=1) -> list[System]:
        resp = self._get(f"systems", {"limit": limit, "page": page})
        return self._parse(resp, System)

    def get_system(self, symbol) -> System:
        resp = self._get(f"systems/{symbol}")
        return self._parse(resp, System)

    def list_waypoints_in_system(self, symbol, limit=10, page=1) -> list[Waypoint]:
        resp = self._get(f"systems/{symbol}/waypoints", {"limit": limit, "page": page})
        return self._parse(resp, Waypoint)

    def get_waypoint(self, symbol) -> Waypoint:
        resp = self._get(f"systems/{symbol}/waypoints/{symbol}")
        return self._parse(resp, Waypoint)

    def get_market(self, system, waypoint) -> Market:
        resp = self._get(f"systems/{system}/waypoints/{waypoint}/market")
        return self._parse(resp, Market)

    def get_shipyard(self, system, waypoint) -> Shipyard:
        resp = self._get(f"systems/{system}/waypoints/{waypoint}/shipyard")
        return self._parse(resp, Shipyard)

    def get_jump_gate(self, system, waypoint) -> JumpGate:
        resp = self._get(f"systems/{system}/waypoints/{waypoint}/jump-gate")
        return self._parse(resp, JumpGate)
