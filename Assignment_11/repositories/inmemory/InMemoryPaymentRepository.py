from Assignment_11.repositories.PaymentRepository import PaymentRepository
from Assignment_10.src.Payment import Payment

class InMemoryPaymentRepository(PaymentRepository):
    def __init__(self):
        self._storage = {}

    def save(self, payment: Payment) -> None:
        self._storage[payment.payment_id] = payment

    def find_by_id(self, payment_id: str) -> Payment:
        return self._storage.get(payment_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, payment_id: str) -> None:
        if payment_id in self._storage:
            del self._storage[payment_id]
