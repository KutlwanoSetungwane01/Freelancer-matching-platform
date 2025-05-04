from Assignment_11.repositories.inmemory.InMemoryProposalRepository import InMemoryProposalRepository
from Assignment_10.src.Proposal import Proposal
from typing import List

class ProposalService:
    def __init__(self, repository: InMemoryProposalRepository):
        self.repository = repository

    def create_proposal(self, proposal: Proposal) -> Proposal:
        # Business logic: Ensure the proposal has a description
        if not proposal.description:
            raise ValueError("Proposal must have a description")
        return self.repository.save(proposal)

    def get_all_proposals(self) -> List[Proposal]:
        return self.repository.find_all()

    def get_proposal_by_id(self, proposal_id: str) -> Proposal:
        proposal = self.repository.find_by_id(proposal_id)
        if not proposal:
            raise ValueError(f"No proposal found with ID {proposal_id}")
        return proposal

    def update_proposal(self, proposal_id: str, updated: Proposal) -> Proposal:
        existing = self.repository.find_by_id(proposal_id)
        if not existing:
            raise ValueError(f"Proposal not found: {proposal_id}")
        return self.repository.save(updated)

    def delete_proposal(self, proposal_id: str) -> None:
        self.repository.delete_by_id(proposal_id)
