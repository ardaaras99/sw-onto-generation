from enum import StrEnum

from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo


class NebulaIndexType(StrEnum):
    EXACT = "exact"
    VECTOR = "vector"


class DocumentType(StrEnum):
    KiraContracts = "Kira Sozleşmesi"
    GenelSozlesme = "Genel Sözleşme"


class CustomerType(StrEnum):
    KUrumsal = "Kurumsal Müşteri"


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
    model_config = {"arbitrary_types_allowed": True}
    edge_type: str | None = Field(default=None, description="Type of the edge in Nebula Graph")
    edge_index: bool = Field(default=False, description="Index of the edge in Nebula Graph")
    description: str | None = Field(default=None, description="LLMe Relation'u tanıtmak için kullanılır")
    extra_fields: list[FieldInfo] | None = Field(default=None, description="Relation'a eklenecek ekstra field'lar")
    field_configs: list[FieldConfig] | None = Field(default=None, description="Nebula graph'de relation'un field'larının config'i, hangi field'ların index type'ı ne olacak")
