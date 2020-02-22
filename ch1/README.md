# Chapter 1

Chapter 1 of the book dealt with setting up pytest and becoming familiar
with some of its command-line arguments. This repository did not include
arguments such as `--tb` for traceback, the arguments for failing tests:
`-x`, `--maxfails=num`, `--lf`, and `--ff`, and the `--capture` stuff to
provide more alternatives to `-s`. Of course, `--version` doesn't appear
in test code either.

## Traceback styles

Traceback styles provided different ways to display failing tests, which
would be specified as parameters for `--tb`, e.g. `--tb=no`.

Styles listed in the book (v3.2 or v3.0.7?) were:

  - no (only shows the status of each test, [.FsxXE])
  - line (just the ErrorType line, e.g. AssertionError)
  - short
  - long (the most verbose)
  - auto (long tracebacks for first and last fails, the default option)
  - native

Some styles may have changed in pytest 5.3.5 (as of this repo).

