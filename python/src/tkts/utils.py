"""
Internal utility methods.
"""

def _get_name_and_code_name(name: str | None, code_name: str | None) -> tuple[str, str]:
  """Makes sensible choices for name and code_name based on each other."""

  if not name and not code_name:
    raise ValueError("Either name or code_name are required")

  name = name or code_name
  assert name is not None

  code_name = code_name or _generate_code_name(name)

  return (name, code_name)


def _generate_code_name(name: str) -> str:
  """Generates a code name based on a name."""

  return name.lower()

