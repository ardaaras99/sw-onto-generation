from typing import ClassVar

from pydantic.fields import FieldInfo

from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import GeneralDocumentInfo, Insan, Sirket


class HasKiracı(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede yer alan kiracıyı belirler.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="hasKiracı")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket
