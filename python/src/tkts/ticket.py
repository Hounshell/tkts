from __future__ import annotations  # Must be line 1

"""
Ticket class.
"""

from tkts.models.schema import Schema

_PRIVATE_TOKEN = object()

_Storage = tuple[str, None] | tuple[None, int] | tuple[str, int]


class Ticket:
  """Represents a single ticket along with all associated data."""

  @staticmethod
  def create(schema: Schema, description: str) -> TicketDelta:
    return TicketDelta(_PRIVATE_TOKEN, Ticket(_PRIVATE_TOKEN, None, schema, []), description)

  def __init__(self, token: object, ticket_id: str | None, schema: Schema, facts: list[tuple[str, _Storage]]):
    if token is not _PRIVATE_TOKEN:
      raise RuntimeError("Create a new ticket with tkts.Ticket.create() or load one from a tkts.storage.Storage object")

    self.__ticket_id = ticket_id
    self.__schema = schema
    self.__facts = facts

  @property
  def ticket_id(self):
    """Gets the unique ticket id."""
    return self.__ticket_id

  @property
  def schema(self):
    """Gets the schema associated with this ticket."""
    return self.__schema

  def update(self, description: str) -> TicketDelta:
    """Starts updating this ticket."""
    return TicketDelta(_PRIVATE_TOKEN, self, description)


class TicketDelta:
  """Represents pending changes to a ticket."""

  def __init__(self, token: object, ticket: Ticket, description: str):
    if token is not _PRIVATE_TOKEN:
      raise RuntimeError("Create a new ticket with tkts.Ticket.create() or modify an existing one with tkts.Ticket.update()")

    self.__ticket = ticket
    self.__description = description



