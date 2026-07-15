class Scheduler:
    def __init__(self):
        self.free_blocks = None
        self.mapped_blocks = {}


class BlockMetaData:
    def __init__(self, hash):
        self.hash = hash
