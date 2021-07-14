from exchangelib import Account

class Listener:
    def __init__(self, account: Account):
        self._account = account
        self.streaming_events_received = self.__EventHandler()
    
    def __get_streaming_events(self, subscription_id: str):
        for notification in self._account.inbox.get_streaming_events(subscription_id):
            self.streaming_events_received(notification.events)
            if self.canceled:
                break

    def listen(self):
        self.canceled = False
        with self._account.inbox.streaming_subscription() as subscription_id:
            while not self.canceled:
                self.__get_streaming_events(subscription_id)
    
    def cancel(self):
        self.canceled = True
    
    
    class __EventHandler:
        def __init__(self):
            self._functions = []

        def __iadd__(self, func):
            self._functions.append(func)
            return self

        def __isub__(self, func):
            self._functions.remove(func)
            return self

        def __call__(self, *args, **kvargs):
            for func in self._functions:
                func(*args, **kvargs)