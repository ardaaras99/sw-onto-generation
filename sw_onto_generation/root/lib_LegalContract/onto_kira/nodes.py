from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import NebulaIndexType, NodeFieldConfig, NodeModelConfig
from sw_onto_generation.common.common_nodes import Adres


class KiraKonusuMulk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Bu bir bina, ev, ofis, işyeri veya başka bir gayrimenkul olabilir. Kira sözleşmesinin konusu olan mülkü tanımlar. Kira konusu mülk, tip, buyukluk, adres ve diğer özellikleri içerebilir.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    tur: str | None = Field(
        default=None,
        description="Kira konusu mulkun turunu belirtir Ev, arsa, ofis, tarla, isyeri, bina gibi",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    adres: Adres | None = Field(default=None, description="Kira konusu mülkün adresi, konumu")
    olcum: str | None = Field(
        default=None,
        description="Kira konusu mülkün ölçüm birimi, örneğin metrekare, dönüm, hektar gibi. Lutfen olcum birimini de belirtiniz",
    )


class Depozito(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kira konusu mulk icin istenilen depozito. Para, altin, doviz , teminat mektubu gibi seyler olabilir. kira sozlesmeleri icin ozel bir teminat turudur. Mutlaka miktar ve turu belirtilmelidir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    depozitoturu: str | None = Field(
        default=None,  # Default olarak Para alindi, eger baska bir tur varsa degistirilebilir
        description="Kira icin verilen dopozitonun turu,teminat mektubu, banka teminatı, altin gibi seyler olabilir.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    miktar: str | None = Field(
        default=None,
        description="Kira icin verilen depozito miktari, para birimi ile birlikte yazilmalidir. Ornegin 1000 TL, 500 USD gibi veya 1000 gram altin gibi. Eger para birimi belirtilmemisse TL olarak alinir.",
    )
    para_birimi: str | None = Field(
        default=None,
        description="Kira icin verilen depozito miktari para birimi. Ornegin TL, USD, EUR gibi",
    )


class Demirbaslar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Predefined",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    demirbas_var: bool | None = Field(
        default=None, description="Kiralan mulk icin sozlesmede demirbas belirtilmis mi ?"
    )


class Demirbas(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sozlesmede demirbas olarak belirtilen esya, donanim, malzeme, mobilya, klima, mutfak esyasi, garaj esyasi etc. gibi seyler. kiracinin sadece kullanabilecegi ama mulkiyeti mulk sahibinde bulunan ve sozlesmede belirtilen esyalar.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Demirbaslar,
    )
    demirbas_özellikleri: str | None = Field(
        default=None,
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
    kira_bedeli: float | None = Field(default=None, description="Kira bedeli miktari")
    para_birimi: str | None = Field(
        default=None, description="Kira bedelinin para birimi. Ornegin TL, USD, EUR gibi"
    )
    odeme_periyodu: str | None = Field(
        default=None,
        description="Kira bedelinin odeme periyodu. Ornegin Aylık, Yıllık gibi. Eger belirtilmemisse Aylık olarak alinir.",
    )
    odeme_bilgisi: str | None = Field(
        default=None,
        description="Kira bedelinin nasil odenecegi, odeme sarti. Ornegin peşin, aylik, yillik gibi. Ayin 5 inci gunu, ayin ilk 3 gunu gibi detaylar da eklenebilir.",
    )
    odeme_yontemi: str | None = Field(
        default=None,
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
        default=None, description="sozlesmedeki kiralanan seyin ne amacla kiralandigi"
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
        default=None,
        description="sozlesmedeki kiralanan seyin simdiki durumu, onarim gerektirip gerektirmedigi, bakim gerektirip gerektirmedigi gibi bilgiler",
    )


class KiraArtisOrani(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kira bedelinin artış oranı ile ilgili bilgileri tanımlar. Yıllık TÜFE, TEFE-TÜFE ortalaması, sabit bir yüzde veya farklı formüller içerebilir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    artis_orani: str | None = Field(
        default=None,
        description="Kira artış oranı. Örneğin 'Yıllık %25', 'TÜFE', '12 aylık TÜFE ortalaması' gibi.",
    )
    artis_periyodu: str | None = Field(
        default=None,
        description="Kira artışının hangi periyotlarda uygulanacağı. Genellikle 'Yıllık' olur.",
    )
    artis_yontemi: str | None = Field(
        default=None,
        description="Kira artışının hesaplama yöntemi. Örneğin 'TÜFE', 'TEFE-TÜFE ortalaması', 'Sabit yüzde artış' gibi.",
    )
    artis_aciklama: str | None = Field(
        default=None,
        description="Kira artışı ile ilgili ek açıklamalar, hangi koşullarda uygulanacağı vb.",
    )


class GiderSorumluluklari(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kiralanan mülke ilişkin yan gider ve masrafların hangi tarafça karşılanacağını tanımlar. Elektrik, su, doğalgaz, aidat, vergi gibi kalemleri içerir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    elektrik: str | None = Field(
        default=None,
        description="Elektrik giderinin hangi tarafça ödeneceği. 'Kiracı', 'Kiraya Veren' vb.",
    )
    su: str | None = Field(default=None, description="Su giderinin hangi tarafça ödeneceği.")
    dogalgaz: str | None = Field(
        default=None, description="Doğalgaz giderinin hangi tarafça ödeneceği."
    )
    aidat: str | None = Field(
        default=None, description="Site/ apartman aidatının hangi tarafça ödeneceği."
    )
    emlak_vergisi: str | None = Field(
        default=None, description="Emlak vergisi veya benzeri vergilerin hangi tarafça ödeneceği."
    )
    diger_giderler: str | None = Field(
        default=None,
        description="Diğer gider kalemleri ve bunların sorumlulukları hakkında açıklama.",
    )


class Sigorta(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kiralanan mülkle ilgili sigorta yükümlülüklerini tanımlar. Konut sigortası, zorunlu deprem sigortası (DASK) vb. bilgileri içerir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    sigorta_tipi: str | None = Field(
        default=None,
        description="Sigorta türü. Örneğin 'Konut Sigortası', 'DASK', 'Eşya Sigortası' vb.",
    )
    sigorta_tutari: str | None = Field(
        default=None,
        description="Sigorta teminat tutarı veya poliçe bedeli. Para birimi ile birlikte.",
    )
    sigorta_saglayan: str | None = Field(
        default=None, description="Sigorta şirketi veya poliçeyi düzenleyen taraf."
    )
    sigorta_suresi: str | None = Field(
        default=None, description="Sigortanın geçerli olduğu süre veya poliçe bitiş tarihi."
    )
    sigorta_aciklama: str | None = Field(
        default=None,
        description="Sigorta ile ilgili ek açıklamalar, hangi tarafın masrafları üstleneceği vb.",
    )
