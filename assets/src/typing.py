import typing as t

Any = t.Any
Headers = t.Dict[str, str]
User_Agent = t.NewType("User_Agent", str)
Messages = t.List[t.Dict[str, str]]

__all__ = ["Any", "Headers", "User_Agent", "Messages"]

# Path: src/typing.py