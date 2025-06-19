from typing import ClassVar

from pydantic import BaseModel, Field, field_validator

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

    # Define node_id with default=None so it can be set during validation
    node_id: int = Field(default=None)

    @field_validator("node_id")
    def validate_node_id(self, v: int) -> int:
        """
        Validate that the node_id is a valid 64-bit integer.
        If not provided (None), a new ID will be generated.
        """
        # Generate a new ID if None was provided
        if v is None:
            return _snowflake_generator.generate_id()

        # Ensure the provided ID is valid
        if not isinstance(v, int):
            raise ValueError("node_id must be an integer")

        # Check if it's within 64-bit range
        max_64bit = (1 << 63) - 1
        min_64bit = -(1 << 63)

        if not (min_64bit <= v <= max_64bit):
            raise ValueError(f"node_id {v} exceeds 64-bit integer limits")

        # Check bit length
        if v.bit_length() > 64:
            raise ValueError(f"node_id has {v.bit_length()} bits, exceeding the 64-bit limit")

        return v

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
