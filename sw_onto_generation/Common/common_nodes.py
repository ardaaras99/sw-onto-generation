from typing import ClassVar

from pydantic import Field

from sw_onto_generation.Base.base_node import BaseNode
from sw_onto_generation.Base.configs import FieldConfig, NebulaIndexType, NodeModelConfig


class GeneralDocumentInfo(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="GeneralDocumentInfo",
        description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
        cardinality=False,
        field_configs=[FieldConfig(field_name="documan_ismi", search_type=NebulaIndexType.VECTOR)],
    )

    documan_ismi: str = Field(description="Belgenin başlığı")


class Adres(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Adres",
        description="Adres bilgilerini tanımlar. Adres, cadde, sokak, mahalle, apartman, ilçe, il ve posta kodu gibi bilgileri içerebilir.",
        cardinality=True,
        field_configs=[
            FieldConfig(field_name="il", search_type=NebulaIndexType.EXACT),
            FieldConfig(field_name="ilçe", search_type=NebulaIndexType.EXACT),
        ],
    )

    cadde: str = Field(description="Adresin cadde veya sokak adı")
    mahalle: str = Field(description="Adresin bulunduğu mahalle")
    apartman: str = Field(description="Adresin bulunduğu apartman adi veya numarasi veya kapi numarası veya her ikisi de olabilir")
    kat: str | None = Field(default=None, description="Adresin bulunduğu kat numarası, apartman içinde kat bilgisi")
    kapi_no: str | None = Field(default=None, description="Adresin bulunduğu kapı numarası, apartman içinde kapı bilgisi")
    ilçe: str = Field(description="Adresin bulunduğu ilçe")
    il: str = Field(description="Adresin bulunduğu il")
    ulke: str = Field(description="Adresin bulunduğu ülke, Türkiye için 'Türkiye' veya 'T.C.' gibi değerler olabilir")
    posta_kodu: str = Field(description="Adresin posta kodu")
    ada: str | None = Field(default=None, description="adreste belirtilmisse kadastro ada bilgisini icerir")
    parsel: str | None = Field(default=None, description="adreste belirtilmisse kadastro parsel bilgisini icerir")


class Insan(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Insan",
        description="Döküman icinde bulunan gercek kisileri yani insanlari tanimlar. Bu insanlar, sözleşmeyi imzalayan veya sözleşmede adı geçen gerçek kişilerdir.",
        cardinality=True,
        field_configs=[
            FieldConfig(field_name="tckn", search_type=NebulaIndexType.EXACT),
            FieldConfig(field_name="soyad", search_type=NebulaIndexType.EXACT),
            FieldConfig(field_name="ad", search_type=NebulaIndexType.EXACT),
        ],
    )

    ad: str = Field(description="İnsanın adı")
    soyad: str = Field(description="İnsanın soyadı")
    tckn: str | None = Field(default=None, description="İnsanın T.C. kimlik numarası, Türkiye Cumhuriyeti vatandaşları için geçerlidir")
    uyruk: str | None = Field(
        default=None,
        description="İnsanın uyruk bilgisi, vatandaşlık bilgisi. Türkiye Cumhuriyeti vatandaşı için 'T.C.' veya 'Türkiye' gibi değerler olabilir. Yabancilar için ise ülke adı veya uyruk bilgisi olabilir.",
    )
    adres: Adres = Field(description="İnsanın adresi, ikametgah adresi, yaşadığı yer")
    eposta: str | None = Field(default=None, description="İnsanın e-posta adresi, iletişim için kullanılabilir")
    telefon: str | None = Field(default=None, description="İnsanın telefon numarası, iletişim için kullanılabilir")
    kepadresi: str | None = Field(default=None, description="İnsanın KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir")


class Sirket(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Sirket",
        description="Döküman icinde bulunan tuzel kisileri yani sirketler, kamukurumlari, dernekler, vakiflar veya organizasyonlari tanimlar. Bu sirketler, sözleşmeyi imzalayan veya sözleşmede adı geçen tuzel kişilerdir.",
        cardinality=True,
        field_configs=[
            FieldConfig(field_name="vkn", search_type=NebulaIndexType.EXACT),
            FieldConfig(field_name="unvan", search_type=NebulaIndexType.EXACT),
        ],
    )
    unvan: str = Field(description="Şirketin ticaret unvani, resmi adı")
    vkn: str = Field(description="Şirketin vergi kimlik numarası, vergi numarası, 10 haneli bir sayı olmalıdır")
    adres: Adres = Field(description="Şirketin adresi, işyeri adresi. Cadde, sokak, il, ilce, mahelle, kapi no, posta kodu, ulke gibi bilgiler içerebilir")
    kepadresi: str | None = Field(default=None, description="Şirketin KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir")
    mersisno: str | None = Field(default=None, description="Şirketin MERSİS numarası, Türkiye'de ticaret sicil kaydı için kullanılan numara")


class SozlesmeBaslangicTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeBaslangicTarihi",
        description="Sozlesmenin baslangic tarihini belirler.Cogunlukla sozlesmenin baslangic tarihi, sozlesmenin imzalandigi tarih veya sozlesmenin yurutulecegi tarih olarak kullanilir.",
        cardinality=True,
        field_configs=[FieldConfig(field_name="baslangic_tarihi", search_type=NebulaIndexType.EXACT)],
    )
    baslangic_tarihi: str = Field(description="Sozlesmenin başlangıç tarihi, sözleşmenin yürürlüğe girdiği tarih. YYYY-MM-DD formatında doldurun lutfen")


class SozlesmeBitisTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeBitisTarihi",
        description="Sozlesmenin bitis tarihini belirler.Cogunlukla sozlesmenin bitis tarihi, sozlesmenin imzalandigi tarih veya sozlesmenin yurutulecegi tarih olarak kullanilir.",
        cardinality=True,
        field_configs=[FieldConfig(field_name="bitis_tarihi", search_type=NebulaIndexType.EXACT)],
    )
    bitis_tarihi: str | None = Field(default=None, description="Sozlesmenin bitis tarihi, sözleşmenin sona erdigi tarih. YYYY-MM-DD formatında doldurun lutfen")
