# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import sys
import unittest

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        argv.append('discover')
    unittest.main(argv=argv)
