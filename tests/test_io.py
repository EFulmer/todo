import pytest

import todo.io


def test_read_items_fails_with_bad_file_name():
    with pytest.raises(FileNotFoundError):
        todo_gen = todo.io.read_items("this file does not exist.csv")
        next(todo_gen)


def test_read_items_happy_case():
    todo_gen = todo.io.read_items("tests/static/example.csv")
    next(todo_gen)


def test_show_all():
    todo_gen = todo.io.show_all("tests/static/example.csv")
    assert len(list(todo_gen)) == 2


def test_show_all():
    todo_gen = todo.io.show_non_complete("tests/static/example.csv")
    assert len(list(todo_gen)) == 1
