# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import deezer
import vcr_unittest


class BaseTestCaseWithVcr(vcr_unittest.VCRTestCase):
    def setUp(self):
        super(BaseTestCaseWithVcr, self).setUp()
        self.client = deezer.Client(
            app_id="foo", app_secret="bar", do_not_compress_reponse=True
        )
        self.unsec_client = deezer.Client(use_ssl=False, do_not_compress_reponse=True)
