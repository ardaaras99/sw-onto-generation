from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import (
    HowToExtract,
    NebulaIndexType,
    NodeFieldConfig,
    NodeModelConfig,
)
from sw_onto_generation.common.common_nodes import Adres


class SigortaPolice(BaseNode):
    """Insurance policy core information node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta poliçesinin temel bilgilerini tanımlar. Poliçe numarası, türü, süresi, tanzim tarihi gibi ana bilgileri içerir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    police_no: str | None = Field(
        default=None,
        description="Sigorta poliçe numarası. Benzersiz tanımlayıcı numara (örn. 0001-0210-61749616, 700067, 301000175277833)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sigorta_turu: str | None = Field(
        default=None,
        description="Sigorta türü (Kasko, Trafik, Konut, Hayat, Sağlık, vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    urun_kodu: str | None = Field(
        default=None,
        description="Ürün kodu (örn. T41 trafik sigortası için, MPSPO009 kasko için)",
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
    police_baslangic_tarihi: str | None = Field(
        default=None,
        description="Poliçenin başlangıç tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    police_bitis_tarihi: str | None = Field(
        default=None,
        description="Poliçenin bitiş tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sure_gun: int | None = Field(
        default=None,
        description="Poliçe süresi gün cinsinden (örn. 365)",
    )
    eski_police_no: str | None = Field(
        default=None,
        description="Önceki poliçe numarası (örn. 1152176523)",
    )
    onceki_sigorta_sirketi: str | None = Field(
        default=None,
        description="Önceki sigorta şirketi adı (örn. ANADOLU SİGORTA)",
    )
    yenileme_no: str | None = Field(
        default=None,
        description="Yenileme numarası",
    )
    ek_no: str | None = Field(
        default=None,
        description="Ek (zeyil) numarası",
    )
    sayfa_no: str | None = Field(
        default=None,
        description="Sayfa numarası bilgisi (örn. 1/1, 1/11)",
    )


class SigortaliKisi(BaseNode):
    """Insured person or entity node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigortalı kişi veya kuruluşun bilgilerini tanımlar. Sigorta kapsamına alınan tarafı belirtir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    musteri_no: str | None = Field(
        default=None,
        description="Müşteri numarası (örn. 9040423, 23418368)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sigorta_ettiren_mi: bool | None = Field(
        default=None,
        description="Bu kişinin aynı zamanda sigorta ettiren olup olmadığı",
    )
    sigorta_konusu_ile_iliskisi: str | None = Field(
        default=None,
        description="Sigortalının sigorta konusu ile ilişkisi (Mal sahibi, Sürücü, Kiracı, vb.)",
    )
    diger_hak_sahipleri: str | None = Field(
        default=None,
        description="Diğer hak sahipleri bilgisi",
    )


class SigortaEttiren(BaseNode):
    """Insurance contractor node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta ettiren kişi veya kuruluşun bilgilerini tanımlar. Sigorta sözleşmesini yapan taraftır.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    odemeden_sorumlu_mu: bool | None = Field(
        default=True,
        description="Sigorta ettiren ödeme sorumluluğuna sahip mi",
    )


class SigortaSirketi(BaseNode):
    """Insurance company node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta şirketinin bilgilerini tanımlar. Sigorta hizmetini veren kuruluştur.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    kurulus_yeri: str | None = Field(
        default=None,
        description="Poliçenin düzenlendiği yer (örn. ANKARA)",
    )
    merkez_adresi: str | None = Field(
        default=None,
        description="Şirket merkez adresi (örn. Allianz Tower Küçükbakkalköy Mah. Kayışdağı Cad. No:1 Ataşehir/İstanbul)",
    )
    kayitli_sermaye: str | None = Field(
        default=None,
        description="Kayıtlı sermaye tutarı (örn. 500 Milyon TL)",
    )
    cikarilmis_sermaye: str | None = Field(
        default=None,
        description="Çıkarılmış sermaye tutarı (örn. 306 Milyon TL)",
    )
    kurucusu: str | None = Field(
        default=None,
        description="Şirketin kurucusu (örn. Akbank)",
    )
    buyuk_mukellefler_vd: str | None = Field(
        default=None,
        description="Büyük Mükellefler Vergi Dairesi numarası (örn. 8000013270)",
    )
    ticaret_sicil_no: str | None = Field(
        default=None,
        description="Ticaret sicil numarası (örn. 6022)",
    )
    mersis_no: str | None = Field(
        default=None,
        description="Mersis numarası (örn. 0-8000-0132-7000012)",
    )
    hizmet_merkezi_tel: str | None = Field(
        default=None,
        description="Hizmet merkezi telefon numarası (örn. 0850 399 99 99)",
    )
    website: str | None = Field(
        default=None,
        description="Şirket web sitesi (örn. www.allianzsigorta.com.tr)",
    )


