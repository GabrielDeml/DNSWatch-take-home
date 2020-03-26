#!/usr/bin/env python
import requests


class DomainFeedChecker:
    # Init vars
    # _domain_feed is a set of the latest parsed data from the domain feed url
    _domain_feed = None

    def __init__(self, url):
        """INITs the class"""
        self.load_domain_feed(url)

    def load_domain_feed(self, url):
        """Reassigns _domain_feed to the parsed data from a domain feed url"""
        # Do a get request to get the data from the domain feed
        domain_feed = requests.get(url)
        # Convert the content into a list
        domain_feed_content = str(domain_feed.content).split('\\n')
        # Convert to set and reassign _domain_feed
        self._domain_feed = set(domain_feed_content)

    def is_domain_in_domain_feed(self, target):
        """"Checks if target is in _domain_feed"""
        return target in self._domain_feed


if __name__ == "__main__":
    # Load the domain feed
    _domain_feed = DomainFeedChecker("http://mirror1.malwaredomains.com/files/justdomains")
    # User Interface
    print("Enter domain to check against the domain feed. \n q to quit \n l:<url> to load a new domain feed")
    while True:
        # Get user input
        usr_input = input('== ')
        # Act upon user input
        if usr_input == 'q':
            print("exiting")
            exit(0)
        elif usr_input == '':
            print("Enter domain to check against the domain feed. \n q to quit \n l:<url> to load a new domain feed")
        elif usr_input[:2] == "l:":
            print("loading data from: " + usr_input[2:])
            _domain_feed.load_domain_feed(usr_input[2:])
            print("New data loaded")
        elif _domain_feed.is_domain_in_domain_feed(usr_input):
            print("Domain is in the domain feed")
        else:
            print("Domain is not in domain feed")
