from pydantic import BaseModel

from .base_api import BaseApi, Collection
from ..models.Agent import Agent
from ..models.Contract import Contract
from ..models.Ship import Ship
from ..models.ShipCargo import ShipCargo
from ..models.TradeGood import TradeGood


class ContractAcceptFulfill(BaseModel):
    agent: Agent
    contract: Contract


class ContractDeliver(BaseModel):
    cargo: ShipCargo
    contract: Contract


class ContractsApi(BaseApi):
    def __init__(self, session, base_url, meta_callback) -> None:
        super().__init__(session, base_url, meta_callback=meta_callback)

    def list_contracts(self, limit=10, page=1) -> Collection[Contract]:
        resp = self._get(f"my/contracts", {"limit": limit, "page": page})
        return self._parse(resp, Contract)

    def get_contract(self, contract_id: str) -> Contract:
        resp = self._get(f"my/contracts/{contract_id}")
        return self._parse(resp, Contract)

    def accept_contract(self, contract_id: str) -> ContractAcceptFulfill:
        resp = self._post(f"my/contracts/{contract_id}/accept")
        return self._parse(resp, ContractAcceptFulfill)

    def deliver_cargo_to_contract(
        self, contract: Contract, ship_symbol: str, trade_good: TradeGood, units: int
    ) -> ContractDeliver:
        resp = self._post(
            f"my/contracts/{contract.id}/deliver",
            {
                "shipSymbol": ship_symbol,
                "tradeSymbol": trade_good.symbol,
                "units": units,
            },
        )
        return self._parse(resp, ContractDeliver)

    def fulfil_contract(self, contract_id: str) -> ContractAcceptFulfill:
        resp = self._post(f"my/contracts/{contract_id}/fulfill")
        return self._parse(resp, ContractAcceptFulfill)
