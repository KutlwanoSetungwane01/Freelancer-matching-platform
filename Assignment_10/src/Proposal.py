class Proposal:
    def __init__(self, proposal_id, cover_letter, bid_amount, status):
        self.proposal_id = proposal_id
        self.cover_letter = cover_letter
        self.bid_amount = bid_amount
        self.status = status  # "pending", "accepted", "rejected"
