from enum import StrEnum

from pydantic import BaseModel, Field


class NebulaIndexType(StrEnum):
    EXACT = "exact"
    VECTOR = "vector"


class NodeFieldConfig(BaseModel):
    index_type: NebulaIndexType | None = Field(
        default=None, description="Nebula graph'de field'un index type'ı"
    )


class RelationFieldConfig(BaseModel):
    index_type: NebulaIndexType | None = Field(
        default=None, description="Nebula graph'de field'un index type'ı"
    )
    default_relation_type: str | None = Field(
        default=None,
        description="Eğer bu field bir relation ise, bu field'un default relation type'ı nedir. Eğer relation değilse None olmalı",
    )


class NodeModelConfig(BaseModel):
    # model_config = {"arbitrary_types_allowed": }
    nodetag_index: bool = Field(description="This tag is indexed in Nebula Graph")
    description: str = Field(description=" LLMe nodu tanıtmak için kullanılır")
    cardinality: bool = Field(description="LLMe node'un birden fazla olup olmadığını belirtir")
    ask_llm: bool = Field(description="LLM e sorup sorulmayacağını belirtir")
    nodeclass_to_be_created_automatically: type[BaseModel] | None = Field(
        description="Bu node'un oluşturulması için kullanılacak base node'un tipi"
    )

    model_config = {"extra": "forbid"}
    # extra_fields: list[FieldInfo] = Field(default=[], description="Node'a eklenecek ekstra field'lar")


class RelationModelConfig(BaseModel):
    # model_config = {"arbitrary_types_allowed": True}
    edge_index: bool = Field(default=False, description="Index of the edge in Nebula Graph")
    description: str | None = Field(
        default=None, description="LLMe Relation'u tanıtmak için kullanılır"
    )
    ask_llm: bool = Field(
        default=True,
        description="Eğer relation iki node un var olması durumunda otomatik bir şekilde oluşuyorsa False, yoksa True",
    )
    # extra_fields: list[FieldInfo] | None = Field(default=None, description="Relation'a eklenecek ekstra field'lar")
