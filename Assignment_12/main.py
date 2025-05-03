from fastapi import FastAPI
from services import jobpost_routes, proposal_routes

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Include your routers
app.include_router(jobpost_routes.router, prefix="/jobs", tags=["Job Posts"])
app.include_router(proposal_routes.router, prefix="/proposals", tags=["Proposals"])
