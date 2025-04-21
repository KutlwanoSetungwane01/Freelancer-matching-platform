class Message:
    def __init__(self, message_id, sender_id, receiver_id, content, timestamp):
        self.message_id = message_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = timestamp
