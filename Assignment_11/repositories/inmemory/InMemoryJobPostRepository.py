from Assignment_11.repositories.JobPostRepository import JobPostRepository
from Assignment_10.src.JobPost import JobPost

class InMemoryJobPostRepository(JobPostRepository):
    def __init__(self):
        self._storage = {}

    def save(self, job: JobPost) -> None:
        self._storage[job.job_id] = job

    def find_by_id(self, job_id: str) -> JobPost:
        return self._storage.get(job_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, job_id: str) -> None:
        if job_id in self._storage:
            del self._storage[job_id]
