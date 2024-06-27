"""For backwards compatibility."""
from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from langchain_community.tools.sql_coder.prompt import SQL_QUERY_CREATOR_RETRY, SQL_QUERY_CREATOR_7b


_importer = create_importer(
    __package__,
    deprecated_lookups={
        "SQL_QUERY_CREATOR_RETRY": "langchain_community.tools.sql_coder.prompt",
        "SQL_QUERY_CREATOR_7b": "langchain_community.tools.sql_coder.prompt",
    },
)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _importer(name)


__all__ = ["SQL_QUERY_CREATOR_RETRY", "SQL_QUERY_CREATOR_7b"]
