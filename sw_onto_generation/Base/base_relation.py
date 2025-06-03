from typing import ClassVar

from pydantic import BaseModel, Field

from sw_onto_generation.Base.base_node import BaseNode
from sw_onto_generation.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig


class BaseRelation(BaseModel):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        relation_type="BaseRelation",
        description="",
        field_configs=[
            FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT),
            FieldConfig(field_name="reason", search_type=NebulaIndexType.VECTOR),
        ],
    )

    source_node: BaseNode
    target_node: BaseNode
    reason: str = Field(description="Bu relationi çıkarırken nasıl bir mantık kullandın")

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        super().__pydantic_init_subclass__(**kwargs)
        # Only run for subclasses, not BaseNode itself
        if cls is BaseRelation:
            return

        parent_config = getattr(cls.__base__, "relation_config", None)
        child_config = getattr(cls, "relation_config", None)

        if parent_config is not None and child_config is not None and parent_config is not child_config:
            # Merge relation_type: use child's
            relation_type = child_config.relation_type
            # Merge descriptions
            description = (parent_config.description or "") + "\n" + (child_config.description or "")
            # Merge field_configs
            parent_fields = {fc.field_name: fc for fc in parent_config.field_configs}
            child_fields = {fc.field_name: fc for fc in child_config.field_configs}
            merged_fields = list(parent_fields.values())
            for fname, fc in child_fields.items():
                if fname in parent_fields:
                    raise ValueError(f"Field '{fname}' already has an index in parent config for {cls.__name__}, with search type {parent_fields[fname].search_type}")
                merged_fields.append(fc)
            # Validate all field_configs reference fields on the subclass
            model_fields = set(cls.model_fields.keys())
            for fc in merged_fields:
                if fc.field_name not in model_fields:
                    if fc.field_name == "relation_type":
                        pass
                    else:
                        raise ValueError(f"Field '{fc.field_name}' in relation_config is not a field of model {cls.__name__}")

            # Create merged config
            merged_config = RelationModelConfig(
                relation_type=relation_type,
                description=description,
                field_configs=merged_fields,
            )
            cls.relation_config = merged_config

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
