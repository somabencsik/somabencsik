"""This module contains the information for Todo model."""

from __future__ import annotations


class Todo:
    """
    Class description for Todo model.

    Attributes
    ----------
    message : str
        Message of the todo.
    """

    objects: list[Todo] = []

    def __init__(self, message: str) -> None:
        self.message = message

        self.done = False

        Todo.objects.append(self)

    def change_status(self) -> None:
        """Checks the todo."""
        self.done = not self.done
