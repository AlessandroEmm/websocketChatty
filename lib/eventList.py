class eventList(list):
    def __init__(self):
        super().__init__()
        self.appendEventListeners = []

    def eAppend(self, item):
        self.append(item)
        self.execute(appendEventListeners)

    def addEventListener(self, callback):
        self.appendEventListeners.append(callback)

    def delEventListener(self, callback):
        for callbacks, index in self.appendEventListeners:
            if callbacks ==  callback:
                pass

    def execute(self, eventList):
        for callback in eventList:
            callback()