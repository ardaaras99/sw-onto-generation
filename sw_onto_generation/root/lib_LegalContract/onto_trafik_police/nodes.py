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
        description="SBM BimRefNo",
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


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    teminat_var: bool = Field(default=False, description="En az bir teminat varsa True, yoksa zaten yaratilmaz.")


class Teminat(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin icerisnde her hangi bir konuda bir veya birden fazla teminat alinmis olabilir. Teminat tipleri olarak banka teminat mektubu, banka hesap blokesi, altin, doviz, para sayabiliriz.. Depozito olarak da teminat istenmis olabilir. her birini ayri bir node olarak tanimlayin.",
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
    indirim_var: bool = Field(default=False, description="En az bir indirim varsa True, yoksa zaten yaratilmaz.")


class Indirim(BaseNode):
    """Discount and surcharge node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta priminde uygulanan indirim ve artışları tanımlar. Hasarsızlık indirimi, yaş artışı vb.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    indirim_artis_turu: str = Field(description="İndirim/artış türü (HASARSIZLIK İNDİRİMİ, DEPREM ARTIRIMI, Yaş, Tecrübe, vb.)")
    oran: str | None = Field(
        default=None,
        description="İndirim/artış oranı (örn. %65, %3, 50)",
    )
    tutar: str | None = Field(
        default=None,
        description="İndirim/artış tutarı ve para birimi",
    )
    aciklama: str | None = Field(
        default=None,
        description="İndirim/artış açıklaması",
    )
