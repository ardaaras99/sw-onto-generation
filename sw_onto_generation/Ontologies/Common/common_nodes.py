from typing import ClassVar

from pydantic import Field

from sw_onto_generation.Ontologies.Base.base_node import BaseNode
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, NodeModelConfig


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
    role: str = Field(default="Taraf", description="İnsanın sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'Sozlesme tarafi', 'isveren', 'isci' gibi. Taraf olarak da tanımlanabilir. ")


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
    role: str = Field(default="Taraf", description="Sirketin sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'Sozlesme tarafi', 'isveren', 'isci' gibi. Taraf olarak da tanımlanabilir. ")


class SozlesmeBaslangicTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeBaslangicTarihi",
        description="""
        Sozlesmenin baslangic tarihini belirler.Cogunlukla sozlesmenin baslangic tarihi, sozlesmenin imzalandigi tarih veya sozlesmenin yurutulecegi tarih olarak kullanilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin ve aciklama alaninda sebebini veya belirsiz yapan cumleyi yazin.
        """,
        cardinality=True,
        field_configs=[FieldConfig(field_name="baslangic_tarihi", search_type=NebulaIndexType.EXACT)],
    )
    baslangic_tarihi: str = Field(
        description="Sozlesmenin başlangıç tarihi, sözleşmenin yürürlüğe girdiği tarih. YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin."
    )
    aciklama: str | None = Field(
        default=None,
        description="Sozlemenin baglangic tarihi belirlenemiyorsa sebebi veya aciklamasi. Ozellikle 'imza tarihinde yururluge girer' gibi ifadeler kullanilmissa 'imza_tarihinde_yururluge_girer' alanini True olarak tanimlayin",
    )
    imza_tarihinde_yururluge_girer: bool = Field(
        default=False, description="Eger sozlesme imza tarihinde yururluge giriyorsa True olarak tanimlayin. Sozlesme baslangic tarihi belirlenebiliyorsa False olarak tanimlayin"
    )


class SozlesmeBitisTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeBitisTarihi",
        description="""
        Sozlesmenin bitis tarihini belirler.Cogunlukla sozlesmenin bitis tarihi ayri bir madde olarak belirtilir.
        Bazen bitis tarihi Sozlesme baslangic tarihindne itibaren bir sure sonra da belirtilebilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin ve aciklama alaninda sebebini veya belirsiz yapan cumleyi yazin.
        """,
        cardinality=True,
        field_configs=[FieldConfig(field_name="bitis_tarihi", search_type=NebulaIndexType.EXACT)],
    )
    bitis_tarihi: str | None = Field(default=None, description="Sozlesmenin bitis tarihi, sözleşmenin sona erdigi tarih. YYYY-MM-DD formatında doldurun lutfen")
    aciklama: str | None = Field(default=None, description="Sozlemenin bitis tarihi belirlenemiyorsa sebebi veya aciklamasi. ")


class SozlesmeYururluk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeYururluk",
        description="""
            Sozlesmenin yururlulukte olup olmadigini belirlet. Baslangic tarihi bugunden sonraki bri tarih ise sozlesme yururlukte degildir. Bitis tarihi bugunden onceki bir tarih ise sozlesme yururlukte degildir.
            Yururlulukte olan sozlesmeler, baslangic tarihi bugunden onceki bir tarih ve bitis tarihi bugunden sonraki bir tarih olan sozlesmelerdir. Bu durumda sozlesme yururlukte kabul edilir. Kesinlikle emin degilsiniz lutfen None olarak tanimlayin.
            """,
        cardinality=False,
    )
    sozlesme_yururluk: bool | None = Field(description="Sozlesmenin yururlukte olup olmadigini belirler. True ise sozlesme yururluktedir, False ise sozlesme yururlukte degildir.")


class SozlesmeKonu(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeKonu",
        description="""
        Bu sozlesmenin ana konusunu tanimlar. Genelde ayri bir madde olarak belirtilir. 'Amac', 'Kapsam', 'Konu', 'Sozlesmenin konusu' gibi ifadelerle baslar.
        Sozlesmenin konusu, sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir.
        Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir.
        """,
        cardinality=False,
    )
    sozlesme_konu: str = Field(
        description="Bu sozlesmenin ne ile ilgili oldugunu belirtir. Sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir. Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir."
    )


class SozlesmeSure(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SozlesmeBitisTarihi",
        description="""
        Sozlesmenin bitis tarihini belirler.Cogunlukla sozlesmenin bitis tarihi ayri bir madde olarak belirtilir.
        Bazen bitis tarihi Sozlesme baslangic tarihindne itibaren bir sure sonra da belirtilebilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin ve aciklama alaninda sebebini veya belirsiz yapan cumleyi yazin.
        """,
        cardinality=False,
        field_configs=[FieldConfig(field_name="bitis_tarihi", search_type=NebulaIndexType.EXACT)],
    )
    bitis_tarihi: str | None = Field(default=None, description="Sozlesmenin bitis tarihi, sözleşmenin sona erdigi tarih. YYYY-MM-DD formatında doldurun lutfen")
    aciklama: str | None = Field(default=None, description="Sozlemenin bitis tarihi belirlenemiyorsa sebebi veya aciklamasi. ")


class Teminat(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Teminat",
        description="""
        Sozlesmenin icerisnde her hangi bir konuda bir veya birden fazla teminat alinmis olabilir. Teminat tipleri olarak banka teminat mektubu, banka hesap blokesi, altin, doviz, para sayabiliriz..
        Depozito olarak da teminat istenmis olabilir.
        """,
        cardinality=True,
    )
    teminat_miktari: str = Field(
        default="", description="Sozlesmede belirtilen herhangi bir teminatin miktari. Teminat miktari, para birimi ile birlikte belirtilmelidir. Ornegin '1000 TL', '500 USD', '2000 EUR' gibi."
    )
    teminat_tipi: str | None = Field(
        default=None,
        description="Teminatin tipi belirtilmelidir. Ornegin 'Banka Teminat Mektubu', 'Banka Hesap Blokesi', 'Altin', 'Doviz', 'Para' gibi. Teminat tipi, teminatin ne sekilde saglandigini belirtir.",
    )


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Teminatlar",
        description="""
        Sozlesmenin icerisnde yer alan tum teminatlari belirtir. Her birini teminatlar listesi icinde tutar.
        """,
        cardinality=False,
    )
    teminatlar: list[Teminat] = Field(default=[], description="Sozlesmedeki tum teminatlari liste icerisinde tutar.")
