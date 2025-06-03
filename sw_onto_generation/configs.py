from dataclasses import dataclass
from enum import StrEnum


class SearchType(StrEnum):
    EXACT = "exact"
    FULLTEXT = "fulltext"
    PARTIAL = "partial"
    FUZZY = "fuzzy"
    VECTOR = "vector"
    TERM = "term"


@dataclass
class FieldProp:
    field_name: str | None = None
    search_type: SearchType | None = None


@dataclass
class NodeProp:
    dgraph_type: str | None = None


@dataclass
class DGraphProps:
    node_prop: list[NodeProp] | None = None
    field_props: list[FieldProp] | None = None


@dataclass
class LLMHelperProps:
    description: str | None = None
    cardinality: bool | None = None
