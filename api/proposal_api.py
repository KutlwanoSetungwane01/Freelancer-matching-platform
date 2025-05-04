from fastapi import APIRouter, HTTPException
from Assignment_10.src.Proposal import Proposal
from Assignment_12.services.ProposalService import ProposalService
from Assignment_11.repositories.inmemory.InMemoryProposalRepository import InMemoryProposalRepository

router = APIRouter(prefix="/api/proposals", tags=["Proposals"])
proposal_service = ProposalService(InMemoryProposalRepository())

@router.post("/", response_model=Proposal)
def create_proposal(proposal: Proposal):
    try:
        return proposal_service.create_proposal(proposal)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[Proposal])
def get_all():
    return proposal_service.get_all_proposals()

@router.get("/{proposal_id}", response_model=Proposal)
def get_by_id(proposal_id: str):
    try:
        return proposal_service.get_proposal_by_id(proposal_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{proposal_id}", response_model=Proposal)
def update(proposal_id: str, proposal: Proposal):
    try:
        return proposal_service.update_proposal(proposal_id, proposal)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{proposal_id}")
def delete(proposal_id: str):
    proposal_service.delete_proposal(proposal_id)
    return {"detail": f"Proposal {proposal_id} deleted"}
