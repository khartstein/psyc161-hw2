#!/usr/bin/env python

import argparse
import sys
import os
from os.path import exists
import time

os.chdir('/Users/Kevin/Documents/psyc161-hw2/questionnaires/')

# NOTE: API (what functions are named, their arguments and return values) is
#       only suggestive.
#
#       Feel free to change everything for this homework.


def read_questions(input_file):
    """Reads questions and answer choices from the input_file
    """
    # Questions will be a list where each item consists of a list where first
    # element is the question, and the 2nd through nth elements are available
    # choices.
    questions = []
    qList = []
    with open(input_file) as f:
        for line in f.readlines():
            if line[0] == '#':
                # this line of the questionnaire is a comment
                continue
            elif line[0] == '-':
                # this line of the questionnaire is a question
                if not qList == []:
                    questions.append(qList)
                qList = []
                newquestion = line.lstrip('- ')
                formattedquestion = newquestion.rstrip('\n')
                qList.append(formattedquestion)
            elif line[0:3] == '  *':
                # this line of the questionnaire is an answer
                newanswer = line.lstrip('  *')
                formattedanswer = newanswer.rstrip('\n')
                qList.append(formattedanswer)
            else:
                print 'Questionnaire is not properly formatted!'
                raise SystemExit(1)
    if not qList == []:
        questions.append(qList)
    return questions


def present_questions(questions, testing=False):
    """Presents each question in list and records answer/response time
    """
    answers, timings = [], []
    for question in questions:
        tStart = time.time()
        if testing:
            if len(question) == 1:
                answer = 'Billy Gates Junior'
            else:
                answer = question[1]
        else:
            answer = raw_input(question[0])
        if len(question) != 1:
            while answer not in question[1:]:
                print 'That is not an appropriate answer!'
                print 'available answers are',
                print question[1:]
                answer = raw_input(question[0])
        tResponse = (time.time() - tStart)
        answers.append(answer)
        timings.append(tResponse)
    return answers, timings


def write_answers(output_file, questions, answers, timings):
    """For each question, write question and participant's answer
    to  an output file. Formatting is the same as for the input
    questionnaire (i.e. lines beginning with '- " are questions, lines
    beginning with '  *' are answers (or response time)).
    """
    with open(output_file, 'w') as f:
        qNum = 0
        for question in questions:
            str2write = '- {}\n  * {}\n  * response time: {}\n'\
                .format(question[0], answers[qNum], timings[qNum])
            f.write(str2write)
            qNum += 1
    f.close()


def parse_options(argv):
    """Sets up options for call from command line
    """

    mainDocString = main.__doc__

    # Define command line options we know
    parser = argparse.ArgumentParser(description=mainDocString)
    parser.add_argument('input_file',
                        help='Input file containing questionnaire')
    parser.add_argument('-o', '--output_file',
                        help='Output file to store answers')

    # Parse command line options
    return parser.parse_args(argv[1:])


# We moved out this functionality into a separate function, so we could
# automatically test its correct function
def main(argv, testing=False):
    """Simple program to run a questionnaire and collect answers/RTs
    """
    args = parse_options(argv)
    if not exists(args.input_file):
        # Error messages are usually output to "standard error", not "standard
        # output", so we will write to the stderr directly as if it was a file.
        # .write() does not add a newline (\n) so we have to do it
        sys.stderr.write("File %s not found\n" % args.input_file)
        raise SystemExit(4)

    if not args.output_file:
        raise ValueError("Please provide the output file")

    questions = read_questions(args.input_file)
    answers, timings = present_questions(questions, testing)

    write_answers(args.output_file, questions, answers, timings)


#
# Testing routines
#
from nose.tools import assert_equal, assert_raises


def test_read_questions():
    """ Tests read_questions function to make sure that the provided
    questionnaire (sample1.txt) returns the appropriate list of questions
    """
    assert_equal(read_questions('sample1.txt'),
                 [['What is your name darling?'],
                 ['Have you slept well today?', 'yes', 'no'],
                 ['Rate from 1 (hate it) to 5 (love it) how much you like to '
                  'press buttons?', '1', '2', '3', '4', '5']])


def test_present_questions():
    """Tests present_questions function to make sure it's working
    """
    (ans, times) = present_questions([['What is your name darling?'],
                                     ['Have you slept well today?',
                                     'yes', 'no'],
                                      ['Rate from 1 (hate it) to 5 '
                                      '(love it) how '
                                       'much you like to press buttons?',
                                       '1', '2', '3', '4', '5']],
                                     testing=True)
    # answers should match defaults when keyword argument 'testing'
    # is set to True
    assert_equal(ans, ['Billy Gates Junior', 'yes', '1'])
    # Since responses are provided automatically, all response times
    # should be less than 0.1 seconds
    assert_equal(times[0:] < [0.1]*3, True)


def test_parse_options():
    """ Tests the parse_options function to make sure that it raises
    a TypeError when integers are provided as arguments instead of
    strings containing appropriate file names.
    """
    assert_raises(TypeError, parse_options, 'sample1.txt', 1)
    assert_raises(TypeError, parse_options, 1, 'output.txt')


def test_main():
    """Tests main function to see if it fails anywhere.
    """
    # Just run it and see it not fail -- we return nothing.  It is a
    # "smoke test"
    assert_equal(main(['questionnaire.py', '-o', 'NOSETEST_OUTPUT.txt',
                       'sample1.txt'], testing=True),
                 None)
    # Make sure we get a ValueError when output file is not specified
    assert_raises(ValueError, main, ['questionnaire.py', 'sample1.txt'],
                  testing=True)


if __name__ == '__main__':
    """Provided everything above is working ok, this will run the main function
    """
    # sys.argv provides command line arguments given to the script
    main(sys.argv)
