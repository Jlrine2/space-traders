from .base_api import BaseApi, Collection
from ..models.Faction import Faction


class FactionsApi(BaseApi):
    def __init__(self, session, base_url, meta_callback) -> None:
        super().__init__(session, base_url, meta_callback=meta_callback)

    def list_factions(self, limit=10, page=1) -> Collection[Faction]:
        resp = self._get(f"factions", {"limit": limit, "page": page})
        return self._parse(resp, Faction)

    def get_faction(self, symbol) -> Faction:
        resp = self._get(f"factions/{symbol}")
        return self._parse(resp, Faction)
