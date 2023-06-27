import pytest

import todo.io


def test_read_items_fails_with_bad_file_name():
    with pytest.raises(FileNotFoundError):
        todo_gen = todo.io.read_items('this file does not exist.csv')
        next(todo_gen)


def test_read_items_happy_case():
    todo_gen = todo.io.read_items('tests/static/example.csv')
    next(todo_gen)
