# %%
from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base_node import BaseNode
from sw_onto_generation.common import Adres
from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, NodeProp, SearchType


class Mulk(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="KiraKonusuMulk"),
            field_props=[
                FieldProp(field_name="tur", search_type=SearchType.EXACT),
            ],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="""
                Bu bir bina, ev, ofis, işyeri veya başka bir gayrimenkul olabilir. Kira sözleşmesinin konusu olan mülkü tanımlar.  
                Kira konusu mülk, tip, buyukluk, adres ve diğer özellikleri içerebilir.
                """,
            cardinality=True,
        ),
    }

    tur: str | None = Field(description="Kira konusu mulkun turunu belirtir Ev, arsa, ofis, tarla, isyeri, bina gibi")
    adres: Adres = Field(description="Kira konusu mülkün adresi, konumu")
    olcum: str | None = Field(default=None, description="Kira konusu mülkün ölçüm birimi, örneğin metrekare, dönüm, hektar gibi. Lutfen olcum birimini de belirtiniz")


# %%
