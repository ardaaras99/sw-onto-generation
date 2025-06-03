from dataclasses import dataclass
from enum import StrEnum

from pydantic import BaseModel, Field

from sw_onto_generation.base_node import BaseNode


@dataclass
class LLMHelperPropsForRelation:
    description: str | None = None


class NebulaIndexType(StrEnum):
    EXACT = "exact"
    FULLTEXT = "fulltext"
    PARTIAL = "partial"
    FUZZY = "fuzzy"
    VECTOR = "vector"


@dataclass
class GraphPropsForRelation:
    relation_type: str | None = None
    index_type: NebulaIndexType | None = None


class BaseRelation(BaseModel):
    source_node: BaseNode
    target_node: BaseNode
    reason: str = Field(description="Bu relationi çıkarırken nasıl bir mantık kullandın")

    @classmethod
    def append_field_description(cls: type[BaseModel], field_name: str, additional_description: str, seperator: str = " ") -> None:
        if field_name not in cls.model_fields:
            raise ValueError(f"Field {field_name} not found in model {cls.__name__}")

        else:
            field_info = cls.model_fields[field_name]

            if field_info.description:
                field_info.description += seperator + additional_description

    @classmethod
    def set_field_description(cls: type[BaseModel], field_name: str, new_description: str) -> None:
        if field_name not in cls.model_fields:
            raise ValueError(f"Field '{field_name}' not found in model {cls.__name__}")

        else:
            cls.model_fields[field_name].description = new_description
