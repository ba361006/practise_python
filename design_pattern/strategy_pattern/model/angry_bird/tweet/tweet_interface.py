import abc

class ITweet(abc.ABC):
    @abc.abstractmethod
    def tweet(self):
        pass