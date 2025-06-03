from enum import StrEnum

from pydantic import BaseModel, Field


class NebulaIndexType(StrEnum):
    EXACT = "exact"
    VECTOR = "vector"


# Burada yer alan tüm descriptionlar Ontology yazanların neyin ne işe yaradığını anlaması için kullanılır.
class FieldConfig(BaseModel):
    field_name: str = Field(description="Nebula graph'de field'un adı")
    search_type: NebulaIndexType = Field(description="Nebula graph'de field'un index type'ı")


class NodeModelConfig(BaseModel):
    node_tag: str = Field(description="Nebula graph'de node'un tag'i")
    description: str = Field(description=" LLMe nodu tanıtmak için kullanılır")
    cardinality: bool = Field(description="LLMe node'un birden fazla olup olmadığını belirtir")
    field_configs: list[FieldConfig] | None = Field(default=None, description="Nebula graph'de node'un field'larının config'i, hangi field'ların index type'ı ne olacak")


class RelationModelConfig(BaseModel):
    relation_type: str = Field(description="Nebula graph'de relation'un adı")
    description: str = Field(description="LLMe Relation'u tanıtmak için kullanılır")
    field_configs: list[FieldConfig] | None = Field(default=None, description="Nebula graph'de relation'un field'larının config'i, hangi field'ların index type'ı ne olacak")
