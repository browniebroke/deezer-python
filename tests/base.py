import vcr_unittest

import deezer


class BaseTestCaseWithVcr(vcr_unittest.VCRTestCase):
    def setUp(self):
        super().setUp()
        self.client = deezer.Client(  # nosec
            app_id="foo", app_secret="bar", do_not_compress_reponse=True
        )
        self.unsec_client = deezer.Client(use_ssl=False, do_not_compress_reponse=True)
        self.client_fr = deezer.Client(headers={"Accept-Language": "fr"})  # French
        self.client_ja = deezer.Client(headers={"Accept-Language": "ja"})  # Japanese
