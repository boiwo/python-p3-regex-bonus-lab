# regex_test.py

import re
from regex import my_regex

# Define the string used for testing
FINDALL_STRING = """
It's such a lovely day today.
Some weather we're having today, huh?
Maybe today's just not my day.
"""

def test_matches_its_such_a_lovely_day():
    '''matches the string "It's such a lovely day today."'''
    assert my_regex.fullmatch("It's such a lovely day today.")

def test_matches_some_weather_were_having():
    '''matches the string "Some weather we're having today, huh?"'''
    assert my_regex.fullmatch("Some weather we're having today, huh?")

def test_matches_maybe_todays_not_my_day():
    '''matches the string "Maybe today's just not my day."'''
    assert my_regex.fullmatch("Maybe today's just not my day.")

def test_finds_all_matches():
    '''can be used to find these three strings and ONLY these three strings.'''
    matches = my_regex.findall(FINDALL_STRING)
    expected_matches = [
        "It's such a lovely day today.",
        "Some weather we're having today, huh?",
        "Maybe today's just not my day.",
    ]
    assert matches == expected_matches
