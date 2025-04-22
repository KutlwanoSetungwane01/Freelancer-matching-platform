from Assignment_11.repositories.ContractRepository import ContractRepository
from Assignment_10.src.Contract import Contract

class InMemoryContractRepository(ContractRepository):
    def __init__(self):
        self._storage = {}

    def save(self, contract: Contract) -> None:
        self._storage[contract.contract_id] = contract

    def find_by_id(self, contract_id: str) -> Contract:
        return self._storage.get(contract_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, contract_id: str) -> None:
        if contract_id in self._storage:
            del self._storage[contract_id]
