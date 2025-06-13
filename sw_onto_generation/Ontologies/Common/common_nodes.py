from typing import ClassVar

from pydantic import Field
from pydantic.fields import FieldInfo

from sw_onto_generation.Ontologies.Base.base_node import BaseNode
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, NodeModelConfig


class GeneralDocumentInfo(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="GeneralDocumentInfo",
        nodetag_index=True,
        description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
        cardinality=False,
        field_configs=[FieldConfig(field_name="documan_ismi", search_type=NebulaIndexType.VECTOR)],
        extra_fields=[FieldInfo(alias="documan_type", annotation=str, default="")],
    )

    documan_ismi: str = Field(description="Belgenin başlığı")


class Adres(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Adres",
        description="Adres bilgilerini tanımlar. Adres, cadde, sokak, mahalle, apartman, ilçe, il ve posta kodu gibi bilgileri içerebilir.",
        cardinality=True,
        ask_llm=False,
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
            FieldConfig(field_name="adres", default_relation_type="has_adres"),
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
        Bu sozlesmenin ana konusunu tanimlar. Genelde ayri bir madde olarak belirtilir. 'Amac', 'Kapsam', 'Konu', 'Sozlesmenin konusu', 'Is tanimi' gibi ifadelerle baslar.
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
        node_tag="SozlesmeSure",
        description="""
        Sozlesmenin suresini belirler. Sozlesmenin suresi, sozlesme gecerlidir. SozlesmeBaslangicTarihi ile SozlesmeBitisTarihi arasindaki suredir.
        Eger bu iki tarih belirtimisse kesinlikle bu iki tarih arasindaki suredir. Imzalandigi tarihten itibaren su kadar sure gecerlidir diye de belirtilebilir.
        Belirtilmemis de olabilir. Yil, ay veya gun seklinde belirtilmis olabilir.En buyuk zaman birimine gore belirtiniz lutfen. Ornek 1 yil 3 ay veya 3 ay 15 gun gibi.
        """,
        cardinality=False,
        field_configs=[FieldConfig(field_name="sozlesme_suresi", search_type=NebulaIndexType.EXACT)],
    )
    sozlesme_suresi: str | None = Field(
        default=None, description="Sozlesmenin suresi, sozlesmenin gecerlilik suresi. Yil, ay veya gun seklinde belirtilmis olabilir. Ornek 1 yil 3 ay veya 3 ay 15 gun gibi."
    )


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Teminatlar",
        description="""
        Sozlesmenin icerisinde herhangi bir teminat olup olmadigini belirler. En az bir teminat varsa true olur yoksa bu node yaratilmaz.
        """,
        cardinality=False,
        ask_llm=False,
    )
    teminat_var: bool | None = Field(default=True, description="En az bir teminat varsa True, yoksa zaten yaratilmaz.")


class Teminat(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Teminat",
        description="""
        Sozlesmenin icerisnde her hangi bir konuda bir veya birden fazla teminat alinmis olabilir. Teminat tipleri olarak banka teminat mektubu, banka hesap blokesi, altin, doviz, para sayabiliriz..
        Depozito olarak da teminat istenmis olabilir. her birini ayri bir node olarak tanimlayin.
        """,
        cardinality=True,
        nodeclass_to_be_created_automatically=Teminatlar,
    )
    teminat_miktari: str = Field(
        default="", description="Sozlesmede belirtilen herhangi bir teminatin miktari. Teminat miktari, para birimi ile birlikte belirtilmelidir. Ornegin '1000 TL', '500 USD', '2000 EUR' gibi."
    )
    teminat_tipi: str | None = Field(
        default=None,
        description="Teminatin tipi belirtilmelidir. Ornegin 'Banka Teminat Mektubu', 'Banka Hesap Blokesi', 'Altin', 'Doviz', 'Para' gibi. Teminat tipi, teminatin ne sekilde saglandigini belirtir.",
    )


class UyusmazlikCozumYeri(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="UyusmazlikCozumYeri",
        description="""
        Herhangi bir uyusmazlik halinde taraflarin hangi mahkemeye veya arabulucuya basvuracagini belirler.
        Genellikle sozlesmenin sonunda belirtilir. 'Anlasmazliklarin Cozumu', 'Uyuşmazlık Çözüm Yeri', 'Uyuşmazlık Mahkemesi', 'Arabuluculuk Merkezi' gibi ifadelerle baslar.
        """,
        cardinality=False,
    )
    uyusmazlik_cozum_yeri: str | None = Field(
        default=None, description="Uyuşmazlık çözüm yeri, uyuşmazlık halinde başvurulacak mahkeme veya arabuluculuk merkezi. Örneğin 'İstanbul Mahkemeleri', 'Ankara Arabuluculuk Merkezi' gibi."
    )


class Kefil(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Kefil",
        description="""
    Bu sozlesmeye kefil olan kisiyi veya sirketi tanimlar. Kefil, sozlesmenin yerine getirilmemesi durumunda sorumluluk alir.
    Kefil, Insan veya Sirket olabilir. Kefil, sözleşmenin tarafı değildir ancak sözleşmenin yerine getirilmemesi durumunda sorumluluk alır.
    kefil in turleri vardir. En onemlisi muteselsil kefildir. Muteselsil kefil, borcun tamamindan sorumludur ve borcun bir kismi icin kefil degildir.
    """,
        cardinality=True,
    )
    kefil: Insan | Sirket | None = Field(
        default=None,
        description="kefil olan sirketin veya da insanin adi veya unvani, VKN veya TCKN gibi kimlik bilgileri ile birlikte tanimlanabilir. Ornegin 'Ahmet Yılmaz', 'ABC Sirketi', '1234567890' gibi.",
    )
    kefil_turu: str | None = Field(default=None, description="Kefilin türü, örneğin 'Müteselsil Kefil', 'Sınırlı Kefil', 'Kefil' gibi.")


class Ekler(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Ekler",
        description="""
        Sozlesmenin icerisinde herhangi bir Ek olup olmadigini belirler. En az bir Ek varsa true olur yoksa bu node yaratilmaz.
        """,
        cardinality=False,
        ask_llm=False,
    )
    ek_var: bool | None = Field(default=True, description="En az bir ek varsa True, yoksa zaten yaratilmaz.")


class Ek(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Ek",
        description="""
        Sozlesmenin icerisnde belirtilen ekler. Ekler, sözleşmenin ayrıntılarını veya ek belgelerini içerebilir. Ekler, sözleşmenin bir parçası olarak kabul edilir. Genelde 'ekler', 'sozlesmenin ekleri', 'ek-1', 'ek-2' gibi ifadelerle başlar.
        Ek ifadesinin mutlaka belirtilmis olmasi gerekir
        """,
        cardinality=True,
        nodeclass_to_be_created_automatically=Ekler,
    )
    ek_aciklama: str = Field(default="", description="sozlemede belirtilen ekin aciklamasi. ")
