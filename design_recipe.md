# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> > > As a user
> > > So that i can keep track of my tasks
> > > I want to check if a text includes the string `#TODO`

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

"""
Given: no text
When: no string is passed as an argument
Then: return an empty list
"""
def test_no_args_returns_empty_string():
    result = tasks(" ")
    assert result == []

"""
Given: three tasks with no #TODO keyword
When: when a list is passed as arguments
Then: return "no tasks to be completed"
"""
def test_when_a_list_is_passed_as_an_argument():
    result = tasks(["hello1", "hello2", "hello3"])
    assert result == "no tasks to be completed"


"""
Given: three tasks with #TODO keyword
When: when a list is passed as arguments
Then: return the list of tasks
"""
def test_todo_exists_then_return_list():
    result = tasks(["hello1 #TODO", "hello2 #TODO", "hello3 #TODO"])
    assert result == ["hello1 #TODO", "hello2 #TODO", "hello3 #TODO"]


"""
Given:three tasks
When: one of the tasks has no #TODO keyword
Then: return the two tasks
"""
def test_returns_tasks_with_todo_keyword():
    result = tasks(["hello1 #TODO", "hello2 #TODO", "hello3"])
    assert result == ["hello1 #TODO", "hello2 #TODO"]

```
