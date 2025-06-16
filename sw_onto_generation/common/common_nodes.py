from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import NebulaIndexType, NodeFieldConfig, NodeModelConfig


class GeneralDocumentInfo(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    documan_ismi: str = Field(
        default="",
        description="Belgenin basligi",
        config=NodeFieldConfig(index_type=NebulaIndexType.VECTOR),
    )
    documan_type: str = Field(...)


class Adres(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Adres bilgilerini tanımlar. Adres, cadde, sokak, mahalle, apartman, ilçe, il ve posta kodu gibi bilgileri içerebilir.",
        cardinality=True,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )

    il: str = Field(
        default="",
        description="Adresin bulunduğu il",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    ilçe: str = Field(
        default="",
        description="Adresin bulunduğu ilçe",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    cadde: str = Field(
        default="",
        description="Adresin cadde veya sokak adı",
    )
    mahalle: str = Field(
        default="",
        description="Adresin bulunduğu mahalle",
    )
    apartman: str = Field(
        default="",
        description="Adresin bulunduğu apartman adi veya numarasi veya kapi numarası veya her ikisi de olabilir",
    )
    kat: str = Field(
        default="",
        description="Adresin bulunduğu kat numarası, apartman içinde kat bilgisi",
    )
    kapi_no: str = Field(
        default="",
        description="Adresin bulunduğu kapı numarası, apartman içinde kapı bilgisi",
    )
    ulke: str = Field(
        default="",
        description="Adresin bulunduğu ülke, Türkiye için 'Türkiye' veya 'T.C.' gibi değerler olabilir",
    )
    posta_kodu: str = Field(
        default="",
        description="Adresin posta kodu",
    )
    ada: str = Field(
        default="",
        description="adreste belirtilmisse kadastro ada bilgisini icerir",
    )
    parsel: str = Field(
        default="",
        description="adreste belirtilmisse kadastro parsel bilgisini icerir",
    )


class Insan(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Döküman icinde bulunan gercek kisileri yani insanlari tanimlar. Bu insanlar, sözleşmeyi imzalayan veya sözleşmede adı geçen gerçek kişilerdir.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    ad: str = Field(
        default="",
        description="İnsanın adı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    soyad: str = Field(
        default="",
        description="İnsanın soyadı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    tckn: str = Field(
        default="",
        description="İnsanın T.C. kimlik numarası, Türkiye Cumhuriyeti vatandaşları için geçerlidir",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    adres: Adres | None = Field(
        default=None, description="İnsanın adresi, ikametgah adresi, yaşadığı yer"
    )
    uyruk_bilgisi: str = Field(
        default="",
        description="İnsanın uyruk bilgisi, vatandaşlık bilgisi. Türkiye Cumhuriyeti vatandaşı için 'T.C.' veya 'Türkiye' gibi değerler olabilir. Yabancilar için ise ülke adı veya uyruk bilgisi olabilir.",
    )
    eposta: str = Field(
        default="",
        description="e-posta adresi, iletişim için kullanılabilir",
    )
    telefon_no: str = Field(
        default="",
        description="telefon numarası, iletişim için kullanılabilir",
    )
    kep_adresi: str = Field(
        default="",
        description="KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir",
    )
    role: str = Field(
        default="Taraf",
        description="İnsanın sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'Sozlesme tarafi', 'isveren', 'isci' gibi. Taraf olarak da tanımlanabilir. ",
    )


class Sirket(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Döküman icinde bulunan tuzel kisileri yani sirketler, kamukurumlari, dernekler, vakiflar veya organizasyonlari tanimlar. Bu sirketler, sözleşmeyi imzalayan veya sözleşmede adı geçen tuzel kişilerdir.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )

    unvan: str = Field(
        default="",
        description="Şirketin ticaret unvani, resmi adı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    vkn: str = Field(
        default="",
        description="Şirketin vergi kimlik numarası, vergi numarası, 10 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    adres: Adres | None = Field(
        default=None,
        description="Şirketin adresi, işyeri adresi. Cadde, sokak, il, ilce, mahelle, kapi no, posta kodu, ulke gibi bilgiler içerebilir",
    )
    kepadresi: str = Field(
        default="",
        description="Şirketin KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir",
    )
    mersisno: str = Field(
        default="",
        description="Şirketin MERSİS numarası, Türkiye'de ticaret sicil kaydı için kullanılan numara",
    )
    role: str = Field(
        default="Taraf",
        description="Sirketin sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'Sozlesme tarafi', 'isveren', 'isci' gibi. Taraf olarak da tanımlanabilir. ",
    )


class SozlesmeBaslangicTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
        Sozlesmenin baslangic tarihini belirler.Cogunlukla sozlesmenin baslangic tarihi, sozlesmenin imzalandigi tarih veya sozlesmenin yurutulecegi tarih olarak kullanilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin ve aciklama alaninda sebebini veya belirsiz yapan cumleyi yazin.
        """,
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    baslangic_tarihi: str = Field(
        default="",
        description="Sozlesmenin başlangıç tarihi, sözleşmenin yürürlüğe girdiği tarih. YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    aciklama: str = Field(
        default="",
        description="Sozlemenin baglangic tarihi belirlenemiyorsa sebebi veya aciklamasi. Ozellikle 'imza tarihinde yururluge girer' gibi ifadeler kullanilmissa 'imza_tarihinde_yururluge_girer' alanini True olarak tanimlayin",
    )
    imza_tarihinde_yururluge_girer: bool = Field(
        default=False,
        description="Eger sozlesme imza tarihinde yururluge giriyorsa True olarak tanimlayin. Sozlesme baslangic tarihi belirlenebiliyorsa False olarak tanimlayin",
    )


class SozlesmeBitisTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
        Sozlesmenin bitis tarihini belirler.Cogunlukla sozlesmenin bitis tarihi ayri bir madde olarak belirtilir.
        Bazen bitis tarihi Sozlesme baslangic tarihindne itibaren bir sure sonra da belirtilebilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lutfen. Eger belirlenemiyorsa 0000-00-00 olarak tanimlayin ve aciklama alaninda sebebini veya belirsiz yapan cumleyi yazin.
        """,
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    bitis_tarihi: str = Field(
        default="",
        description="Sozlesmenin bitis tarihi, sözleşmenin sona erdigi tarih. YYYY-MM-DD formatında doldurun lutfen",
        config=NodeFieldConfig(
            index_type=NebulaIndexType.EXACT,
        ),
    )
    aciklama: str = Field(
        default="",
        description="Sozlemenin bitis tarihi belirlenemiyorsa sebebi veya aciklamasi.",
    )


class SozlesmeYururluk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
            Sozlesmenin yururlulukte olup olmadigini belirlet. Baslangic tarihi bugunden sonraki bri tarih ise sozlesme yururlukte degildir. Bitis tarihi bugunden onceki bir tarih ise sozlesme yururlukte degildir.
            Yururlulukte olan sozlesmeler, baslangic tarihi bugunden onceki bir tarih ve bitis tarihi bugunden sonraki bir tarih olan sozlesmelerdir. Bu durumda sozlesme yururlukte kabul edilir. Kesinlikle emin degilsiniz lutfen None olarak tanimlayin.
            """,
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    sozlesme_yururluk: bool = Field(
        default=False,
        description="Sozlesmenin yururlukte olup olmadigini belirler. True ise sozlesme yururluktedir, False ise sozlesme yururlukte degildir.",
    )


class SozlesmeSure(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
        Sozlesmenin suresini belirler. Sozlesmenin suresi, sozlesme gecerlidir. SozlesmeBaslangicTarihi ile SozlesmeBitisTarihi arasindaki suredir.
        Eger bu iki tarih belirtimisse kesinlikle bu iki tarih arasindaki suredir. Imzalandigi tarihten itibaren su kadar sure gecerlidir diye de belirtilebilir.
        Belirtilmemis de olabilir. Yil, ay veya gun seklinde belirtilmis olabilir.En buyuk zaman birimine gore belirtiniz lutfen. Ornek 1 yil 3 ay veya 3 ay 15 gun gibi.
        """,
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    sozlesme_suresi: str = Field(
        default="",
        description="Sozlesmenin suresi, sozlesmenin gecerlilik suresi. Yil, ay veya gun seklinde belirtilmis olabilir. Ornek 1 yil 3 ay veya 3 ay 15 gun gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class SozlesmeKonu(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin konusunu belirler. Sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir. Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir.",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    konu: str = Field(
        default="",
        description="Sozlesmenin konusunu belirler. Sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir. Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir.",
    )


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    teminat_var: bool = Field(
        default=False, description="En az bir teminat varsa True, yoksa zaten yaratilmaz."
    )


class Teminat(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin icerisnde her hangi bir konuda bir veya birden fazla teminat alinmis olabilir. Teminat tipleri olarak banka teminat mektubu, banka hesap blokesi, altin, doviz, para sayabiliriz.. Depozito olarak da teminat istenmis olabilir. her birini ayri bir node olarak tanimlayin.",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Teminatlar,
    )
    teminat_miktari: str = Field(
        default="",
        description="Sozlesmede belirtilen herhangi bir teminatin miktari. Teminat miktari, para birimi ile birlikte belirtilmelidir. Ornegin '1000 TL', '500 USD', '2000 EUR' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    teminat_tipi: str = Field(
        default="",
        description="Teminatin tipi belirtilmelidir. Ornegin 'Banka Teminat Mektubu', 'Banka Hesap Blokesi', 'Altin', 'Doviz', 'Para' gibi. Teminat tipi, teminatin ne sekilde saglandigini belirtir.",
    )


class UyusmazlikCozumYeri(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Herhangi bir uyusmazlik halinde taraflarin hangi mahkemeye veya arabulucuya basvuracagini belirler. Genellikle sozlesmenin sonunda belirtilir. 'Anlasmazliklarin Cozumu', 'Uyuşmazlık Çözüm Yeri', 'Uyuşmazlık Mahkemesi', 'Arabuluculuk Merkezi' gibi ifadelerle baslar.",
        cardinality=False,
        ask_llm=True,
        nodeclass_to_be_created_automatically=None,
    )
    uyusmazlik_cozum_yeri: str = Field(
        default="",
        description="Uyuşmazlık çözüm yeri, uyuşmazlık halinde başvurulacak mahkeme veya arabuluculuk merkezi. Örneğin 'İstanbul Mahkemeleri', 'Ankara Arabuluculuk Merkezi' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


# class Kefil(BaseNode):
#     node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
#         node_tag="Kefil",
#         description="""
#     Bu sozlesmeye kefil olan kisiyi veya sirketi tanimlar. Kefil, sozlesmenin yerine getirilmemesi durumunda sorumluluk alir.
#     Kefil, Insan veya Sirket olabilir. Kefil, sözleşmenin tarafı değildir ancak sözleşmenin yerine getirilmemesi durumunda sorumluluk alır.
#     kefil in turleri vardir. En onemlisi muteselsil kefildir. Muteselsil kefil, borcun tamamindan sorumludur ve borcun bir kismi icin kefil degildir.
#     """,
#         cardinality=True,
#     )
#     kefil: Insan | Sirket | None = Field(
#         default=None,
#         description="kefil olan sirketin veya da insanin adi veya unvani, VKN veya TCKN gibi kimlik bilgileri ile birlikte tanimlanabilir. Ornegin 'Ahmet Yılmaz', 'ABC Sirketi', '1234567890' gibi.",
#     )
#     kefil_turu: str | None = Field(default=None, description="Kefilin türü, örneğin 'Müteselsil Kefil', 'Sınırlı Kefil', 'Kefil' gibi.")


class Ekler(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        ask_llm=False,
        nodeclass_to_be_created_automatically=None,
    )
    ek_var: bool = Field(
        default=False, description="En az bir ek varsa True, yoksa zaten yaratilmaz."
    )


class Ek(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin icerisnde belirtilen ekler. Ekler, sözleşmenin ayrıntılarını veya ek belgelerini içerebilir. Ekler, sözleşmenin bir parçası olarak kabul edilir. Genelde 'ekler', 'sozlesmenin ekleri', 'ek-1', 'ek-2' gibi ifadelerle başlar. Ek ifadesinin mutlaka belirtilmis olmasi gerekir",
        cardinality=True,
        ask_llm=True,
        nodeclass_to_be_created_automatically=Ekler,
    )
    ek_aciklama: str = Field(default="", description="sozlemede belirtilen ekin aciklamasi. ")
