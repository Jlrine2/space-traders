from requests import Session
from requests_ratelimiter import LimiterSession


def _default_callback(meta):
    pass


def _get_session() -> Session:
    s = LimiterSession(per_second=2)
    return s


class Client:
    def __init__(
        self,
        token,
        session: Session = _get_session(),
        base_url="https://api.spacetraders.io/v2",
    ):
        self.token = token
        self.session = session
        self.base_url = base_url
        self.session.headers.update({"Authorization": f"Bearer {token}"})

        from .api import agents, contracts, factions, fleet, systems

        self.meta_callback = _default_callback
        self.agents: agents.AgentApi = self._register_api(agents.AgentApi)
        self.contracts: contracts.ContractsApi = self._register_api(
            contracts.ContractsApi
        )
        self.factions: factions.FactionsApi = self._register_api(factions.FactionsApi)
        self.fleet: fleet.FleetApi = self._register_api(fleet.FleetApi)
        self.systems: systems.SystemsApi = self._register_api(systems.SystemsApi)

    def _register_api(self, api):
        return api(self.session, self.base_url, self.meta_callback)

    def status(self):
        resp = self.session.get(f"{self.base_url}/")
        resp.raise_for_status()
        return resp.json()

    @classmethod
    def new(cls, faction, symbol):
        s = _get_session()
        resp = s.post(
            "https://api.spacetraders.io/v2/register",
            json={"faction": str(faction), "symbol": symbol},
        )
        resp.raise_for_status()
        return Client(resp.json()["data"]["token"], s)
