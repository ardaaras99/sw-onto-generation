from pydantic import BaseModel, Field

from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, SearchType


class BaseNode(BaseModel):
    model_config = {
        DGraphProps.__name__: DGraphProps(
            field_props=[FieldProp(field_name="reason", search_type=SearchType.EXACT)],
        ),
        LLMHelperProps.__name__: LLMHelperProps(description="", cardinality=False),
    }
    reason: str = Field(description="Bu nodeu çıkarırken nasıl bir mantık kullandın")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Store the update_dict for later processing
        if hasattr(cls, "update_dict"):
            cls._pending_update_dict = cls.update_dict

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        super().__pydantic_init_subclass__(**kwargs)
        # Apply the pending update_dict after Pydantic has fully processed the class
        if hasattr(cls, "_pending_update_dict"):
            cls.modify_model_config(cls._pending_update_dict)
            delattr(cls, "_pending_update_dict")

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

        cls.model_config = cls.model_config
        for u_key, u_val in update_dict.items():
            # u value either DGraphProps or LLMHelperProps
            if u_key not in cls.model_config:
                cls.model_config[u_key] = u_val
            else:
                if u_key == LLMHelperProps.__name__:
                    val = cls.model_config[u_key]
                    # description'ı parenttan al ve ekle
                    u_val.description = f"{val.description}\n{u_val.description}"
                    # cardinality provide edilmemisse parenttan al
                    if u_val.cardinality is None:
                        u_val.cardinality = val.cardinality
                    cls.model_config[u_key] = u_val
                elif u_key == DGraphProps.__name__:
                    val: DGraphProps = cls.model_config[u_key]
                    existing_field_props = val.field_props
                    provided_field_props = u_val.field_props
                    field_names_of_cls = [field_name for field_name in cls.model_fields.keys()]

                    # provide edilen field prop cls te bir field değilse veya aynı field name ile bir field prop varsa hata ver
                    non_problematic_field_props = []
                    for fp in provided_field_props:
                        if fp.field_name not in field_names_of_cls:
                            raise ValueError(f"Field {fp.field_name} not found in model {cls.__name__}, existing fields: {field_names_of_cls}")
                        elif fp.field_name in [fp.field_name for fp in existing_field_props]:
                            raise ValueError(f"Field {fp.field_name} has already have index {fp.search_type}")
                        else:
                            non_problematic_field_props.append(fp)
                    u_val.field_props = non_problematic_field_props
                    u_val.field_props.extend(existing_field_props)
                    cls.model_config[u_key] = u_val
