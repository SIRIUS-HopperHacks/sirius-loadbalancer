class Item:
    def __init__(self, value: object):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        try:
            return self.value.__dict__ == other.value.__dict__
        except AttributeError:
            return self.value == other.value
