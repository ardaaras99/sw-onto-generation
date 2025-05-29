from dataclasses import dataclass
from enum import StrEnum

from pydantic import BaseModel


class SearchType(StrEnum):
    EXACT = "exact"
    FULLTEXT = "fulltext"
    PARTIAL = "partial"
    FUZZY = "fuzzy"
    VECTOR = "vector"


@dataclass
class FieldProp:
    field_name: str = ""
    search_type: SearchType = SearchType.EXACT


@dataclass
class NodeProp:
    dgraph_type: str = ""


@dataclass
class DGraphProps:
    node_prop: NodeProp
    field_props: list[FieldProp]

    @staticmethod
    def check_field_props(target_class: type[BaseModel], field_props: list[FieldProp]) -> None:
        provided_field_names = [field_prop.field_name for field_prop in field_props]
        existing_field_names = [field_name for field_name in target_class.model_fields.keys()]
        for field_name in provided_field_names:
            if field_name not in existing_field_names:
                raise ValueError(f"Field {field_name} not found in model {target_class.__name__}, existing fields: {existing_field_names}")


@dataclass
class LLMHelperProps:
    description: str = "Base Node Description"
    cardinality: bool = True
