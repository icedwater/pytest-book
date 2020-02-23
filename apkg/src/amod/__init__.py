"""
This file determines how modules within this package are imported.
In this case, since `amod.py` is in the `amod/` directory, and the
the package's `setup.py` is told to look for modules in `src/`, we
are really importing the code in the `amod/amod.py` for `apkg`.

This means when `apkg` is installed, we `import amod`, NOT `apkg`.
"""

from amod.amod import *
