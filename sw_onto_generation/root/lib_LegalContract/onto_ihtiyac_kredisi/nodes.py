from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import (
    HowToExtract,
    NebulaIndexType,
    NodeFieldConfig,
    NodeModelConfig,
)


class KrediTutari(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi sözleşmesinde belirtilen toplam kredi tutarını tanımlar. Tutar mutlaka para birimi ile birlikte yazılmalıdır.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    kredi_tutari: float | None = Field(default=None, description="Kredi tutarı (sayı)")
    para_birimi: str | None = Field(
        default=None,
        description="Para birimi (TL, USD, EUR vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    aciklama: str | None = Field(default=None, description="Tutarla ilgili ek açıklama veya şartlar")


class FaizBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Krediye uygulanacak faiz oranı ve hesaplama yöntemini tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    faiz_orani: str | None = Field(default=None, description="Faiz oranı (örn. '%1,89 aylık', 'Yıllık %23,5')")
    faiz_turu: str | None = Field(
        default=None,
        description="Faiz türü (Sabit, Değişken, Azalan vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    faiz_hesaplama_yontemi: str | None = Field(default=None, description="Faizin nasıl hesaplanacağı (basit, bileşik vb.)")
    faiz_aciklama: str | None = Field(default=None, description="Faizle ilgili ek açıklamalar veya koşullar")


class VadeBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin vadesi / toplam geri ödeme süresini tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
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
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    taksit_sayisi: int | None = Field(default=None, description="Toplam taksit sayısı")
    taksit_tutari: str | None = Field(default=None, description="Her taksit tutarı ve para birimi (örn. '1.250 TL')")
    odeme_periyodu: str | None = Field(
        default="Aylık",
        description="Ödeme periyodu (Aylık vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    ilk_odeme_tarihi: str | None = Field(
        default=None,
        description="İlk taksit tarihi (YYYY-MM-DD)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    son_odeme_tarihi: str | None = Field(
        default=None,
        description="Son taksit tarihi (YYYY-MM-DD)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class KrediAmaci(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin kullanım amacını (ihtiyaç, tatil, eğitim, sağlık vb.) tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    kredi_amaci: str | None = Field(default=None, description="Kredinin kullanım amacı")


class TahsisUcreti(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi tahsis / dosya ücreti bilgilerini tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    tahsis_ucreti: str | None = Field(default=None, description="Tahsis ücreti ve para birimi (örn. '420 TL')")


class ErkenOdemeCezasi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredinin erken kapatılması hâlinde uygulanacak ücret veya ceza bilgisini tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    ceza_tutari: str | None = Field(default=None, description="Erken ödeme cezası (örn. '%2', '350 TL'), yoksa None")
    aciklama: str | None = Field(default=None, description="Cezayla ilgili ek açıklama veya şartlar")


class SigortaBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi kapsamında yaptırılan hayat, işsizlik veya ferdi kaza sigortası detaylarını tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    sigorta_tipi: str | None = Field(
        default=None,
        description="Sigorta türü (Hayat, İşsizlik vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sigorta_primi: str | None = Field(default=None, description="Sigorta primi / tutarı ve para birimi")
    sigorta_suresi: str | None = Field(default=None, description="Sigortanın geçerlilik süresi veya bitiş tarihi")
    sigorta_saglayan: str | None = Field(default=None, description="Sigorta şirketi adı")


class Masraflar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Krediye ilişkin ek masraflar (ekspertiz, vergiler vb.) bulunup bulunmadığını gösterir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    masraf_var: bool | None = Field(default=True, description="En az bir masraf varsa True")


class Masraf(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Her bir ek masraf kalemini tanımlar (örneğin dosya ücreti harici masraflar, vergiler).",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=Masraflar,
    )
    masraf_adi: str = Field(description="Masrafın adı / türü, BSMV, KKDF, Ekspertiz vb.")
    masraf_tutari: str = Field(description="Masraf tutarı ve para birimi")
    aciklama: str | None = Field(default=None, description="Ek açıklama veya şart")


class TemerrutBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Ödeme gecikmesi (temerrüt) halinde uygulanacak hükümleri tanımlar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    temerrut_hali: str | None = Field(default="Taksidin vadesinde ödenmemesi", description="Temerrüdün ne zaman doğacağı")
    temerrut_faiz_orani: str | None = Field(default=None, description="Akdi faiz + %30 sınırı içindeki gecikme faizi oranı")
    bildirim_suresi_gun: int | None = Field(default=30, description="Muacceliyet bildirimi için tanınan süre (gün)")
    hukuki_sonuclar: str | None = Field(default=None, description="İcra takibi, rehin paraya çevirme vb.")


class CaymaHakki(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Kredi kullanımından cayma koşulları",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    sure_gun: int = Field(14, description="Kanuni cayma süresi (gün)")
    faiz_ve_vergiler_odenir_mi: bool = Field(True, description="Cayarken akdi faiz + ödenmiş vergiler iade edilir mi?")
    iade_suresi_gun: int = Field(30, description="Anapara + işleyen faizin bankaya iade edilme süresi")
    ek_masraf_var_mi: bool = Field(False, description="Kanun gereği ek tazminat / cezai şart doğar mı?")


class TeminatBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Rehin, ipotek veya kefalet gibi teminat bilgileri",
        cardinality=True,  # Bir sözleşmede birden fazla teminat olabilir
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    teminat_turu: str = Field(
        description="Taşıt Rehni | İpotek | Kefalet | Teminatsız",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    teminat_detayi: str | None = Field(default=None, description="Araç plakası, tapu bilgisi, kefil TCKN vb.")
    teminat_tutari: str | None = Field(default=None, description="Teminat kapsamındaki azami tutar ve birim")
