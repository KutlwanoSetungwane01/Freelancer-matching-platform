from Assignment_11.repositories.inmemory.InMemoryUserRepository import InMemoryUserRepository
from Assignment_11.repositories.inmemory.InMemoryJobPostRepository import InMemoryJobPostRepository
from Assignment_11.repositories.inmemory.InMemoryProposalRepository import InMemoryProposalRepository
# (Import more in-memory repositories as needed)

class RepositoryFactory:
    @staticmethod
    def get_user_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryUserRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_jobpost_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryJobPostRepository()
        else:
            raise ValueError("Unsupported storage type")

    @staticmethod
    def get_proposal_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryProposalRepository()
        else:
            raise ValueError("Unsupported storage type")
