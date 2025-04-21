class Payment:
    def __init__(self, payment_id, amount, date, status):
        self.payment_id = payment_id
        self.amount = amount
        self.date = date
        self.status = status  # "pending", "completed", "failed"
