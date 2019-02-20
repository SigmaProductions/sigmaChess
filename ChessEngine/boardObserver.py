
class Observer:
    def __init__(self):
        self.callbacks=[]

    def Bind(self, callback):
        self.callbacks.append(callback)

    def RaisePropertyChanged(self):
        for callback in self.callbacks:
            callback()