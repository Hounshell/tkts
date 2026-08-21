"""
Ticket schema class.
"""

from tkts import utils
from tkts.models.facts import Fact


class Schema:
  """Defines the schema for a ticket."""

  def __init__(
      self,
      name: str | None = None,
      code_name: str | None = None,
      facts: list[Fact] | None = None):

    # Set the name and code_name based on inputs and generator.
    name, code_name = utils._get_name_and_code_name(name, code_name)

    self.__name = name
    self.__code_name = code_name
    self.__facts = (facts or [])[:]

    # Make sure that each fact has a unique code_name
    seen_fact_names = set()
    for fact in facts or []:
      if fact.code_name in seen_fact_names:
        raise ValueError(f"Fact {fact.code_name} has the same name as another fact")

      seen_fact_names.add(fact.code_name)

  @property
  def name(self):
    """Gets the name of this schema."""
    return self.__name

  @property
  def code_name(self):
    """Gets the code name of this schema."""
    return self.__code_name

  @property
  def facts(self):
    """Gets the list of facts in this schema."""
    return self.__facts[:]

