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
    search_type: NebulaIndexType | None = Field(default=None, description="Nebula graph'de field'un index type'ı")
    default_relation_type: str | None = Field(default=None, description="Eğer bu field bir relation ise, bu field'un default relation type'ı nedir. Eğer relation değilse None olmalı")


class NodeModelConfig(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    node_tag: str = Field(default="", description="Nebula graph'de node'un tag'i")
    nodetag_index: bool = Field(default=False, description="This tag is indexed in Nebula Graph")
    description: str = Field(description=" LLMe nodu tanıtmak için kullanılır")
    cardinality: bool = Field(description="LLMe node'un birden fazla olup olmadığını belirtir")
    ask_llm: bool = Field(default=True, description="LLM e sorup sorulmayacağını belirtir")
    nodeclass_to_be_created_automatically: type[BaseModel] | None = Field(default=None, description="Bu node'un oluşturulması için kullanılacak base node'un tipi")
    extra_fields: list[FieldInfo] = Field(default_factory=list, description="Node'a eklenecek ekstra field'lar")
    field_configs: list[FieldConfig] = Field(default_factory=list, description="Nebula graph'de node'un field'larının config'i, hangi field'ların index type'ı ne olacak")


class RelationModelConfig(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    edge_index: bool = Field(default=False, description="Index of the edge in Nebula Graph")
    description: str | None = Field(default=None, description="LLMe Relation'u tanıtmak için kullanılır")
    ask_llm: bool = Field(default=True, description="Eğer relation iki node un var olması durumunda otomatik bir şekilde oluşuyorsa False, yoksa True")
    extra_fields: list[FieldInfo] | None = Field(default=None, description="Relation'a eklenecek ekstra field'lar")
    field_configs: list[FieldConfig] | None = Field(default=None, description="Nebula graph'de relation'un field'larının config'i, hangi field'ların index type'ı ne olacak")
