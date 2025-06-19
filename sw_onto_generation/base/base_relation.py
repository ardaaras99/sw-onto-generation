from typing import ClassVar

from pydantic import BaseModel, Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import RelationModelConfig


class BaseRelation(BaseModel):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig()

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

    @classmethod
    def update_relation_config(cls: type[BaseModel], new_relation_config: RelationModelConfig) -> None:
        if not hasattr(cls, "relation_config"):
            raise ValueError(f"Model {cls.__name__} has no relation_config")

        # yeni relation_type ı parenttakinin üstüne yaz
        # yeni relation configdeki descriptionı, parenttan gelenle birleştir
        # yeni relation configdeki field_configsı, parenttan gelenle birleştir
        # TODO: fieldları check et, eğer modele ait değilse buna index ekleyemezsin diye hata ver,
        # TODO: eğer modele aitse ve çoktan bir index varsa, bu property ait bir index var hatası ver
