# PSYC161 Homework #2

This homework is a part of the
[PSYC161 Introduction to Programming for Psychologists & Neuroscientists](https://github.com/dartmouth-pbs/psyc161)
course work.

## Ultimate goal

On the example of a simple Python program

- solidify interaction with [Git](http://git-scm.com),
  [GitHub](http://github.com), [nose](https://nose.readthedocs.org),
  [Travis CI](http://travis-ci.org/) and [Coveralls](https://coveralls.io/)

- practice good coding/documentation habits
  ([PEP8](https://www.python.org/dev/peps/pep-0008/),
  [NumPy docstrings](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard))

- learn to use learned basic Python constructs (functions, loops) and
  data types (strings, lists, etc)

- do rudimentary file I/O (input/output)

- discover and use
  [argparse](https://docs.python.org/2/library/argparse.html) library
  to help managing command line options


## Problem to solve

We are in the situation, when unfortunately there is no plain simple
utility to ask our experiment participants few simple questions before
running a real experiment.

**Approach**:  We will create a new handy little helper tool

**Solution**:

1. Write a program which will
    - read questions from an external file
    - verify that the file has questions formatted correctly, if not
      -- report an error and exit with exit code 1
    - present questions to the participant in the order present in
      the file, and upon answer which doesn't conform the list of
      available choices -- repeat the question
    - collect their input and response timing information
    - store results into an output file

    Program should

	- carry unit-tests to verify correct operation
	- be well documented (docstrings for functions, in the header of
      the file)
	- have correct executable permissions to be ran as `./questionnairer.py`


### "Extra credit"

1. Create a unit-test which goes through available questionnaires
   (under questionnaires/) and verifies that they are all of correct
   syntax, and could be used for the experiment.

2. Provide `--randomize` option to present questions in the random
   order.

3. Provide `--check-input` option which would allow to test syntax of
   any given questionnaire input file without actually running it.  It
   should exit with exit code

      - 2 if file is of incorrect syntax
      - 3 if file has no questions (empty or only comments)

4. Provide `--ai` mode mimicing a life person responding, using
   specified output file as input for information about responses and timing


## HOWTO

- For instructions on basic Git/GitHub manipulations, see
   [psyc161-hw1/README.md](https://github.com/dartmouth-pbs/psyc161-hw1/blob/master/README.md#howto)

- Sample questionnaires for you to practice/test on are available
  under `questionnaires/` directory, which will give you an idea of
  how input/output should be structured.
