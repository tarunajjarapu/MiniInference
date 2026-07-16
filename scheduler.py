from re import L


class Scheduler:
    def __init__(self):
        self.free_blocks = None
        self.mapped_blocks = {}

    def add_new_request(self, request):
        self.mapped_blocks[request.id]


class BlockMetaData:
    def __init__(self, hash):
        self.hash = hash


# atomic uuid
class Request:
    def __init__(self, user, tokens):
        self.id = next_uid()
        self.user = user
        self.tokens = tokens
