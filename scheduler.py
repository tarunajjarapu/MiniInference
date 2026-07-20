class Scheduler:
    def __init__(self):
        self.free_blocks = None
        self.mapped_blocks = {}

    def add_new_request(self, request):
        self.mapped_blocks[request.id]


class BlockMetaData:
    def __init__(self, hash):
        self.hash = hash


class Router:
    def __init__(self, priorerty=1):
        self.priorerty = priorerty
        self.requests = []

    def schedule(self, request):
        self.requests.append(request)


# atomic uuid
class Request:
    def __init__(self, user, tokens):
        self.id = next_uid()
        self.user = user
        self.tokens = tokens
