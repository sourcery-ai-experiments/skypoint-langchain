"""For backwards compatibility."""
from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from langchain_community.tools.spark_unitycatalog.prompt import QUERY_CHECKER, SQL_QUERY_VALIDATOR

_importer = create_importer(
    __package__,
    deprecated_lookups={
        "QUERY_CHECKER": "langchain_community.tools.spark_unitycatalog.prompt",
        "SQL_QUERY_VALIDATOR": "langchain_community.tools.spark_unitycatalog.prompt",
    },
)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _importer(name)


__all__ = ["QUERY_CHECKER", "SQL_QUERY_VALIDATOR"]
