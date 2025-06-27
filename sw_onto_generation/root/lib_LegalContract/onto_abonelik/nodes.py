from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import HowToExtract, NebulaIndexType, NodeFieldConfig, NodeModelConfig
from sw_onto_generation.common.common_nodes import Adres


class Taahhutname(BaseNode):
    """Taahhütname (commitment document) ana bilgilerini tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Taahhütname belgesi temel bilgilerini içerir. Taahhüt süresi, aktivasyon tarihi ve referans edilen sözleşmeler dahil.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    taahhut_suresi: str | None = Field(
        default=None,
        description="Taahhüt süresi (örn. '12 ay', '24 ay')",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    aktivasyon_tarihi: str | None = Field(
        default=None,
        description="Hizmet aktivasyon tarihi - fatura başlangıç tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    taahhutname_imza_tarihi: str | None = Field(
        default=None,
        description="Taahhütname imza tarihi, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    taahhutname_no: str | None = Field(
        default=None,
        description="Taahhütname referans numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    genel_aciklama: str | None = Field(default=None, description="Taahhütname genel açıklaması ve koşulları")


class EkSozlesmeler(BaseNode):
    """Taahhütname ile ilişkili ek sözleşmelerin varlığını belirtir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined node - Taahhütname ile ilişkili ek sözleşmeler var mı?",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    ek_sozlesme_var: bool = Field(default=True, description="En az bir ek sözleşme varsa True")


class EkSozlesme(BaseNode):
    """Taahhütname ile ilişkili her bir ek sözleşmeyi tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Taahhütname kapsamında referans edilen her bir ek sözleşme bilgisi",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=EkSozlesmeler,
    )

    sozlesme_adi: str = Field(description="Ek sözleşme adı (örn. 'DBS Ofis Güvenlik Duvarı Hizmetine İlişkin Ek Sözleşme')")
    sozlesme_tarihi: str | None = Field(
        default=None,
        description="Ek sözleşmenin imzalandığı tarih, YYYY-MM-DD formatında",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    sozlesme_aciklamasi: str | None = Field(default=None, description="Ek sözleşme kapsamı ve açıklaması")


class TaahhutKapsamiHizmetler(BaseNode):
    """Taahhüt kapsamında sunulan hizmetlerin varlığını belirtir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined node - Taahhüt kapsamında hizmetler var mı?",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    hizmet_var: bool = Field(default=True, description="En az bir hizmet varsa True")


class TaahhutKapsamiHizmet(BaseNode):
    """Taahhüt kapsamında sunulan her bir hizmeti tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Taahhüt kapsamında sunulan her bir hizmet (DBS, MPLS VPN, veri merkezi hizmetleri vb.)",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=TaahhutKapsamiHizmetler,
    )

    hizmet_adi: str = Field(description="Hizmet adı (örn. '4000 GB SAS', 'Fortigate VM01 UTM aylık', '50 Mbps MPLS VPN')")
    lokasyon_no: str | None = Field(
        default=None,
        description="Hizmet lokasyon numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    kapasite: str | None = Field(default=None, description="Hizmet kapasitesi (örn. '4000 GB', '50 Mbps', '77 Adet')")
    liste_fiyati_vergi_haric: str | None = Field(default=None, description="Liste fiyatı vergiler hariç (örn. '6.870,617 TL')")
    liste_fiyati_vergi_dahil: str | None = Field(default=None, description="Liste fiyatı vergiler dahil (örn. '8.244,74 TL')")
    indirimli_fiyat_vergi_haric: str | None = Field(default=None, description="İndirimli fiyat vergiler hariç (örn. '5.840,024 TL')")
    indirimli_fiyat_vergi_dahil: str | None = Field(default=None, description="İndirimli fiyat vergiler dahil (örn. '7.008,029 TL')")
    hizmet_aciklamasi: str | None = Field(default=None, description="Hizmet detaylı açıklaması")


class Donanimlar(BaseNode):
    """Taahhüt kapsamında donanım ve yatırım bilgilerinin varlığını belirtir."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined node - Donanım/yatırım bilgileri var mı?",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    bilgi_var: bool = Field(default=True, description="Donanım/yatırım bilgisi varsa True")


class Donanim(BaseNode):
    """Taahhüt kapsamında temin edilen donanımları tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Taahhüt kapsamında temin edilen donanım/ekipman bilgileri",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=Donanimlar,
    )

    hizmet_adi: str = Field(description="Donanımın kullanıldığı hizmet adı")
    donanim_marka_model: str = Field(description="Donanım marka/model bilgisi")
    adet: int | None = Field(default=None, description="Donanım adedi")
    bedel: str | None = Field(default=None, description="Donanım bedeli")
    aboneye_yansitilacak_bedel_vergi_haric: str | None = Field(default=None, description="Aboneye yansıtılacak bedel vergiler hariç")
    aboneye_yansitilacak_bedel_vergi_dahil: str | None = Field(default=None, description="Aboneye yansıtılacak bedel vergiler dahil")
    mulkiyet_durumu: str | None = Field(default=None, description="Donanımın mülkiyet durumu (Turkcell Superonline'a ait vs abone'ye ait)")


class TaahhutIhlalKosullari(BaseNode):
    """Taahhüt ihlali durumunda uygulanacak koşulları tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Taahhütten cayma, ihlal durumlarında uygulanacak koşul ve ceza bilgileri",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    ihlal_durumlari: str | None = Field(default=None, description="Taahhüt ihlali sayılan durumlar")
    cayma_bedeli_hesaplama: str | None = Field(default=None, description="Cayma bedeli hesaplama yöntemi")
    donanim_iade_kosullari: str | None = Field(default=None, description="Donanım iade koşulları")
    ek_tazminat_hakki: str | None = Field(default=None, description="Hizmet sağlayıcının ek tazminat hakları")
    odeme_kosullari: str | None = Field(default=None, description="Cayma bedeli ödeme koşulları")


