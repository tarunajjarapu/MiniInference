class Scheduler:
    def __init__(self, model):
        self.mapped_blocks = {}
        self.free_blocks = BlockNode(None)
        self.free_block_length = 0
        self.model = model

    def add_new_request(self, request):
        self.mapped_blocks[request.id] = request

    def get_next_block(self):
        if self.free_block_length > 0:
            take = self.free_blocks.next
            if self.free_blocks.next is not None:
                self.free_blocks.next = self.free_blocks.next.next
            take.next = None
            self.free_block_length -= 1
            return take
        return None


class BlockNode:
    def __init__(self, next, data=None):
        self.next = next
        self.metaData = data


class BlockMetaData:
    def __init__(self, hash):
        self.hash = hash


class Router:
    def __init__(self, priorerty=1):
        self.priorerty = priorerty
        self.requests = []

    def schedule(self, request):
        self.requests.append(request)
        print(request.id)

    def run_scheduler(self):
        run_tasks = Scheduler()
        for request in self.requests:
            run_tasks.add_new_request(request)


class Request:
    _uuid = 0

    def __init__(self, user, tokens):
        self.id = self.next_uid()
        self.user = user
        self.tokens = tokens

    @classmethod
    def next_uid(cls):
        cur = cls._uuid
        cls._uuid += 1
        return cur
