# This is a placeholder for future database implementation

from Assignment_11.repositories.UserRepository import UserRepository
from Assignment_10.src.User import User

class DatabaseUserRepository(UserRepository):
    def save(self, user: User) -> None:
        raise NotImplementedError("Database saving not implemented yet")

    def find_by_id(self, user_id: str) -> User:
        raise NotImplementedError("Database retrieval not implemented yet")

    def find_all(self):
        raise NotImplementedError("Database retrieval not implemented yet")

    def delete(self, user_id: str) -> None:
        raise NotImplementedError("Database deletion not implemented yet")
