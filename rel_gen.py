# %%
from typing import ClassVar

from rich import print as rprint

from sw_onto_generation.base_relation import BaseRelation, GraphPropsForRelation, LLMHelperPropsForRelation, NebulaIndexType
from sw_onto_generation.common import SozlesmeBitisTarihi
from sw_onto_generation.kira import Mulk


class KiraSuresi(BaseRelation):
    model_config: ClassVar[dict] = {
        LLMHelperPropsForRelation.__name__: LLMHelperPropsForRelation(
            description="Kira sözleşmesinin süresini belirler.",
        ),
        GraphPropsForRelation.__name__: GraphPropsForRelation(
            relation_type="KiraSuresi",
            index_type=NebulaIndexType.EXACT,
        ),
    }
    source_node: Mulk
    target_node: SozlesmeBitisTarihi


rprint(KiraSuresi.model_fields)
rprint(KiraSuresi.model_config)

# %%
