from fastapi import APIRouter, HTTPException
from models import Contract
from services.contract_service import ContractService

router = APIRouter()
contract_service = ContractService()

@router.post("/", response_model=Contract)
def create_contract(contract: Contract):
    return contract_service.create_contract(contract)

@router.get("/", response_model=list[Contract])
def read_contracts():
    return contract_service.get_contracts()

@router.get("/{contract_id}", response_model=Contract)
def read_contract(contract_id: int):
    contract = contract_service.get_contract_by_id(contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract
