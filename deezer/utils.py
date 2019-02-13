"""Utils."""

from collections import OrderedDict


class SortedDict(OrderedDict):
    @classmethod
    def from_dict(cls, dct):
        odict = cls()
        for key in sorted(dct.keys()):
            odict[key] = dct[key]
        return odict
