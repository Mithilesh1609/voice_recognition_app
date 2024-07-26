import uuid

class audioNotFoundError(Exception):
    def __init__(self, message="target not found."):
        self.errorId = str(uuid.uuid4())
        self.message = message
        super().__init__(self.message)