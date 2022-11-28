# -*- coding: utf-8 -*-
from . import tweet_interface


class tweetTwice(tweet_interface.ITweet):
    def tweet(self):
        print("tweet Twice")


class muteTweet(tweet_interface.ITweet):
    def tweet(self):
        print("I don't tweet")