# Legacy nodes - kept for compatibility


class AbonelikBedeli(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Abonelik için ödenecek periyodik ücret (aylık, yıllık vb.)",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    abonelik_bedeli: float = Field(description="Toplam vergiler dahil ücret miktarı (sayı)")
    para_birimi: str = Field(default="TL", description="Para birimi (TL, USD, EUR vb.)")
    odeme_periyodu: str = Field(default="Aylık", description="Ödeme periyodu (Aylık, Yıllık vb.)")
    odeme_yontemi: str | None = Field(default=None, description="Ödeme yöntemi (otomatik ödeme, kredi kartı, havale vb.)")
    indirim_aciklamasi: str | None = Field(default=None, description="Kampanya / indirim varsa açıklaması")
    taahhut_var_mi: bool | None = Field(default=None, description="Taahhüt var mı?")
    taahhut_sonrasi_bedel: str | None = Field(default=None, description="Taahhüt süresi sonunda geçerli olacak abonelik bedeli (örn. '200 TL')")


class CaymaBedeli(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="Taahhüt süresi dolmadan fesih hâlinde ödenecek cayma bedeli",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    cayma_bedeli: str = Field(description="Cayma bedeli miktarı ve para birimi")
    bedelin_hesaplama_yontemi: str | None = Field(default=None, description="Cayma bedelinin hesaplanma yöntemi")


class KurulumBedeli(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Başlangıçta ödenen kurulum / aktivasyon ücreti",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    kurulum_ucreti: str = Field(description="Kurulum ücreti (örn. '500 TL')")
    para_birimi: str = Field(default="TL", description="Para birimi (TL, USD, EUR vb.)")


class HizmetSeviyesi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Hız, kota, kesintisiz hizmet garantisi gibi parametreleri tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    hiz: str | None = Field(default=None, description="İnternet hızı (örn. '100 Mbps')")
    kota: str | None = Field(default=None, description="Aylık veri kotası / kWh vb.")
    kesinti_tazminati: str | None = Field(default=None, description="Hizmet kesintisi halinde uygulanacak tazminat")


class FaturaBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Abonelik kapsamında düzenlenen faturalara ilişkin temel bilgileri tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    fatura_kesim_tarihi: str | None = Field(default=None, description="Fatura kesim günü / tarihi")
    fatura_periyodu: str | None = Field(default="Aylık", description="Fatura periyodu (Aylık, 3-Aylık vb.)")
    fatura_adresi: Adres | None = Field(default=None, description="Faturaların gönderileceği adres")


class TaksitSecenegi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Abonelik bedelinin taksitlendirilmiş ödeme planını tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    taksit_sayisi: int | None = Field(default=None, description="Toplam taksit sayısı")
    taksit_tutari: str | None = Field(default=None, description="Her bir taksit tutarı (örn. '150 TL')")
    toplam_tutar: str | None = Field(default=None, description="Toplam tahsil edilecek tutar (taksitli)")


class EkUcretler(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Abonelik kapsamında ek / ilave ücret bulunup bulunmadığını gösterir.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    ek_ucret_var: bool | None = Field(default=True, description="En az bir ek ücret varsa True")


class EkUcret(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Abonelik kapsamında tahsil edilen her bir ek ücret kalemini tanımlar.""",
        nodetag_index=False,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=EkUcretler,
    )
    ucret_adi: str = Field(description="Ücretin adı / türü (örn. 'Damga Vergisi')")
    ucret_tutari: str = Field(description="Ücretin tutarı ve para birimi (örn. '18,90 TL')")
    aciklama: str | None = Field(default=None, description="Ek açıklama veya şart")


class KampanyaBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Aboneliğe uygulanan kampanya / promosyon detaylarını tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    kampanya_adi: str | None = Field(default=None, description="Kampanyanın adı")
    kampanya_suresi: str | None = Field(default=None, description="Kampanyanın geçerli olduğu süre (örn. '6 Ay')")
    indirim_orani: str | None = Field(default=None, description="İndirim oranı veya tutarı (örn. '%20', '50 TL')")
    kampanya_aciklama: str | None = Field(default=None, description="Kampanya ile ilgili ek açıklama")


class BildirimBilgisi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Aboneye yapılacak bildirimlerin yöntemi ve adres bilgilerini tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    bildirim_metodu: str | None = Field(default=None, description="Bildirim yöntemi (SMS, E-posta, Posta vb.)")
    bildirim_adresi: str | None = Field(default=None, description="Bildirimlerin gönderileceği adres / numara")
    tercih_edilen_kanal: str | None = Field(default=None, description="Abonenin tercih ettiği iletişim kanalı")


class GecikmeFaizi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Ödemelerin gecikmesi hâlinde uygulanacak faiz / ceza bilgilerini tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    faiz_orani: str | None = Field(default=None, description="Gecikme faiz oranı (örn. '%1,5')")
    hesaplama_yontemi: str | None = Field(default=None, description="Faizin hesaplanma yöntemi (günlük, aylık vb.)")
    aciklama: str | None = Field(default=None, description="Ek açıklama veya şartlar")


class ServisKesinti(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Hizmet kesintisi hâlinde uygulanacak prosedür ve tazminat bilgilerini tanımlar.""",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    kesinti_sartlari: str | None = Field(default=None, description="Kesinti gerçekleştiğinde geçerli şartlar")
    tazminat_miktari: str | None = Field(default=None, description="Kesinti durumunda ödenecek tazminat (örn. '1 günlük ücret')")
    para_birimi: str | None = Field(default=None, description="Tazminat para birimi (TL, USD, EUR vb.)")
