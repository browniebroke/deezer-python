# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import unittest

import requests_mock


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.requests_mocker = requests_mock.mock()
        self.requests_mocker.start()

    def tearDown(self):
        self.requests_mocker.stop()
