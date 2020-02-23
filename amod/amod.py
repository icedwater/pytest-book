"""
This module was developed following Appendix 4 on Packaging and
Distributing Python Projects in the PyTest book by Brian Okken.
It seems that while pip can install the module, uninstalling it
leaves it still importable because of __name__ being defined in
setup.py.
"""

def ans_all():
    """
    This returns the answer to the Ultimate Question. Nobody is
    aware of what the Question could be. #h2g2
    """
    return 42
