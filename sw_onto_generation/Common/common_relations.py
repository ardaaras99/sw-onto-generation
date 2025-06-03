from typing import ClassVar

from sw_onto_generation.Base.base_relation import BaseRelation
from sw_onto_generation.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig
from sw_onto_generation.Common.common_nodes import GeneralDocumentInfo, Insan, Sirket


class HasKiracı(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        relation_type="hasKiracı",
        description="Sozlesmede yer alan kiracıyı belirler.",
        field_configs=[],
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket
