from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import NodeModelConfig
from sw_onto_generation.common.common_nodes import Adres


class KiraKonusuMulk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Bu bir bina, ev, ofis, işyeri veya başka bir gayrimenkul olabilir. Kira sözleşmesinin konusu olan mülkü tanımlar. Kira konusu mülk, tip, buyukluk, adres ve diğer özellikleri içerebilir.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    tur: str = Field(
        default="",
        description="Kira konusu mulkun turunu belirtir Ev, arsa, ofis, tarla, isyeri, bina gibi",
    )
    adres: Adres | None = Field(
        default=None,
        description="Kira konusu mülkün adresi, konumu",
    )
    olcum: str = Field(
        default="",
        description="Kira konusu mülkün ölçüm birimi, örneğin metrekare, dönüm, hektar gibi. Lutfen olcum birimini de belirtiniz",
    )


class Depozito(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kira konusu mulk icin istenilan depozito. Para, altin, doviz , teminat mektubu gibi seyler olabilir. kira sozlesmeleri icin ozel bir teminat turudur. Mutlaka miktar ve turu belirtilmelidir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    depozitoturu: str = Field(
        default="Para",  # Default olarak Para alindi, eger baska bir tur varsa degistirilebilir
        description="Kira icin verilen dopozitonun turu,teminat mektubu, banka teminatı, altin gibi seyler olabilir. Eger para ise turune gore TL, USD, EUR gibi birim belirtiniz",
    )
    miktar: str = Field(
        default="",
        description="Kira icin verilen depozito miktari, para birimi ile birlikte yazilmalidir. Ornegin 1000 TL, 500 USD gibi veya 1000 gram altin gibi. Eger para birimi belirtilmemisse TL olarak alinir.",
    )


class Demirbaslar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Predefined",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    demirbas_var: bool = Field(
        default=False,
        description="Kiralan mulk icin sozlesmede demirbas belirtilmis mi ?",
    )


class Demirbas(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sozlesmede demirbas olarak belirtilen esya, donanim, malzeme, mobilya, klima, mutfak esyasi, garaj esyasi etc. gibi seyler. kiracinin sadece kullanabilecegi ama mulkiyeti mulk sahibinde bulunan ve sozlesmede belirtilen esyalar.Birden fazla olabilir. madde madde belirtilebilecegi gibi virgule ayrilmis bir metin ile de belirtilebilir. her birini ayri bir node olarak cikarmani istiyorum.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Demirbaslar,
    )
    demirbas_özellikleri: str = Field(
        default="",
        description="Demirbasin adi, ozellikleri, markasi, modeli gibi bilgiler icerebilir",
    )


class KiraBedeli(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kira sozlesmesinde belirlenen kira miktari. Bu miktar aylik veya yillik olarak belirtilmis olabilir. Kira bedeli, para birimi ile birlikte yazilmalidir. Ornegin 1000 TL, 500 USD gibi.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    kira_bedeli: float = Field(
        default=0.0,
        description="Kira bedeli miktari",
    )
    para_birimi: str = Field(
        default="TL",
        description="Kira bedelinin para birimi. Ornegin TL, USD, EUR gibi",
    )
    odeme_periyodu: str = Field(
        default="Aylık",
        description="Kira bedelinin odeme periyodu. Ornegin Aylık, Yıllık gibi. Eger belirtilmemisse Aylık olarak alinir.",
    )
    odeme_bilgisi: str = Field(
        default="",
        description="Kira bedelinin nasil odenecegi, odeme sarti. Ornegin peşin, aylik, yillik gibi. Ayin 5 inci gunu, ayin ilk 3 gunu gibi detaylar da eklenebilir.",
    )
    odeme_yontemi: str = Field(
        default="",
        description="Kira bedelinin odeme yontemi. Ornegin banka havalesi, nakit, kredi karti gibi. Hangi hesaba odenecegi de belirtilebilir.",
    )


class KiraAmaci(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kiralanan seyin ne icin kullanilacagi. En cok karsilasilan mesken, ev, ofis, fabrika, depo, isyeri, lokanta, restoran gibi seyler olabilir. daha uzun aciklamalar da olabilir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    kira_amaci: str | None = Field(
        default="",
        description="sozlesmedeki kiralanan seyin ne amacla kiralandigi",
    )


class SimdikiDurum(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kiralanan seyin simdiki durumunu gosterir. Kiralanan seyin mevcut durumu, onarim gerektirip gerektirmedigi, kiralanan seyin kullanilabilirligi, kiralanan seyin bakim gerektirip gerektirmedigi gibi bilgileri icerir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    simdiki_durum: str | None = Field(
        default="",
        description="sozlesmedeki kiralanan seyin simdiki durumu, onarim gerektirip gerektirmedigi, bakim gerektirip gerektirmedigi gibi bilgiler",
    )
