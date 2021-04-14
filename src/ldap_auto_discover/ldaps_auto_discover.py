from collections import defaultdict
from datetime import datetime, timedelta
import random
import sys

import dns.resolver
from . import ldap_auto_discover

discoverer = None
def ldaps_auto_discover(domain):
    """
    Returns a space-separated list of LDAPS servers for this domain.

    This uses SRV records to discover local LDAP servers and returns them in
    a prioritized, space-separated list for python-ldap's initialize function.
    """
    global discoverer
    if discoverer is None:
        discoverer = ldap_auto_discover.ServerDiscoverer("ldap", "tcp", domain)
    hosts = discoverer.hosts()

    return ' '.join('ldaps://{}:{}'.format(target, "636")
                    for target, port in hosts)

