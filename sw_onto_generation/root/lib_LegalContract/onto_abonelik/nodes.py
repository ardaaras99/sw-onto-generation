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


class AbonelikHizmeti(BaseNode):
    """Aboneliğin konusunu – hangi hizmetin sağlandığını – tanımlar."""

    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="""Bu bir internet, telefon, elektrik, su, dijital içerik vb. hizmet olabilir.
        Tarife / paket adı, hizmet hızı, kota veya kanal sayısı gibi bilgiler içerebilir.""",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    hizmet_turu: str = Field(
        description="Hizmet türü (internet, mobil, elektrik vb.)",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    tarife_adi: str | None = Field(default=None, description="Tarife veya paket adı (Örn. 'Fiber 100 Mbps')")
    hizmet_aciklamasi: str | None = Field(default=None, description="Hizmetin detaylı açıklaması / kapsamı")
    hizmet_adresi: Adres | None = Field(
        default=None,
        description="Hizmetin sağlandığı adres (sabit hizmetler için). Mobil hizmetlerde boş bırakılabilir.",
    )
    abonelik_no: str = Field(
        description="Abone / müşteri numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


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


class Ekipmanlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="Abonelik kapsamında kullanıcıya tahsis edilen cihaz/donanım var mı?",
        nodetag_index=False,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    ekipman_var: bool | None = Field(default=True, description="En az bir ekipman varsa True")


class Ekipman(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        description="""Abonelik ile verilen modem, router, set‑top box, sayaç vb. gibi her bir cihazı tanımlar.""",
        nodetag_index=False,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=Ekipmanlar,
    )
    ekipman_adi: str = Field(description="Cihaz adı / modeli (örn. 'ZXHN H298A Modem')")
    seri_no: str | None = Field(default=None, description="Seri numarası veya IMEI vb.")
    depozito: str | None = Field(default=None, description="Cihaz için alınan depozito / teminat (örn. '300 TL')")
    aciklama: str | None = Field(default=None, description="Cihaz ile ilgili ek açıklama")


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
