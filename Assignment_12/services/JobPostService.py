# Assignment_12/services/JobPostService.py

from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

# A sample model for a job post
class JobPost(BaseModel):
    id: str
    title: str
    description: str
    client_id: str
    budget: float

# Simulated in-memory store
job_posts: List[JobPost] = []

class JobPostService:
    @staticmethod
    def create_job_post(data: dict) -> JobPost:
        job = JobPost(id=str(uuid4()), **data)
        job_posts.append(job)
        return job

    @staticmethod
    def get_all_jobs() -> List[JobPost]:
        return job_posts

    @staticmethod
    def get_job_by_id(job_id: str) -> Optional[JobPost]:
        return next((job for job in job_posts if job.id == job_id), None)
