class Review:
    def __init__(self, review_id, rating, comment, reviewer_id, reviewed_user_id):
        self.review_id = review_id
        self.rating = rating
        self.comment = comment
        self.reviewer_id = reviewer_id
        self.reviewed_user_id = reviewed_user_id
