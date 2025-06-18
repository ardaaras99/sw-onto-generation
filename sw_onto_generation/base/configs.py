from enum import StrEnum

from pydantic import BaseModel, Field


class NebulaIndexType(StrEnum):
    EXACT = "exact"
    VECTOR = "vector"


class HowToExtract(StrEnum):
    CASE_0 = "case_0"  # LLM extract edecek
    CASE_1 = "case_1"  # nodes_to_be_created case i, başka bir node da bu node nodes_to_be_created içinde olacak
    CASE_2 = "case_2"  # bu node başka bir node in içinde field olarak bulunuyor olacak
    CASE_3 = "case_3"  # GeneralDocumentInfo node'u için kullanılır özel fonksiyonu var


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
    how_to_extract: HowToExtract = Field(description="LLM e sorup sorulmayacağını belirtir")
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
