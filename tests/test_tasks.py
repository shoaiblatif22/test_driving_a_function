from lib.tasks import *
import pytest

@pytest.mark.skip
def test_no_args_returns_empty_string():
    result = tasks(" ")
    assert result == []


def test_text_check_returns_a_list():
    result = tasks(["hello world"])
    assert result == "no tasks to be completed"


def test_when_a_list_is_passed_as_an_argument():
    result = tasks(["hello1", "hello2", "hello3"])
    assert result == "no tasks to be completed"


def test_todo_exists_then_return_list():
    result = tasks(["hello1 #TODO", "hello2 #TODO", "hello3 #TODO"])
    assert result == ["hello1 #TODO", "hello2 #TODO", "hello3 #TODO"]
