# DNSWatch-take-home

To run:
1) pip install -r requirements.txt
2) python3 DNSWatch-take-home.py

# How it works:
There are two main functions load_domain_feed and is_domain_in_domain_feed. 

## load_domain_feed
When load_domain_feed is called with a URL. It does an HTTP request to the URL to get the data. Then it splits the data into a list. That list is then converted to a HashSet and assigned to the global var _domain_feed.

## is_domain_in_domain_feed
This simply checks if the target is in the HashSet and returns a boolean.

## Reason for decisions made:
Class: I made it its own class because it was supposed to be its own module and that made me comfortable using _domain_feed as global.
HashSet: Checking if the set contains a domain is O(1) assuming we don't have any collisions.
