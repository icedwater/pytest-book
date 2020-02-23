# apkg: a quick demo of packaging and distribution

`apkg` is a Python package showing how easy it is to create
installable, maintainable, shareable packages and distributions.

It does contain one function, called `ans_all()`, to be used so:

    >>> import apkg
    >>> apkg.ans_all()
    42

That's it, really.

Note: one difference from the book is `setup.py` no longer has a
      `bdist_wheel` option. `bdist_egg` is available instead. Do
      check `python setup.py --help-commands` for the latest.
