from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import NebulaIndexType, NodeFieldConfig, NodeModelConfig
from sw_onto_generation.common.common_nodes import Insan, Sirket


class KrediTutari(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi sözleşmesinde belirtilen toplam kredi tutarını tanımlar. Tutar mutlaka para birimi ile birlikte yazılmalıdır.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    kredi_tutari: float | None = Field(default=None, description="Kredi tutarı (sayı)")
    para_birimi: str | None = Field(default=None, description="Para birimi (TL, USD, EUR vb.)")
    aciklama: str | None = Field(
        default=None, description="Tutarla ilgili ek açıklama veya şartlar"
    )


class FaizBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Krediye uygulanacak faiz oranı ve hesaplama yöntemini tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    faiz_orani: str | None = Field(
        default=None, description="Faiz oranı (örn. '%1,89 aylık', 'Yıllık %23,5')"
    )
    faiz_turu: str | None = Field(
        default=None, description="Faiz türü (Sabit, Değişken, Azalan vb.)"
    )
    faiz_hesaplama_yontemi: str | None = Field(
        default=None, description="Faizin nasıl hesaplanacağı (basit, bileşik vb.)"
    )
    faiz_aciklama: str | None = Field(
        default=None, description="Faizle ilgili ek açıklamalar veya koşullar"
    )


class VadeBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin vadesi / toplam geri ödeme süresini tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    vade_suresi: str | None = Field(
        default=None,
        description="Vade süresi (örn. '36 Ay')",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    toplam_taksit: int | None = Field(default=None, description="Toplam taksit sayısı")


class GeriOdemePlani(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi geri ödeme planı hakkında detayları tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    taksit_sayisi: int | None = Field(default=None, description="Toplam taksit sayısı")
    taksit_tutari: str | None = Field(
        default=None, description="Her taksit tutarı ve para birimi (örn. '1.250 TL')"
    )
    odeme_periyodu: str | None = Field(default="Aylık", description="Ödeme periyodu (Aylık vb.)")
    ilk_odeme_tarihi: str | None = Field(default=None, description="İlk taksit tarihi (YYYY-MM-DD)")
    son_odeme_tarihi: str | None = Field(default=None, description="Son taksit tarihi (YYYY-MM-DD)")


class KrediAmaci(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin kullanım amacını (ihtiyaç, tatil, eğitim, sağlık vb.) tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    kredi_amaci: str | None = Field(default=None, description="Kredinin kullanım amacı")


class TahsisUcreti(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi tahsis / dosya ücreti bilgilerini tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    tahsis_ucreti: str | None = Field(
        default=None, description="Tahsis ücreti ve para birimi (örn. '420 TL')"
    )


class ErkenOdemeCezasi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin erken kapatılması hâlinde uygulanacak ücret veya ceza bilgisini tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    ceza_tutari: str | None = Field(
        default=None, description="Erken ödeme cezası (örn. '%2', '350 TL')"
    )
    aciklama: str | None = Field(
        default=None, description="Cezayla ilgili ek açıklama veya şartlar"
    )


class SigortaBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi kapsamında yaptırılan hayat, işsizlik veya ferdi kaza sigortası detaylarını tanımlar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    sigorta_tipi: str | None = Field(default=None, description="Sigorta türü (Hayat, İşsizlik vb.)")
    sigorta_primi: str | None = Field(
        default=None, description="Sigorta primi / tutarı ve para birimi"
    )
    sigorta_suresi: str | None = Field(
        default=None, description="Sigortanın geçerlilik süresi veya bitiş tarihi"
    )
    sigorta_saglayan: str | None = Field(default=None, description="Sigorta şirketi adı")


class Masraflar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Krediye ilişkin ek masraflar (ekspertiz, vergiler vb.) bulunup bulunmadığını gösterir.",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    masraf_var: bool | None = Field(default=True, description="En az bir masraf varsa True")


class Masraf(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Her bir ek masraf kalemini tanımlar (örneğin dosya ücreti harici masraflar, vergiler).",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Masraflar,
    )
    masraf_adi: str = Field(description="Masrafın adı / türü")
    masraf_tutari: str = Field(description="Masraf tutarı ve para birimi")
    aciklama: str | None = Field(default=None, description="Ek açıklama veya şart")


class Kefiller(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi sözleşmesinde kefil olup olmadığını gösterir.",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    kefil_var: bool | None = Field(default=True, description="En az bir kefil varsa True")


class Kefil(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi sözleşmesinde yer alan her bir kefili (gerçek veya tüzel) tanımlar.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Kefiller,
    )
    kefil: Insan | Sirket | None = Field(
        default=None, description="Kefil olan kişi veya şirket bilgisi"
    )
    kefil_turu: str | None = Field(default=None, description="Kefil türü (Müteselsil, Sınırlı vb.)")
