from fastapi import FastAPI
from services import jobpost_routes, proposal_routes

app = FastAPI(title="Freelancer Job Matching Platform API")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Register routers
app.include_router(jobpost_routes.router, prefix="/jobs", tags=["Job Posts"])
app.include_router(proposal_routes.router, prefix="/proposals", tags=["Proposals"])
