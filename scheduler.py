class Scheduler:
    def __init__(self):
        self.mapped_blocks = {}
        self.free_blocks = BlockNode(None)
        self.free_block_lengh = 0

    def add_new_request(self, request):
        self.mapped_blocks[request.id] = request

    def get_next_block(self):
        if self.free_block_length > 0:
            take = self.free_blocks.next
            self.free_blocks.next = self.free_blocks.next.next
            take.next = None
            return take
        return None


class BlockNode:
    def __init__(self, next):
        self.next = next


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