class Acente(BaseNode):
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
    acente_unvani: str | None = Field(
        default=None,
        description="Acente ünvanı (örn. ZORLU SİGORTA VE REASÜRANS BROKERLİĞİ A.Ş.)",
    )
    levha_kayit_no: str | None = Field(
        default=None,
        description="Levha kayıt numarası (örn. BR888-39965)",
    )
    telefon: str | None = Field(
        default=None,
        description="Acente telefon numarası (örn. 3122127779)",
    )
    faks: str | None = Field(
        default=None,
        description="Acente faks numarası (örn. 3122157337)",
    )
    teknik_personel_adi: str | None = Field(
        default=None,
        description="Teknik personel adı soyadı (örn. GÖNÜL DİVİ)",
    )
    teknik_personel_kayit_no: str | None = Field(
        default=None,
        description="Teknik personel kayıt numarası (örn. 090-TP-011)",
    )


class SigortaKonusu(BaseNode):
    """Subject of insurance node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta konusunu tanımlar. Sigortalanan mal, eşya veya risk alanını belirtir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    konu_turu: str | None = Field(
        default=None,
        description="Sigorta konusunun türü (Araç, Konut, Ticari Mal, vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    konu_aciklamasi: str | None = Field(
        default=None,
        description="Sigorta konusunun detaylı açıklaması",
    )
    deger: str | None = Field(
        default=None,
        description="Sigorta konusunun değeri ve para birimi",
    )
    adres: Adres | None = Field(
        default=None,
        description="Sigorta konusunun bulunduğu adres",
    )


class Arac(BaseNode):
    """Vehicle information node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Araç sigortalarında araç bilgilerini tanımlar. Kasko ve trafik sigortası için kullanılır.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    plaka: str | None = Field(
        default=None,
        description="Araç plakası (örn. 06 FC9481, 34 NV 5754)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    marka_tip: str | None = Field(
        default=None,
        description="Araç markası ve tip bilgisi (örn. MERCEDES S 350 BLUETEC 4MATIC LONG, BMW 525D XDRIVE SEDAN)",
    )
    model: str | None = Field(
        default=None,
        description="Araç model yılı (örn. 2015, 1968)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    kullanim_sekli: str | None = Field(
        default=None,
        description="Araç kullanım şekli (örn. OTOMOBİL, OTOMOBİL (SÜRÜCÜ DAHİL 9 KOLTUK))",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    kullanim_tarzi: str | None = Field(
        default=None,
        description="Araç kullanım tarzı detayı (örn. Özel otomobil)",
    )
    motor_no: str | None = Field(
        default=None,
        description="Araç motor numarası (örn. 64286741762987, 12998212002036)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sasi_no: str | None = Field(
        default=None,
        description="Araç şasi numarası (örn. WDD2221331A230764, 11304312004054)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    koltuk_sayisi: int | None = Field(
        default=None,
        description="Araç koltuk sayısı",
    )
    yer_adedi: str | None = Field(
        default=None,
        description="Araç yer adedi (örn. 4+1)",
    )
    trafik_tescil_tarihi: str | None = Field(
        default=None,
        description="Trafik tescil tarihi (örn. 11/11/2013, 23/08/2022)",
    )
    egm_marka_bilgisi: str | None = Field(
        default=None,
        description="EGM marka bilgisi (örn. MERCEDES-BENZ)",
    )
    egm_model_yili: str | None = Field(
        default=None,
        description="EGM model yılı (örn. 1968)",
    )
    ruhsat_ikametgah: str | None = Field(
        default=None,
        description="Ruhsat/ikametgah bilgisi (örn. 34 - MALTEPE)",
    )
    sbm_bimref_no: str | None = Field(
        default=None,
        description="SBM BimRefNo (örn. inm6a89Rclefxmix8ewOoGQXyVmioqQD8ko9W+QjiHw=)",
    )
    sbm_tramer_no: str | None = Field(
        default=None,
        description="SBM Tramer numarası (örn. 695453130, 732131842)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    hasarsizlik_basamagi: str | None = Field(
        default=None,
        description="Hasarsızlık/hasarlılık basamağı (örn. 8. KADEME, 8)",
    )
    arac_degeri: str | None = Field(
        default=None,
        description="Aracın sigorta değeri ve para birimi",
    )
    standart_disi_aksesuar: str | None = Field(
        default=None,
        description="Standart dışı aksesuar bilgisi ve değeri",
    )


class TeminatKapsami(BaseNode):
    """Coverage scope node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta kapsamında sağlanan teminatları tanımlar. Hangi risklerin kapsama dahil olduğunu belirtir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
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

    trafik_primi: str | None = Field(
        default=None,
        description="Trafik primi tutarı (örn. 4,180.17 TL, 5,802.70 TL)",
    )
    net_prim: str | None = Field(
        default=None,
        description="Net prim tutarı ve para birimi (örn. 4,644.63 TL, 65,778.70 TL)",
    )
    ek_teminat_prim: str | None = Field(
        default=None,
        description="Ek teminat primi (örn. 3,223.73 TL)",
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
    pesin_orani: str | None = Field(
        default=None,
        description="Peşin ödeme oranı",
    )


class Hasarkaydi(BaseNode):
    """Damage history node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta geçmişindeki hasar kayıtlarını tanımlar. Önceki hasarlar ve ödenen tazminatları içerir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    hasar_tarihi: str | None = Field(
        default=None,
        description="Hasar tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    hasar_tutari: str | None = Field(
        default=None,
        description="Hasar tutarı ve para birimi",
    )
    hasar_aciklamasi: str | None = Field(
        default=None,
        description="Hasar açıklaması ve detayları",
    )
    odenen_tazminat: str | None = Field(
        default=None,
        description="Ödenen tazminat tutarı ve para birimi",
    )
    hasar_durumu: str | None = Field(
        default=None,
        description="Hasar durumu (Kapalı, Açık, İncelenmede, vb.)",
    )


class IndirimArtis(BaseNode):
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


class OzelSart(BaseNode):
    """Special conditions node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta poliçesindeki özel şart ve hükümleri tanımlar. Standart dışı koşulları içerir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    sart_adi: str = Field(description="Özel şart adı veya kodu")
    sart_aciklamasi: str | None = Field(
        default=None,
        description="Özel şartın detaylı açıklaması",
    )
    sart_turu: str | None = Field(
        default=None,
        description="Özel şart türü (Teminat Kısıtlaması, Muafiyet, İstisna, vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    gecerlilik_kosulu: str | None = Field(
        default=None,
        description="Özel şartın geçerlilik koşulu",
    )


class AciklamaVeOzelSartlar(BaseNode):
    """General explanations and special conditions node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Poliçedeki genel açıklamalar ve özel şartları tanımlar. Genel şartlar, klozlar ve diğer hukuki metinleri içerir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    genel_aciklama: str | None = Field(
        default=None,
        description="Genel açıklama metni",
    )
    temerrut_hukmu: str | None = Field(
        default=None,
        description="Prim ödeme borcunda temerrüt ile ilgili hükümler",
    )
    ktk_hukmu: str | None = Field(
        default=None,
        description="KTK (Karayolları Trafik Kanunu) ile ilgili hükümler",
    )
    kvkk_aydinlatma: str | None = Field(
        default=None,
        description="KVKK (Kişisel Verilerin Korunması Kanunu) aydınlatma beyanı",
    )
    hasar_bildirim_hatsi: str | None = Field(
        default=None,
        description="Hasar bildirim hattı numarası (örn. 0850 250 8181)",
    )
    eksper_atama_klozu: str | None = Field(
        default=None,
        description="Eksper atama ile ilgili kloz",
    )
    diger_hukumler: str | None = Field(
        default=None,
        description="Diğer özel hükümler ve klozlar",
    )


class Lehtar(BaseNode):
    """Beneficiary node."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Sigorta lehdarını tanımlar. Özellikle hayat sigortası ve rehinli araçlarda önemlidir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    lehtar_turu: str | None = Field(
        default=None,
        description="Lehtar türü (Banka, Kişi, Kuruluş, vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    lehtar_payi: str | None = Field(
        default=None,
        description="Lehtarın payı (Tam, %50, vb.)",
    )
    lehtar_aciklamasi: str | None = Field(
        default=None,
        description="Lehtar ile ilgili açıklama",
    )
