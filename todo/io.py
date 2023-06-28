"""Functions for reading and writing the To-Do list CSV."""
import csv
import dataclasses
import datetime
import pathlib
from typing import Generator


DATE_FORMAT = "%Y-%m-%d"
strptime = lambda x: datetime.datetime.strptime(x, DATE_FORMAT).date()


@dataclasses.dataclass
class ToDoItem:
    _id: int
    name: str
    date_created: datetime.date = dataclasses.field(default_factory=datetime.date.today)
    complete: bool = False

    def __str__(self):
        return f"{self._id}. {self.name}"


FIELDS = dataclasses.fields(ToDoItem)
FIELD_NAMES = [f.name for f in FIELDS]


def read_bool(s: str) -> bool:
    map_ = {
        "true": True,
        "false": False,
    }
    return map_[s.lower()]


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
        reader = csv.DictReader(f, fieldnames=FIELD_NAMES)
        for row in reader:
            # TODO(Eric): get types working nicely; e.g. complete
            # should get automatically converted to a boolean upon load
            yield ToDoItem(
                _id=row["_id"],
                name=row["name"],
                date_created=strptime(row["date_created"]),
                complete=read_bool(row["complete"]),
            )


def show_all(file_name: str) -> Generator[ToDoItem, None, None]:
    """Yield all items from the to-do list file specified.

    Args:
        file_name: name of the CSV file with the to-do list items.

    Raises:
        FileNotFoundError: if file_name does not exist.

    Yields:
        ToDoItems from the file, in order.
    """
    yield from (x for x in read_items(file_name))


def show_non_complete(file_name: str) -> Generator[ToDoItem, None, None]:
    """Yield outstanding items from the to-do list file specified.

    Args:
        file_name: name of the CSV file with the to-do list items.

    Raises:
        FileNotFoundError: if file_name does not exist.

    Yields:
        Not-yet-completed ToDoItems from the file, in order.
    """
    yield from (x for x in read_items(file_name) if not x.complete)


def add_item(file_name: str, task: str):
    """Add an item to the to-do list.

    Args:
        file_name: name of the CSV file containing the to-do list.

    Side Effects:
        Writes `task` to the to-do list, set as not complete and with a
        date_created of today.
    """
    item = ToDoItem(_id=..., task=task)
    with open(file_name, mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writerow(**item)
