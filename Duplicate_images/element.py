class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None