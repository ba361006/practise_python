# -*- coding: utf-8 -*-
import abc


class ITweet(abc.ABC):
    @abc.abstractmethod
    def tweet(self):
        pass
