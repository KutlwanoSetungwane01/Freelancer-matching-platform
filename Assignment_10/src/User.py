class User:
    def __init__(self, user_id, name, email, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role  # "freelancer" or "employer"

    def __str__(self):
        return f"{self.name} ({self.role})"



