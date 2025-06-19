from typing import Any, ClassVar

from pydantic import BaseModel, Field, model_validator

from sw_onto_generation.base.configs import (
    HowToExtract,
    NebulaIndexType,
    NodeFieldConfig,
    NodeModelConfig,
)
from sw_onto_generation.base.id_generator import SnowflakeGenerator

# Global instance of the Snowflake generator
_snowflake_generator = SnowflakeGenerator()


class BaseNode(BaseModel):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    reason: str = Field(
        description="Bu nodeu çıkarırken nasıl bir mantık kullandın",
        config=NodeFieldConfig(index_type=NebulaIndexType.VECTOR),
    )

    # Define node_id with default=None, but we'll always overwrite it
    node_id: int = Field(default=None)

    @model_validator(mode="before")
    @classmethod
    def generate_node_id(cls, data: Any) -> Any:
        """
        Always generate a new node_id, ignoring any provided value.
        """
        if isinstance(data, dict):
            # Always generate a new ID, regardless of whether one was provided
            data["node_id"] = _snowflake_generator.generate_id()
        return data

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
