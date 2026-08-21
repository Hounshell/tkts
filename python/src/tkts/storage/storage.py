"""
Base class and simple examples of storage for TKTS.
"""

from abc import ABC, abstractmethod
from tkts.models.schema import Schema
from tkts.ticket import Ticket


class Storage(ABC):
  """Storage repository for TKTS."""

  def __init__(self, all_schemas: list[Schema]):
    self.__all_schemas: dict[str, Schema] = {s.code_name: s for s in all_schemas}


  @abstractmethod
  def commit(self, change) -> Ticket:
    """Commits a ticket change-log to storage and returns the resulting ticket."""

  @abstractmethod
  def load(self, ticket_id: str) -> Ticket | None:
    """Loads a single ticket from storage by id."""

  @abstractmethod
  def query(self, *query_blocks: str) -> list[Ticket]:
    """Queries storage for zero or more tickets."""

  def _load_ticket(self, ticket_id: str, schema_name: str) -> Ticket:
    return Ticket(ticket_id, None, self.__all_schemas[schema_name], [])


class MemoryStorage(Storage):
  """Simple in-memory storage of basic ticket data."""

  def commit(self, change):
    assert False

  def load(self, ticket_id):
    assert False

  def query(self, *query_blocks):
    assert False

