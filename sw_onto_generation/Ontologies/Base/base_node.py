from typing import Any, ClassVar

from pydantic import BaseModel, Field

from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, NodeModelConfig


class BaseNode(BaseModel):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="BaseNode",
        description="",
        cardinality=False,
        field_configs=[FieldConfig(field_name="reason", search_type=NebulaIndexType.VECTOR)],
    )

    reason: str = Field(description="Bu nodeu çıkarırken nasıl bir mantık kullandın")
    reference_text: str = Field(description="Bu nodeu çıkarırken hangi metinleri kullandın, direkt kopyalayarak buraya yaz")

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        super().__pydantic_init_subclass__(**kwargs)
        # Only run for subclasses, not BaseNode itself
        if cls is BaseNode:
            return

        parent_config = getattr(cls.__base__, "node_config", None)
        child_config = getattr(cls, "node_config", None)

        if parent_config is not None and child_config is not None and parent_config is not child_config:
            # Merge node_tag: use child's
            node_tag = child_config.node_tag
            # Merge descriptions
            description = (parent_config.description or "") + "\n" + (child_config.description or "")
            # Merge field_configs
            parent_fields = {fc.field_name: fc for fc in parent_config.field_configs}
            child_fields = {fc.field_name: fc for fc in child_config.field_configs}
            merged_fields = list(parent_fields.values())
            for fname, fc in child_fields.items():
                if fname in parent_fields:
                    raise ValueError(f"Field '{fname}' already has an index in parent config for {cls.__name__}")
                merged_fields.append(fc)
            # Validate all field_configs reference fields on the subclass
            model_fields = set(cls.model_fields.keys())
            for fc in merged_fields:
                if fc.field_name not in model_fields:
                    raise ValueError(f"Field '{fc.field_name}' in node_config is not a field of model {cls.__name__}")
            # Merge other configs (cardinality, etc.) - use child's if present, else parent's
            cardinality = getattr(child_config, "cardinality", getattr(parent_config, "cardinality", False))
            # Create merged config
            merged_config = NodeModelConfig(
                node_tag=node_tag,
                description=description,
                cardinality=cardinality,
                field_configs=merged_fields,
            )
            cls.node_config = merged_config

    @classmethod
    def append_field_description(cls: type[BaseModel], field_name: str, additional_description: str, seperator: str = " ") -> None:
        """
        Field'un açıklamasının sonuna eklenecek açıklama ekler.

        Args:
            cls (type[BaseModel]): BaseNode'un kendisi
            field_name (str): Field'un adı
            additional_description (str): Field'un açıklamasının sonuna eklenecek açıklama
            seperator (str, optional): Field'un açıklamasının sonuna eklenecek separator. Defaults to " ".

        Raises:
            ValueError: Field'un adı modelde yoksa hata verir
        """

        if field_name not in cls.model_fields:
            raise ValueError(f"Field {field_name} not found in model {cls.__name__}")

        else:
            field_info = cls.model_fields[field_name]

            if field_info.description:
                field_info.description += seperator + additional_description
            else:
                field_info.description = additional_description

    @classmethod
    def set_field_description(cls: type[BaseModel], field_name: str, new_description: str) -> None:
        """
        Field'un açıklamasını değiştirir.

        Args:
            cls (type[BaseModel]): BaseNode'un kendisi
            field_name (str): Field'un adı
            new_description (str): Field'un açıklaması

        Raises:
            ValueError: Field'un adı modelde yoksa hata verir
        """
        if field_name not in cls.model_fields:
            raise ValueError(f"Field '{field_name}' not found in model {cls.__name__}")

        else:
            cls.model_fields[field_name].description = new_description
