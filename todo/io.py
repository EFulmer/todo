import csv
import pathlib
from dataclasses import dataclass
from typing import Generator


@dataclass
class ToDoItem:
    _id: int
    name: str
    date_created: str
    complete: bool

    def __str__(self):
        return f"{self._id}. {self.name}"


def read_items(file_name: str) -> Generator[ToDoItem, None, None]:
    """Read to-do list items from the given CSV.

    Args:
        file_name: name of the CSV file with the to-do list items.

    Raises:
        FileNotFoundError: if file_name does not exist.

    Yields:
        ToDoItems from the file, in order.
    """
    if not pathlib.Path(file_name).exists():
        raise FileNotFoundError(f"{file_name} does not exist")
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            yield ToDoItem(*row)
