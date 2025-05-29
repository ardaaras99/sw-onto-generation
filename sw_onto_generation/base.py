from pydantic import BaseModel, Field
from rich import print as rprint

from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, NodeProp, SearchType


class BaseNode(BaseModel):
    model_config = {
        DGraphProps.__name__: DGraphProps(node_prop=NodeProp(), field_props=[FieldProp(field_name="reason", search_type=SearchType.EXACT)]),
        LLMHelperProps.__name__: LLMHelperProps(),
    }
    reason: str = Field(description="Bu nodeu çıkarırken nasıl bir mantık kullandın")

    @classmethod
    def append_field_description(cls: type[BaseModel], field_name: str, additional_description: str, seperator: str = " ") -> None:
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
        if field_name not in cls.model_fields:
            raise ValueError(f"Field '{field_name}' not found in model {cls.__name__}")

        else:
            cls.model_fields[field_name].description = new_description

    @classmethod
    def modify_model_config(cls: type[BaseModel], update_dict: dict[str, DGraphProps | LLMHelperProps]) -> None:
        if not hasattr(cls, "model_config"):
            raise ValueError(f"Model {cls.__name__} has no model_config")

        current_config = cls.model_config

        for key, new_dc_instance in update_dict.items():
            if key not in current_config:
                current_config[key] = new_dc_instance
            else:
                if key == LLMHelperProps.__name__:
                    existing_value: LLMHelperProps = current_config[key]
                    new_dc_instance: LLMHelperProps = new_dc_instance

                    new_dc_instance.description = f"{existing_value.description}\n{new_dc_instance.description}"
                    current_config[key] = new_dc_instance
                elif key == DGraphProps.__name__:
                    new_dc_instance: DGraphProps
                    existing_value: DGraphProps = current_config[key]
                    DGraphProps.check_field_props(target_class=cls, field_props=new_dc_instance.field_props)
                    # append new field_props to existing field_props
                    new_dc_instance.field_props.extend(existing_value.field_props)
                    current_config[key] = new_dc_instance
