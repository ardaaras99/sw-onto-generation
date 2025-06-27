from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import HowToExtract, NebulaIndexType, NodeFieldConfig, NodeModelConfig
from sw_onto_generation.common.common_nodes import Sirket


class TrafikPolice(BaseNode):
    """Trafik sigortası poliçesinin temel bilgilerini tanımlar. Poliçe numarası, türü, süresi, tanzim tarihi gibi ana bilgileri içerir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Trafik poliçesinin temel bilgilerini tanımlar. Poliçe numarası, türü, süresi, tanzim tarihi gibi ana bilgileri içerir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    police_no: str | None = Field(
        default=None,
        description="Trafik poliçe numarası. Örnek: 1152176523",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    urun_kodu: str | None = Field(
        default=None,
        description="Ürün kodu (örn. T41 trafik sigortası)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    tanzim_tarihi: str | None = Field(
        default=None,
        description="Poliçenin tanzim (düzenleme) tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    basim_tarihi: str | None = Field(
        default=None,
        description="Poliçenin basım tarihi ve saati",
    )
    toplam_sayfa_sayisi: int | None = Field(
        default=None,
        description="Toplam sayfa sayısı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    cografi_siniri: str | None = Field(
        default=None,
        description="Coğrafi sınırları belirtir.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    hasarsızlık_basamak: str | None = Field(
        default=None,
        description="Hasarsızlık basamaklarını belirtir. Örnek: 1. Basamak, 2. Basamak, 3. Basamak",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Acente(Sirket):
    """Insurance agent information node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta acentesi bilgilerini tanımlar. Poliçeyi düzenleyen acente veya broker bilgileri.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    acente_no: str | None = Field(
        default=None,
        description="Acente numarası (örn. 700053, 311000349810734, 5103)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    acente_levha_no: str | None = Field(
        default=None,
        description="Acente levha numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    acente_kodu: str | None = Field(
        default=None,
        description="Acente kodu",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Arac(BaseNode):
    """Araç bilgilerini tanımlar. Araç plakası, markası, modeli, sürücü dahil koltuk sayısı gibi bilgileri içerir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Araç sigortalarında araç bilgilerini tanımlar. Trafik sigortası için kullanılır.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    plaka_no: str | None = Field(
        default=None,
        description="Araç plakası. Örnek: 34 ABC 123",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    marka: str | None = Field(
        default=None,
        description="Araç markası (örn. BMW, Mercedes, Renault)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    model_adi: str | None = Field(
        default=None,
        description="Araç model adı (örn. 525D, C180, Megane)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    donanim_paketi: str | None = Field(
        default=None,
        description="Araç donanım paketi veya serisi (örn. EXECUTIVE, PRESTIGE, SPORTLINE)",
    )
    kasa_tipi: str | None = Field(
        default=None,
        description="Araç kasa tipi (örn. SEDAN, HATCHBACK, SUV)",
    )
    motor_hacmi: str | None = Field(
        default=None,
        description="Motor hacmi veya silindir hacmi (örn. 2.0, 1.6, 1.5)",
    )
    motor_gucu: str | None = Field(
        default=None,
        description="Motor gücü (örn. 218 HP, 136 HP)",
    )
    cekis_tipi: str | None = Field(
        default=None,
        description="Çekiş tipi (örn. XDRIVE, 4MATIC, Önden Çekiş, Arkadan İtiş)",
    )
    marka_butun_bilgi: str | None = Field(
        default=None,
        description="Araç markası ve tip bilgisi (örn. BMW 525D XDRIVE SEDAN 2.0 (218) EXECUTIVE)",
    )
    kullanim_tarzi: str | None = Field(
        default=None,
        description="Araç kullanım tarzi",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    motor_no: str | None = Field(
        default=None,
        description="Araç motor numarası (örn. 64286741762987)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sasi_no: str | None = Field(
        default=None,
        description="Araç şasi numarası (örn. WDD2421231A234764)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    koltuk_sayisi: int | None = Field(
        default=None,
        description="Araç toplam koltuk sayısı",
    )
    yer_adedi: str | None = Field(
        default=None,
        description="Araç yer adedi (örn. 4+1)",
    )
    trafik_tescil_tarihi: str | None = Field(
        default=None,
        description="Trafik tescil tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sbm_bimref_no: str | None = Field(
        default=None,
        description="SBM BimRefNo, Sig Bilgi İşlem Merkezi Referans Numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sbm_tramer_no: str | None = Field(
        default=None,
        description="SBM Tramer numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    trafik_cikis_tarihi: str | None = Field(
        default=None,
        description="Trafik çıkış tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    yakit_tipi: str | None = Field(
        default=None,
        description="Araç yakıt tipi (örn. Benzin, Dizel, Elektrik, vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    teminat_var: bool = Field(default=True, description="En az bir teminat varsa True, yoksa zaten yaratilmaz.")


class Teminat(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin icerisnde herhangi bir konuda bir veya birden fazla teminat alinmis olabilir. Kişi, kaza, olay ve yillik teminatlar olabilir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=Teminatlar,
    )

    teminat_adi: str = Field(description="Teminat adı (Maddi Hasar Araç Başına, Ölüm ve Sakatlanma Kişi Başına, Cam Kırılması, vb.)")
    teminat_tutari: str | None = Field(
        default=None,
        description="Teminat tutarı ve para birimi (örn. 200,000.00 TL, 1,800,000.00 TL, Rayiç Değer)",
    )
    teminat_tipi: str | None = Field(
        default=None,
        description="Teminat tipi (Ana Teminat, Ek Teminat, Hizmet, vb.)",
    )
    fiyat_yuzdesi: str | None = Field(
        default=None,
        description="Fiyat yüzdesi bilgisi",
    )
    prim_tutari: str | None = Field(
        default=None,
        description="Bu teminat için hesaplanan prim tutarı",
    )
    muafiyet: str | None = Field(
        default=None,
        description="Muafiyet tutarı ve para birimi",
    )
    kisitlama: str | None = Field(
        default=None,
        description="Teminat kısıtlaması (15 Gün - 2 Defa, %25 kesinti vb.)",
    )
    aciklama: str | None = Field(
        default=None,
        description="Teminat açıklaması ve özel koşulları",
    )


class SigortaPrimi(BaseNode):
    """Insurance premium node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta primi ve ödeme bilgilerini tanımlar. Prim tutarı, vergi, harç bilgilerini içerir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    net_prim: str | None = Field(
        default=None,
        description="Net prim tutarı ve para birimi (örn. 4,644.63 TL, 65,778.70 TL)",
    )
    sgk_payi: str | None = Field(
        default=None,
        description="SGK payı tutarı (örn. 464.46 TL, 644.74 TL)",
    )
    bsmv: str | None = Field(
        default=None,
        description="BSMV (Banka ve Sigorta Muameleleri Vergisi) tutarı (örn. 3,288.94 TL)",
    )
    gider_vergisi: str | None = Field(
        default=None,
        description="Gider vergisi tutarı (örn. 232.23 TL, 462.07 TL)",
    )
    thg_fonu: str | None = Field(
        default=None,
        description="Trafik Hizmetleri Geliştirme Fonu tutarı (örn. 232.23 TL, 322.37 TL)",
    )
    ghkp: str | None = Field(
        default=None,
        description="Güvence Hesabı Karşılık Payı tutarı (örn. 92.89 TL)",
    )
    guvence_hesabi: str | None = Field(
        default=None,
        description="Güvence Hesabı tutarı (örn. 128.95 TL)",
    )
    yangin_vergisi: str | None = Field(
        default=None,
        description="Yangın vergisi tutarı",
    )
    toplam_brut_prim: str | None = Field(
        default=None,
        description="Toplam brüt prim tutarı (örn. 5,201.98 TL, 69,067.64 TL, 10,584.56 TL)",
    )
    odenecek_prim: str | None = Field(
        default=None,
        description="Ödenecek prim (toplam ödenecek) tutarı ve para birimi",
    )
    odeme_sekli: str | None = Field(
        default=None,
        description="Ödeme şekli (Peşin, Taksitli, vb.)",
    )
    taksit_sayisi: int | None = Field(
        default=None,
        description="Taksit sayısı",
    )


class Indirimler(BaseNode):
    """Indirimler node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    indirim_var: bool = Field(default=True, description="En az bir indirim varsa True, yoksa zaten yaratilmaz.")


class Indirim(BaseNode):
    """Discount node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta priminde uygulanan indirimleri tanımlar. Hasarsızlık indirimi, meslek indirimi vb.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    indirim_turu: str = Field(description="İndirim türü (HASARSIZLIK İNDİRİMİ, vb.)")
    oran: str | None = Field(
        default=None,
        description="İndirim oranı (örn. %65, %3, 50)",
    )
    tutar: str | None = Field(
        default=None,
        description="İndirim tutarı ve para birimi",
    )
    aciklama: str | None = Field(
        default=None,
        description="İndirim açıklaması",
    )


class Artirimlar(BaseNode):
    """Artırımlar node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    artirim_var: bool = Field(default=True, description="En az bir artırım varsa True, yoksa zaten yaratilmaz.")


class Artirim(BaseNode):
    """Artırım node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta priminde uygulanan artırımları tanımlar. Deprem artırımı vb.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    artirim_turu: str = Field(description="Artırım türü (DEPREM ARTIRIMI, vb.)")
    oran: str | None = Field(
        default=None,
        description="Artırım oranı (örn. %65, %3, 50)",
    )
    aciklama: str | None = Field(
        default=None,
        description="Artırım açıklaması",
    )


class Istisnalar(BaseNode):
    """Istisnalar node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    istisna_var: bool = Field(default=True, description="En az bir istisna varsa True, yoksa zaten yaratilmaz.")


class Istisna(BaseNode):
    """Istisna node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta poliçesinde uygulanan istisnaları tanımlar. Bu istisnalar primi azaltabilir, teminat kapsamını sınırlayabilir. Alkollü araba kullanımı, sürücü belgesiz araç kullanımı vb.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    istisna_turu: str = Field(description="Istisna türü (ALKOLLU ARABA KULLANIMI, vb.)")
    açıklama: str | None = Field(
        default=None,
        description="Istisna açıklaması",
    )


class EkKlozlar(BaseNode):
    """Ek klozlar node. Bu klozlar poliçe için ek koşulları belirtir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    ek_kloz_var: bool = Field(default=True, description="En az bir ek kloz varsa True, yoksa zaten yaratilmaz.")


class EkKloz(BaseNode):
    """Ek kloz node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Ek klozlar node. Bu klozlar poliçe için ek koşulları belirtir. ",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    ek_kloz_adi: str = Field(description="Ek kloz adı")
    ek_kloz_aciklama: str | None = Field(
        default=None,
        description="Ek kloz açıklaması. Bu açıklamalar poliçe için ek koşulları belirtir.",
    )
