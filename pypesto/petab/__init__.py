"""
PEtab
=====

pyPESTO support for the PEtab data format.
"""
from .importer import PetabImporter

# PEtab and amici are optional dependencies
try:
    import petab
except ImportError:
    raise ImportError("PEtab import requires an installation of petab "
                      "(https://github.com/PEtab-dev/PEtab). "
                      "Install via `pip3 install petab`.")
try:
    import amici
except ImportError:
    raise ImportError("PEtab import requires an installation of amici "
                      "(https://github.com/icb-dcm/amici). "
                      "Install via `pip3 install amici`.")
