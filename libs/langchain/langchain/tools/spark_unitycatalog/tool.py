from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from langchain_community.tools import (
        ListUnityCatalogTablesTool,
        InfoUnityCatalogTool,
        SqlQueryValidatorTool,
        QueryUCSQLDataBaseTool,

    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "ListUnityCatalogTablesTool": "langchain_community.tools",
    "InfoUnityCatalogTool": "langchain_community.tools",
    "SqlQueryValidatorTool": "langchain_community.tools",
    "QueryUCSQLDataBaseTool": "langchain_community.tools",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "ListUnityCatalogTablesTool",
    "InfoUnityCatalogTool",
    "SqlQueryValidatorTool",
    "QueryUCSQLDataBaseTool",
]
