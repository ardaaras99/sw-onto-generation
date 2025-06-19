from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.configs import (
    HowToExtract,
    NebulaIndexType,
    NodeFieldConfig,
    NodeModelConfig,
)


class GeneralDocumentInfo(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Doküman hakkında genel bilgileri tanımlar, sözleşme ismi veya başlığı en önemli bilgidir. Her sözleşmede mutlaka bulunur.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    doküman_tipi: str = Field(
        default="Sözleşme",
        description="Belgenin tipi, örneğin 'Sözleşme', 'Sözleşme', 'Sözleşme' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    doküman_ismi: str = Field(
        default="Sözleşme",
        description="Belgenin başlığı",
        config=NodeFieldConfig(index_type=NebulaIndexType.VECTOR),
    )
    sozlesme_no: str | None = Field(
        default=None,
        description="Sözleşme numarası / referans numarası",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Adres(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Adres bilgilerini tanımlar. Adres, cadde, sokak, mahalle, apartman, ilçe, il ve posta kodu gibi bilgileri içerebilir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_2,  # Used in Insan and Sirket nodes, LLM fills there. Keep false.
        nodeclass_to_be_created_automatically=None,
    )

    il: str | None = Field(
        default=None,
        description="Adresin bulunduğu ilin adı, Örneğin 'İstanbul', 'Ankara', 'İzmir'",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    ilçe: str | None = Field(
        default=None,
        description="Adresin bulunduğu ilçenin adı, Örneğin 'Beşiktaş', 'Kadıköy', 'Ümraniye'",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    cadde: str | None = Field(default=None, description="Adresin bulunduğu cadde veya sokak adı")
    mahalle: str | None = Field(default=None, description="Adresin bulunduğu mahalle adı")
    apartman: str | None = Field(
        default=None,
        description="Adresin bulunduğu apartman adı veya numarası veya kapi numarası veya her ikisi de olabilir",
    )
    kat: str | None = Field(
        default=None,
        description="Adresin bulunduğu kat numarası, apartman içinde bulunan kat bilgisi",
    )
    kapı_no: str | None = Field(
        default=None,
        description="Adresin bulunduğu kapı numarası, apartman içinde bulunan kapı bilgisi",
    )
    posta_kodu: str | None = Field(
        default=None,
        description="Adresin bulunduğu posta kodu",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    ülke: str | None = Field(
        default=None,
        description="Adresin bulunduğu ülke, Türkiye için 'Türkiye' gibi değerler olabilir",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    ada: str | None = Field(default=None, description="Adreste belirtilmişse kadastro ada bilgisini içerir")
    parsel: str | None = Field(default=None, description="Adreste belirtilmişse kadastro parsel bilgisini içerir")
    acik_adres: str | None = Field(default=None, description="Adresin tek satırda tam hâli")


class Insan(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Doküman içinde bulunan gerçek kişileri yani insanları tanımlar. Bu insanlar, sözleşmeyi imzalayan veya sözleşmede adı geçen gerçek kişilerdir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    ad: str | None = Field(
        default=None,
        description="İnsanın adı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    soyad: str | None = Field(
        default=None,
        description="İnsanın soyadı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    tckn: str | None = Field(
        default=None,
        description="İnsanın T.C. kimlik numarası, Türkiye Cumhuriyeti vatandaşları için geçerlidir. 11 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    yabanci_kimlik_no: str | None = Field(
        default=None,
        description="İnsanın yabancı kimlik numarası, Türkiyede kayıtlı yabancı vatandaşlar için geçerlidir. 99 ile başlayan 11 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    pasaport_no: str | None = Field(
        default=None,
        description="İnsanın pasaport numarası, pasaporta sahip herkes için geçerlidir. 9 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    adres: Adres | None = Field(default=None, description="İnsanın adresi, ikametgah adresi, yaşadığı yer")
    uyruk_bilgisi: str | None = Field(
        default=None,
        description="İnsanın uyruk bilgisi, vatandaşlık bilgisi. Türkiye Cumhuriyeti vatandaşı için 'T.C.' veya 'Türkiye' gibi değerler olabilir. Yabancilar için ise ülke adı veya uyruk bilgisi olabilir.",
    )
    eposta: str | None = Field(default=None, description="Elektronik posta adresi, iletişim için kullanılabilir")
    telefon_no: str | None = Field(default=None, description="telefon numarası, iletişim için kullanılabilir")
    kep_adresi: str | None = Field(
        default=None,
        description="KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir",
    )
    role: str = Field(
        default="Taraf",
        description="İnsanın sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'İşveren', 'İşçi' gibi. Spesifik bir rol belirtilmemişse Taraf olarak da tanımlanabilir.",
    )
    dogum_tarihi: str | None = Field(
        default=None,
        description="İnsanın doğum tarihi, YYYY-MM-DD formatında doldurun lütfen.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    cinsiyet: str | None = Field(
        default=None,
        description="İnsanın cinsiyeti, erkek veya kadın olabilir.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    meslek: str | None = Field(
        default=None,
        description="İnsanın mesleği, örneğin 'İşçi', 'Mühendis', 'Avukat', 'Doktor', 'Öğretmen' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    vergi_no: str | None = Field(
        default=None,
        description="İnsanın vergi numarası, vergi numarası, 10 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    vergi_dairesi: str | None = Field(
        default=None,
        description="İnsanın bağlı olduğu vergi dairesi, örneğin 'Yeğenbey Vergi Dairesi",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Sirket(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Doküman içinde bulunan tüzel kişileri yani şirketler, kamu kuruluşları, dernekler, vakıflar veya organizasyonlari tanımlar. Bu şirketler, sözleşmeyi imzalayan veya sözleşmede adı geçen tüzel kişilerdir.",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )

    unvan: str | None = Field(
        default=None,
        description="Şirketin ticari unvanı, resmi adı",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    vkn: str | None = Field(
        default=None,
        description="Şirketin vergi kimlik numarası, vergi numarası, 10 haneli bir sayı olmalıdır",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    adres: Adres | None = Field(
        default=None,
        description="Şirketin adresi, işyeri adresi. Cadde, sokak, il, ilçe, mahalle, kapı no, posta kodu, ülke gibi bilgiler içerebilir",
    )
    kepadresi: str | None = Field(
        default=None,
        description="Şirketin KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir",
    )
    mersisno: str | None = Field(
        default=None,
        description="Şirketin 16 haneli MERSİS numarası, Türkiye'de ticaret sicil kaydı için kullanılan numara",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    role: str = Field(
        default="Taraf",
        description="İnsanın sözleşmedeki rolü, örneğin 'Kiracı', 'Kiraya Veren', 'Vekil', 'İşveren', 'İşçi' gibi. Spesifik bir rol belirtilmemişse Taraf olarak da tanımlanabilir.",
    )


class SozlesmeBaslangicTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
        Sözleşmenin başlangıç tarihini belirler.Çoğunlukla sözleşmenin başlangıç tarihi, sözleşmenin imzalandığı tarih veya sözleşmenin yürürlüğe girdiği tarih olarak kullanılır.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun. Eğer belirlenemiyorsa açıklama alanında sebebini veya belirsiz yapan cümleyi yazın.
        """,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    baslangic_tarihi: str | None = Field(
        default=None,
        description="Sözleşmenin başlangıç tarihi, sözleşmenin yürürlüğe girdiği tarih. YYYY-MM-DD formatında doldurun lütfen.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    aciklama: str | None = Field(
        default=None,
        description="Sözleşmenin başlangıç tarihi belirlenemiyorsa sebebi veya açıklaması. Özellikle 'imza tarihinde yürürlüğe girer' gibi ifadeler kullanılırsa 'imza_tarihinde_yururluge_girer' alanını True olarak tanımlayın",
    )
    imza_tarihinde_yururluge_girer: bool = Field(
        default=False,
        description="Eğer sözleşme imza tarihinde yürürlüğe giriyorsa True olarak tanımlayın. Sözleşme başlangıç tarihi belirlenebiliyorsa False olarak tanımlayın",
    )


class SozlesmeBitisTarihi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
        Sözleşmenin bitiş tarihini belirler. Çoğunlukla sözleşmenin bitiş tarihi ayrı bir madde olarak belirtilir.
        Bazen bitiş tarihi Sözleşme başlangıç tarihinden itibaren bir süre sonra da belirtilebilir.
        Belirlenebiliyorsa YYYY-MM-DD formatında doldurun lütfen. Eğer belirlenemiyorsa None olarak tanımlayın ve açıklama alanında sebebini veya belirsiz yapan cümleyi yazın.
        """,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    bitis_tarihi: str | None = Field(
        default=None,
        description="Sözleşmenin bitiş tarihi, sözleşmenin sona erdiği tarih. YYYY-MM-DD formatında doldurun lütfen",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    aciklama: str | None = Field(
        default=None,
        description="Sözleşmenin bitiş tarihi belirlenemiyorsa sebebi veya açıklaması.",
    )


class SozlesmeYururluk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="""
            Sözleşmenin yürürlükte olup olmadığını belirlet. Başlangıç tarihi bugünden sonraki bir tarih ise sözleşme yürürlükte değildir. Bitiş tarihi bugünden önceki bir tarih ise sözleşme yürürlükte değildir.
            Yürürlükte olan sözleşmeler, başlangıç tarihi bugünden önceki bir tarih ve bitiş tarihi bugünden sonraki bir tarih olan sözleşmelerdir. Bu durumda sözleşme yürürlükte kabul edilir. Kesinlikle emin değilsiniz lütfen None olarak tanımlayın.
            """,
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    sozlesme_yururluk: bool | None = Field(
        default=None,
        description="Sözleşmenin yürürlükte olup olmadığını belirler. True ise sözleşme yürürlüktedir, False ise sözleşme yürürlükte değildir.",
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
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    sozlesme_suresi: str | None = Field(
        default=None,
        description="Sozlesmenin suresi, sozlesmenin gecerlilik suresi. Yil, ay veya gun seklinde belirtilmis olabilir. Ornek 1 yil 3 ay veya 3 ay 15 gun gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class SozlesmeKonu(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin konusunu belirler. Sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir. Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    konu: str | None = Field(
        default=None,
        description="Sozlesmenin konusunu belirler. Sozlesmenin amacini ve kapsamini belirler. Sozlesmenin ne ile ilgili oldugunu, hangi hizmetlerin veya urunlerin saglanacagini burada belirtilir. Ozellikle belirtilmemisse sozlesmenin 1-3 cumlelik ozeti ile tanimlanabilir.",
    )


class Teminatlar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
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
    teminat_miktari: str | None = Field(
        default=None,
        description="Sozlesmede belirtilen herhangi bir teminatin miktari. Teminat miktari, para birimi ile birlikte belirtilmelidir. Ornegin '1000 TL', '500 USD', '2000 EUR' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )
    teminat_tipi: str | None = Field(
        default=None,
        description="Teminatin tipi belirtilmelidir. Ornegin 'Banka Teminat Mektubu', 'Banka Hesap Blokesi', 'Altin', 'Doviz', 'Para' gibi. Teminat tipi, teminatin ne sekilde saglandigini belirtir.",
    )


class UyusmazlikCozumYeri(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Herhangi bir uyusmazlik halinde taraflarin hangi mahkemeye veya arabulucuya basvuracagini belirler. Genellikle sozlesmenin sonunda belirtilir. 'Anlasmazliklarin Cozumu', 'Uyuşmazlık Çözüm Yeri', 'Uyuşmazlık Mahkemesi', 'Arabuluculuk Merkezi' gibi ifadelerle baslar.",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=None,
    )
    uyusmazlik_cozum_yeri: str | None = Field(
        default=None,
        description="Uyuşmazlık çözüm yeri, uyuşmazlık halinde başvurulacak mahkeme veya arabuluculuk merkezi. Örneğin 'İstanbul Mahkemeleri', 'Ankara Arabuluculuk Merkezi' gibi.",
        config=NodeFieldConfig(index_type=NebulaIndexType.EXACT),
    )


class Ekler(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    ek_var: bool = Field(default=True, description="En az bir ek varsa True, yoksa zaten yaratilmaz.")


class Ek(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=True,
        description="Sozlesmenin icerisnde belirtilen ekler. Ekler, sözleşmenin ayrıntılarını veya ek belgelerini içerebilir. Ekler, sözleşmenin bir parçası olarak kabul edilir. Genelde 'ekler', 'sozlesmenin ekleri', 'ek-1', 'ek-2' gibi ifadelerle başlar. Ek ifadesinin mutlaka belirtilmis olmasi gerekir",
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=Ekler,
    )
    ek_aciklama: str | None = Field(default=None, description="sozlemede belirtilen ekin aciklamasi. ")


class FesihMaddeleri(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    fesih_var: bool = Field(default=True, description="En az bir fesih maddesi varsa True, yoksa zaten yaratilmaz.")


class FesihMaddesi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="""
        Sözleşmenin içinde herhangi bir fesih maddesi olup olmadığını belirler. En az bir fesih maddesi varsa true olur yoksa bu node yaratılmaz.
        """,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=FesihMaddeleri,
    )
    fesih_maddesi: str | None = Field(default=None, description="Sozlesmede belirtilen fesih maddesi. ")


class FaizMaddeleri(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="Predefined",
        cardinality=False,
        how_to_extract=HowToExtract.CASE_1,
        nodeclass_to_be_created_automatically=None,
    )
    faiz_var: bool = Field(
        default=True,
        description="En az bir faize iliskin madde varsa True, yoksa zaten yaratilmaz.",
    )


class FaizMaddesi(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        nodetag_index=False,
        description="""
        Sozlesmede uygulanacak faiz veya temerrüt faizi ile ilgili maddeleri tanimlar. Her farkli faiz tipi veya orani icin ayri bir node olusturun.
        """,
        cardinality=True,
        how_to_extract=HowToExtract.CASE_0,
        nodeclass_to_be_created_automatically=FaizMaddeleri,
    )
    faiz_orani: str = Field(
        default="",
        description="Faiz orani. Ornek: 'Yıllık %10', 'Aylık %1,5', 'TCMB politika faizi + %3' gibi.",
    )
    faiz_turu: str | None = Field(
        default=None,
        description="Faizin turu. Ornek: 'Temerrüt Faizi', 'Yasal Faiz', 'Avans Faizi' gibi.",
    )
    faiz_hesaplama_aciklamasi: str | None = Field(
        default=None,
        description="Faizin nasil hesaplanacagini veya hangi kosullarda uygulanacagini aciklayan cumle veya madde metni.",
    )
