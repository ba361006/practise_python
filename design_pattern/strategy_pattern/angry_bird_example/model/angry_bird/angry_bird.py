# -*- coding: utf-8 -*-
import abc


class AngryBird(abc.ABC):
    def __init__(self, fly_behaviour, tweet_behaviour):
        self.__fly_behaviour = fly_behaviour
        self.__tweet_behaviour = tweet_behaviour

    @abc.abstractmethod
    def description(self):
        pass

    def fly(self):
        self.__fly_behaviour.fly()

    def tweet(self):
        self.__tweet_behaviour.tweet()
