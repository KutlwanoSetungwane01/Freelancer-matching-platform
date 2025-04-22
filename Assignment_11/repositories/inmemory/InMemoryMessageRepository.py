from Assignment_11.repositories.MessageRepository import MessageRepository
from Assignment_10.src.Message import Message

class InMemoryMessageRepository(MessageRepository):
    def __init__(self):
        self._storage = {}

    def save(self, message: Message) -> None:
        self._storage[message.message_id] = message

    def find_by_id(self, message_id: str) -> Message:
        return self._storage.get(message_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, message_id: str) -> None:
        if message_id in self._storage:
            del self._storage[message_id]
