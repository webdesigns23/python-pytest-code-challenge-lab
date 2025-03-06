## Overview 
### Introduction: Algorithms in Interviews & Testing

#### What is an Algorithm?

An algorithm is a step-by-step procedure or set of rules designed to perform a task or solve a problem. Algorithms are the foundation of computer programming, defining how data is processed, stored, and retrieved efficiently.

#### Algorithms in Tech Interviews

Algorithm challenges are a core part of technical interviews for software engineers, used to evaluate problem-solving skills, coding ability, and efficiency. Companies such as Google, Meta, Amazon, and Microsoft frequently ask candidates to solve coding problems under time constraints.

#### How Leetcode & Codewars Use Testing

Platforms like Leetcode, Codewars, and HackerRank include test suites for each coding challenge. These test suites:

* Provide automated validation of solutions.
* Include edge cases and performance tests.
* Ensure code correctness before submission.

#### Your Task in This Lab

In this lab, you will build your own test suite for a common algorithm problem—the Longest Palindromic Substring—just like platforms like Leetcode would. Instead of solving a challenge with a pre-existing test set, you'll define the test cases yourself, ensuring robust validation before implementing the function (or using a provided solution).

### Scenario:

As a junior software developer, you have been assigned to work on a feature validation team that ensures code reliability before deployment. A senior engineer has provided a function requirement: identifying the longest palindromic substring in a given input string. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
<br>
Before implementing the function, the team follows a Test-Driven Development (TDD) approach, requiring you to first write a test suite that verifies correctness. Your task is to:
* Write test cases using pytest to validate a function for the Longest Palindromic Substring problem.
* Consider normal, edge, and failure cases to ensure test robustness.
* Run your tests and refine them as needed.
* Implement the function yourself OR use the provided working solution if needed.

## Instructions
### Set Up


### Instructions
1. Step 1: Understand the Challenge (5 min)
* You need to write tests for a function that finds the longest palindromic substring in a given string. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
* Function Signature
```python
def longest_palindromic_substring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring.
    """
    pass  # Function implementation comes later
```
* Example Inputs/Outputs

|   Input  |  Output | Explanation |
| --- | --- | --- |
| "babad" | "bab" or "aba" | Both are valid palindromes. |
| "cbbd" | "bb" | The longest palindrome is "bb". |
| “a” | “a” | A single character is always a palindrome. |
| “ac” | "a" or "c" | Either character is a valid palindrome. |
| “racecar” | “racecar” | The entire string is a palindrome. |

* Constraints / Assumptions
    * 1 <= s.length <= 1000
    * s consists of only digits and English letters.

2. Step 2: Write Your Test Suite
Your primary task is to create a Pytest test suite for the function in test_palindrome.py.
Your test cases should cover:
Basic Cases – Check common inputs return expected outputs.
Edge Cases – Handle single-character strings, empty strings, long strings, and no-palindrome cases.
⚠️ Do NOT implement longest_palindromic_substring yet! Follow the Test-Driven Development (TDD) approach.

3. Step 3: Run the Tests
Once you’ve written your test cases, run them using pytest:
pytest
You should see failing tests, since the function is not yet implemented. This is expected! 
If any of the tests pass without a solution implemented, something is wrong with your tests and you’ll need to debug.

4. Handle e

5. Step 5: Implement the Function
Now, solve the algorithm by adding code to the function in palindrome.py until all tests pass.
Break Glass Solution
🚨 The purpose of the lab is the test suite implementation, so if you cannot solve the problem on your own that’s okay! You can use this working solution:
def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    
    start, max_length = 0, 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and (j - i + 1) > max_length:
                start, max_length = i, j - i + 1
    
    return s[start:start + max_length]


Step 6: Verify and Submit (10 min)
Confirm your tests pass:
pytest
Push your final version to GitHub:
git add .
git commit -m "Completed testing lab"
git push origin main

