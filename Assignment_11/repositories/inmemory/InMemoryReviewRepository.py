from Assignment_11.repositories.ReviewRepository import ReviewRepository
from Assignment_10.src.Review import Review

class InMemoryReviewRepository(ReviewRepository):
    def __init__(self):
        self._storage = {}

    def save(self, review: Review) -> None:
        self._storage[review.review_id] = review

    def find_by_id(self, review_id: str) -> Review:
        return self._storage.get(review_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, review_id: str) -> None:
        if review_id in self._storage:
            del self._storage[review_id]
