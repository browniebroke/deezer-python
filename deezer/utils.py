"""Utils."""

from collections import OrderedDict


class SortedDict(OrderedDict):
    """Sorted ``dict``.

    This class is present to order query string and keep the request call always the
    same way. This is necessary to have reproducible tests with ``vcr.py``.

    ``dict`` ordering is deterministic before 3.6 and is not guaranteed in Python < 3.7
    """

    @classmethod
    def from_dict(cls, dct):
        odict = cls()
        for key in sorted(dct.keys()):
            odict[key] = dct[key]
        return odict
