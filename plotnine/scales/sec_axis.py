class secondary_axis:
    """
    Secondary axis representing a transformed view of the primary y-scale.
    """
    def __init__(self, trans, name=None, breaks=None, labels=None):
        self.trans = trans
        self.name = name
        self.breaks = breaks
        self.labels = labels

    def transform(self, values):
        return [self.trans(v) for v in values]
