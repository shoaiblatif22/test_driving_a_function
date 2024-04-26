# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

>>> As a user 
>>> So that i can keep track of my tasks
>>> I want to check if a text includes the string `#TODO`

## 2. Design the Function Signature
```python
def tasks(text)
    """Checks if tasks contains the word `#TODO`
        Paramaters: (text) => takes in a string(s) as an argument
        No side effects
        Paramaters: ([]) => takes in a list as an argument
        returns a list of tasks with the keyword '#TODO'
    """
    pass


```
## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

#1ST TEST CASE 
"""
Given a text check that it returns a string within a list
"""

tasks("hello") => ["hello"]

#2 TEST CASE

"""
Given no text, return an empty list
"""
tasks("") => []

#3 TEST CASE

"""
Given three tasks with no #TODO keyword, return "no tasks to be completed"
"""
tasks("hello", "hello", "hello") => "no tasks to be completed"

#4 TEST CASE

"""
Given three tasks with #TODO keyword, return the list of tasks
"""
tasks("hello1 #TODO", "hello2 #TODO", "hello3 #TODO") => ["hello1 #TODO", "hello2 #TODO", "hello3 #TODO"]

#5 TEST CASE

"""
Given three tasks with two tasks with the #TODO keyword and one task with no keyword, 
return the two tasks
"""
tasks("hello1 #TODO", "hello2", "hello3 #TODO") => ["hello1 #TODO", "hello3 #TODO"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.tasks.py import *

"""
Given a text check that it returns a string within a list
"""
def test_text_check_returns_a_list():
    result = tasks("hello world")
    assert result == ["hello world"]




```


