import pytest
from palindrome import longest_palindromic_substring

# Test Input/Output and Long String
@pytest.mark.parametrize("s, expected",[
	("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"]),
	("abcdefg2222racecartacocattacocathijklmnop",["2222", "racecar", "tacocattacocat"])
])
def test_inputs_outputs(s, expected):
	result = longest_palindromic_substring(s)
	assert result in expected

# Test Constraint- 1 <= s.length <= 1000
@pytest.mark.parametrize("s",[
	"a",
	"a" * 1000
])
def test_length_constraint(s):
	result = longest_palindromic_substring(s)
	assert 1 <= len(result) <= 1000

# Test Constraint - s consists of only digits and English letters.
@pytest.mark.parametrize("s",[
	"abc121cba",
	"aba",
	"123321"
])
def test_alphanumeric(s):
	result = longest_palindromic_substring(s)
	assert result.isalnum()

# Edge Case - handle single-character strings
def test_single_character():
	assert longest_palindromic_substring("s") == "s"

# Edge Case - handle empty string
def test_empty_string():
	assert longest_palindromic_substring(" ") == " "

