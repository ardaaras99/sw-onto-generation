__version__ = "0.1.0"
import inspect
import sys
from enum import StrEnum


class LegalContract(StrEnum):
    KIRA = "kira"
    ABONELIK = "abonelik"


# class KullanımKlavuzu(StrEnum):
#     DONANIM = "donanım"
#     YAZILIM = "yazılım"


# Automatically collect all StrEnum classes defined in this module


ENUM_CLASSES = [
    cls
    for name, cls in inspect.getmembers(sys.modules[__name__])
    if inspect.isclass(cls) and issubclass(cls, StrEnum) and cls is not StrEnum
]
#! add enum classes to the structure

DIR_STRUCTURE = {}
for enum_class in ENUM_CLASSES:
    entries = []
    for entry in enum_class:
        entries.append(entry)
    DIR_STRUCTURE[enum_class.__name__] = entries
