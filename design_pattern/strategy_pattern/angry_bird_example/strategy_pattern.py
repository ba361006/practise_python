# -*- coding: utf-8 -*-
from model.angry_bird import AngryBird
from model.angry_bird import fly
from model.angry_bird import tweet


class Red(AngryBird):
    def __init__(self):
        super().__init__(fly.FastFly(), tweet.tweetTwice())

    def description(self):
        print("this is red")


class Yellow(AngryBird):
    def __init__(self):
        super().__init__(fly.SlowFly(), tweet.muteTweet())

    def description(self):
        return print("this is Yellow")


red = Red()
red.description()
red.tweet()
red.fly()

print()

yellow = Yellow()
yellow.description()
yellow.tweet()
yellow.fly()
