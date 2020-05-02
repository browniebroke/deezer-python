import vcr_unittest

import deezer


class BaseTestCaseWithVcr(vcr_unittest.VCRTestCase):
    def setUp(self):
        super().setUp()
        self.client = deezer.Client(app_id="foo", app_secret="bar")  # nosec
        self.unsec_client = deezer.Client(use_ssl=False)
        self.client_fr = deezer.Client(headers={"Accept-Language": "fr"})  # French
        self.client_ja = deezer.Client(headers={"Accept-Language": "ja"})  # Japanese
