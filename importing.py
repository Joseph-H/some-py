# always import a module on a line
import os
import sys

# but you can do this
from os import path, walk, unlink

# you can do this
from os import (path, walk, unlink, uname,
                remove, rename)

# or this
from os import path, walk, unlink, uname, \
    remove, rename

# you can do optional imports
try:
    from urlparse import urljoin  # NOQA
    from urllib2 import urlopen  # NOQA
except ImportError:
    # Python 3
    from urllib.parse import urljoin
    from urllib.request import urlopen
