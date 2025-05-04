from models import Contract
from typing import List

class ContractService:
    def __init__(self):
        self.contracts = []  # Temporary in-memory store

    def create_contract(self, contract: Contract) -> Contract:
        self.contracts.append(contract)
        return contract

    def get_contracts(self) -> List[Contract]:
        return self.contracts

    def get_contract_by_id(self, contract_id: int) -> Contract | None:
        for c in self.contracts:
            if c.id == contract_id:
                return c
        return None
