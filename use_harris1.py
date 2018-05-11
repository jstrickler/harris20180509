#!/usr/bin/env python
import sys

from harris.misc import harrisutil

harrisutil.spam()
harrisutil.ham()

print(harrisutil.A)

for path in sys.path:
    print(path)
