# Assignment_12/services/jobpost_routes.py

from fastapi import APIRouter, HTTPException
from typing import List
from .JobPostService import JobPostService, JobPost

router = APIRouter(prefix="/jobs", tags=["Job Posts"])

@router.post("/", response_model=JobPost)
def create_job(job: JobPost):
    return JobPostService.create_job_post(job.dict())

@router.get("/", response_model=List[JobPost])
def get_all_jobs():
    return JobPostService.get_all_jobs()

@router.get("/{job_id}", response_model=JobPost)
def get_job(job_id: str):
    job = JobPostService.get_job_by_id(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
