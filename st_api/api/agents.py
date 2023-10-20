from .base_api import BaseApi, Collection
from ..models.Agent import Agent


class AgentApi(BaseApi):
    def __init__(self, session, base_url, meta_callback) -> None:
        super().__init__(session, base_url, meta_callback=meta_callback)

    def get_agent(self) -> Agent:
        resp = self._get("my/agent")
        return self._parse(resp, Agent)

    def list_agents(self, limit=10, page=1) -> Collection[Agent]:
        resp = self._get(f"agents", {"limit": limit, "page": page})
        return self._parse(resp, Agent)

    def get_public_agent(self, symbol) -> Agent:
        resp = self._get(f"agents/{symbol}")
        return self._parse(resp, Agent)
