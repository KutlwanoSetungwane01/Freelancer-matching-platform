class JobPost:
    def __init__(self, job_id, title, description, skills_required, status):
        self.job_id = job_id
        self.title = title
        self.description = description
        self.skills_required = skills_required
        self.status = status  # "open", "in progress", "closed"
