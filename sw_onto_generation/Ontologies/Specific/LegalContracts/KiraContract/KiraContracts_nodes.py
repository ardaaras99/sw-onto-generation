from typing import ClassVar

from pydantic import Field

from sw_onto_generation.Ontologies.Base.base_node import BaseNode
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, NodeModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import Adres


class KiraKonusuMulk(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Kira_konusu_mulk",
        description="""
                Bu bir bina, ev, ofis, işyeri veya başka bir gayrimenkul olabilir. Kira sözleşmesinin konusu olan mülkü tanımlar.  
                Kira konusu mülk, tip, buyukluk, adres ve diğer özellikleri içerebilir.
                """,
        cardinality=True,
        field_configs=[FieldConfig(field_name="adres", search_type=NebulaIndexType.VECTOR)],
    )

    tur: str | None = Field(description="Kira konusu mulkun turunu belirtir Ev, arsa, ofis, tarla, isyeri, bina gibi")
    adres: Adres = Field(description="Kira konusu mülkün adresi, konumu")
    olcum: str | None = Field(default=None, description="Kira konusu mülkün ölçüm birimi, örneğin metrekare, dönüm, hektar gibi. Lutfen olcum birimini de belirtiniz")


class KiraDepozito(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="KiraDepozito",
        description="""
                Kira konusu mulk icin istenilan depozito. Para, altin, doviz , teminat mektubu gibi seyler olabilir.
                kira sozlesmeleri icin ozel bir teminat turudur. Mutlaka miktar ve turu belirtilmelidir.
                """,
        cardinality=False,
    )

    depozitoturu: str = Field(
        default="Para",  # Default olarak Para alindi, eger baska bir tur varsa degistirilebilir
        description="Kira icin verilen dopozitonun turu,teminat mektubu, banka teminatı, altin gibi seyler olabilir. Eger para ise turune gore TL, USD, EUR gibi birim belirtiniz",
    )
    miktar: str = Field(
        default="",
        description="Kira icin verilen depozito miktari, para birimi ile birlikte yazilmalidir. Ornegin 1000 TL, 500 USD gibi veya 1000 gram altin gibi. Eger para birimi belirtilmemisse TL olarak alinir.",
    )


class Demirbas(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Demirbas",
        description="""
            Sozlesmede demirbas olarak belirtilen esya, donanim, malzeme, mobilya, klima, mutfak esyasi, garaj esyasi etc. gibi seyler.
            kiracinin sadece kullanabilecegi ama mulkiyeti mulk sahibinde bulunan ve sozlesmede belirtilen esyalar.Birden fazla olabilir.
            madde madde belirtilebilecegi gibi virgule ayrilmis bir metin ile de belirtilebilir. her birini ayri bir node olarak cikarmani istiyorum.
            """,
        cardinality=True,
    )
    demirbas_ismi: str | None = Field(description="Demirbasin adi, ozellikleri, markasi, modeli gibi bilgiler icerebilir")


class Demirbaslar(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="Demirbaslar",
        description="""
                Kira konusu mulk icinde bulunan ve kiracinin sadece kullanabilecegi ama mulkiyeti mulk sahibinde bulunan ve sozlesmede belirtilen esyalar.Birden fazla olabilir. 
                en az bir tane varsa true olur yoksa yaratilmaz.
                demirbaslar madde madde belirtilebilecegi gibi virgule ayrilmis bir metin ile de belirtilebilir.
                """,
        cardinality=False,
    )

    demirbas_var: bool | None = Field(description="Kiralan mulk icin sozlesmede demirbas belirtilmis mi ?.")


class KiraBedeli(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="KiraBedeli",
        description="""
            Kira sozlesmesinde belirlenen kira miktari. Bu miktar aylik veya yillik olarak belirtilmis olabilir.
            Kira bedeli, para birimi ile birlikte yazilmalidir. Ornegin 1000 TL, 500 USD gibi.
            """,
        cardinality=False,
    )
    kira_bedeli: float = Field(default=0.0, description="Kira bedeli miktari")
    para_birimi: str = Field(default="TL", description="Kira bedelinin para birimi. Ornegin TL, USD, EUR gibi")
    odeme_periyodu: str = Field(default="Aylık", description="Kira bedelinin odeme periyodu. Ornegin Aylık, Yıllık gibi. Eger belirtilmemisse Aylık olarak alinir.")
    odeme_bilgisi: str = Field(
        default="", description="Kira bedelinin nasil odenecegi, odeme sarti. Ornegin peşin, aylik, yillik gibi. Ayin 5 inci gunu, ayin ilk 3 gunu gibi detaylar da eklenebilir."
    )
    odeme_yontemi: str = Field(default="", description="Kira bedelinin odeme yontemi. Ornegin banka havalesi, nakit, kredi karti gibi. Hangi hesaba odenecegi de belirtilebilir.")


class KiraAmaci(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="KiraAmaci",
        description="""
            Kiralanan seyin ne icin kullanilacagi. En cok karsilasilan mesken, ev, ofis, fabrika, depo, isyeri, lokanta, restoran gibi seyler olabilir. 
            daha uzun aciklamalar da olabilir. 
            """,
        cardinality=False,
    )
    kira_amaci: str | None = Field(default="", description="sozlesmedeki kiralanan seyin ne amacla kiralandigi")


class SimdikiDurum(BaseNode):
    node_config: ClassVar[NodeModelConfig] = NodeModelConfig(
        node_tag="SimdikiDurum",
        description="""
            Kiralanan seyin simdiki durumunu gosterir. Kiralanan seyin mevcut durumu, onarim gerektirip gerektirmedigi,
            kiralanan seyin kullanilabilirligi, kiralanan seyin bakim gerektirip gerektirmedigi gibi bilgileri icerir. 
            """,
        cardinality=False,
    )
    simdiki_durum: str | None = Field(default="", description="sozlesmedeki kiralanan seyin simdiki durumu, onarim gerektirip gerektirmedigi, bakim gerektirip gerektirmedigi gibi bilgiler")


"""''

class FinansalUnsur(BaseNode):
    değer: str = Field(description="Finansal unsur değeri")
    tür: str = Field(description="")





class FesihMaddesi(BaseNode):
    açıklama: str = Field(description="Fesih maddesinin açıklaması")
    koşul: str = Field(description="Fesih maddesinin koşulu")
"""

# %%

#### Extract Nodes ####

# EXTRACTED_NODES = [
#     GeneralDocumentInfo(
#         reason="Metnin ilk sayfasında büyük harflerle ve tek başına ʻKİRA SÖZLEŞMESİʼ ibaresi yer alıyor. Bu ifade, sözleşmenin türünü ve başlığını açıkça belirtmektedir. Dolayısıyla sözleşme başlığı olarak bu ibare seçildi.",
#         sözleşme_başlığı="KİRA SÖZLEŞMESİ",
#     ),
#     Şirket(
#         reason="Metinde 'KİRAYA VEREN' başlığı altında tüzel kişi bilgileri (unvan, adres, Mersis No) verilmiş; vergi numarası ayrıca yer almadığından Mersis No vergi kimliği olarak alındı.",
#         unvan="Ankara Teknoloji Geliştirme Bölgesi Kurucu ve İşletici A.Ş. (Bilkent Cyberpark)",
#         vergi_no="0069 0206 6920 0011",
#         adres="Cyberplaza B Blok 1. Kat, 06800 Bilkent - Ankara",
#     ),
#     Şirket(
#         reason="Metinde 'KİRACI-1' başlığı altında şirket adı, açık adresi, Mersis ve vergi numarası belirtilmiş.",
#         unvan="C/S ENFORMASYON TEKNOLOJİLERİ LTD. ŞTİ.",
#         vergi_no="195 003 1078",
#         adres="Üniversiteler Mah. Beytepe Lodumlu Köy Yolu Cad. No: 5/208, Çankaya/Ankara",
#     ),
#     Şirket(
#         reason="Metinde 'KİRACI-2' başlığı altında şirket adı, açık adresi, Mersis ve vergi numarası belirtilmiş.",
#         unvan="SİBERTEK DANIŞMANLIK EĞİTİM VE YATIRIM ANONİM ŞİRKETİ",
#         vergi_no="770 013 3981",
#         adres="Ankara Teknoloji Geliştirme Bölgesi, Cyberpark Tepe Binası, Beytepe Lodumlu Köyü Yolu No: 5/234, Çankaya/Ankara",
#     ),
#     BaşlangıçTarihi(reason="Metinde “MADDE 2. KİRA BAŞLANGIÇ TARİHİ” başlığı altında “Kira başlangıç tarihi 01/01/2022 tarihidir.” ifadesi geçtiği için bu tarih kira sözleşmesinin başlangıç tarihi olarak seçildi.", değer="01/01/2022"),
#     BitişTarihi(reason="Metinde kira başlangıç tarihi 01/01/2022 olarak verilmiş ve sürenin 10 ay olduğu belirtilmiştir. Başlangıç tarihine 10 ay eklendiğinde sözleşme 31/10/2022 tarihinde sona erer.", değer="31/10/2022"),
#     FinansalUnsur(reason='MADDE 5.1\'de "Aylık kira bedeli; 44.456-TL +KDV’dir" ifadesi doğrudan TL para birimi içerdiği için finansal unsur olarak tespit edildi.', değer="44.456 TL + KDV", tür="Aylık kira bedeli"),
#     FinansalUnsur(reason='MADDE 6\'da "KİRACI 133.368-TL tutarında teminatı ... verecektir" cümlesi açık bir para tutarı içerdiğinden finansal unsur olarak çıkarıldı.', değer="133.368 TL", tür="Kira teminatı"),
#     FinansalUnsur(reason='MADDE 7\'de "aylık 19.737-TL +KDV ... ortak gider bedeli" ifadesi parasal bir yükümlülük olduğu için finansal unsur olarak kaydedildi.', değer="19.737 TL + KDV", tür="Aylık ortak gider bedeli"),
#     Mülkiyet(
#         reason="Metinde MADDE 4'te 'KİRALANAN' ifadesiyle mülkiyetin açık adresi ve 'toplam 918 m2’lik alan' bilgisi verildi. Mülkiyetin türü işyeri/ofis olarak tanımlandı. Metinde mülkiyetin parasal değeri belirtilmediği için 'Belirtilmemiş' ifadesi kullanıldı.",
#         değer="Belirtilmemiş",
#         tür="İşyeri (kiralanan ofis alanı)",
#         adres="Ankara Teknoloji Geliştirme Bölgesi, Üniversiteler Mahallesi, Şehit Mustafa Tayyarcan Caddesi, No:5, Cyberpark Tepe Binası, 2.Kat No: 208-234, 06800 Bilkent Çankaya/Ankara",
#         metrekare="918 m2",
#     ),
#     FesihMaddesi(
#         reason="Madde 12.2 ve 12.4'te 'Sözleşme’nin feshedilmesi' ibaresi ile KİRAYA VEREN’e fesih ve tahliye hakkı tanınmış; kullanım amacına aykırılık açıkça fesih sebebi olarak gösterilmiş.",
#         açıklama="KİRACI, kiralananı tahsis amacına aykırı veya hukuka aykırı şekilde kullanır ve 30 gün içinde aykırılığı gidermezse KİRAYA VEREN sözleşmeyi fesheder; KİRACI kira süresinin sonuna kadarki kira bedelleri tutarında cezai bedel öder.",
#         koşul="Kiralananın tahsis amacı dışında veya hukuka aykırı kullanılması ve aykırılığın 30 gün içinde giderilmemesi yahut giderilmesinin imkânsız olması.",
#     ),
#     FesihMaddesi(
#         reason="Madde 13.3–13.6’da temerrüt hâli ve 'sözleşmenin feshi ve tahliyesi' ifadeleri bulunuyor; kira bedelinin ödenmemesi fesih sebebi olarak düzenlenmiş.",
#         açıklama="KİRACI aylık kira bedelini ait olduğu ayın ilk 5 günü içinde ödemez veya ödemeler eksik kalırsa temerrüde düşer; KİRAYA VEREN ayrıca bildirim yapmaksızın sözleşmeyi feshedip kiralananı tahliye ettirebilir.",
#         koşul="Kira bedelinin tamamının süresinde (her ayın ilk 5 günü) ödenmemesi veya eksik ödenmesi.",
#     ),
#     FesihMaddesi(
#         reason="Madde 15.3'te teminatın verilmemesi / tamamlanmaması durumunda 'Sözleşmeyi fesih ve tahliye' hakkı açıkça tanınmış.",
#         açıklama="KİRACI, sözleşme imzasında öngörülen nakit/banka teminatını vermez, yenilemez veya eksik kısmı tamamlamazsa KİRAYA VEREN sözleşmeyi feshedebilir ve cezai bedel talep eder.",
#         koşul="Teminatın hiç verilmemesi, süresi içinde yenilenmemesi veya eksik kısmının tamamlanmaması.",
#     ),
#     FesihMaddesi(
#         reason="Madde 16.3–16.4’te yazılı onay alınmadan yapılan tadilatların 'akde aykırılık' sayılacağı ve bu nedenle fesih hakkı doğacağı belirtilmiş.",
#         açıklama="KİRACI, KİRAYA VEREN’in yazılı onayı olmaksızın kiralananda tadilat/tesisat/inşaat yaparsa KİRAYA VEREN sözleşmeyi feshedebilir, masrafları ve cezai bedeli tahsil eder.",
#         koşul="Kiralananda KİRAYA VEREN’in ön yazılı onayı olmadan herhangi bir tadilat, inşaat, dekorasyon yapılması.",
#     ),
#     FesihMaddesi(
#         reason="Madde 16.7’de işin süresinde bitirilmemesi hâlinde KİRAYA VEREN’e fesih imkânı tanınmış.",
#         açıklama="KİRACI onay verilmiş projeyi belirtilen sürede bitirmez veya verilen ek sürede de tamamlayamazsa KİRAYA VEREN sözleşmeyi feshedebilir; tamamlanmamış işleri masrafları KİRACI’ya ait olmak üzere kendisi yapabilir.",
#         koşul="Onaylı inşaat/tadilat işlerinin belirlenen veya ek verilen sürede tamamlanmaması.",
#     ),
#     FesihMaddesi(
#         reason="Madde 17.3’te bakım-onarım yükümlülüğünün yerine getirilmemesinin akde aykırılık olduğu, KİRAYA VEREN’in fesih hakkı olduğu ifade edilmiş.",
#         açıklama="KİRACI, sorumluluğundaki bakım ve onarım işlerini KİRAYA VEREN’in verdiği sürede yapmazsa KİRAYA VEREN sözleşmeyi feshedebilir ve giderleri KİRACI’dan tahsil eder.",
#         koşul="Bakım ve onarımın verilen süre içinde yapılmaması veya tehlikenin giderilmemesi.",
#     ),
#     FesihMaddesi(
#         reason="Madde 18.1–18.2’de mevzuata aykırılığın tekrarı hâlinde 'sözleşmeyi derhal feshedebilir' hükmü yer alıyor.",
#         açıklama="KİRACI Teknoloji Geliştirme Bölgesi mevzuatına ya da KİRAYA VEREN’in bildirimlerine uymaz ve uyarıya rağmen düzeltme yapmazsa sözleşme derhal feshedilir.",
#         koşul="Mevzuat hükümlerine uyulmaması veya istenen belge/formların süresinde sunulmaması ve aykırılığın devam etmesi.",
#     ),
#     FesihMaddesi(
#         reason="Madde 18.5’te denetime engel olunmasının 'açıkça akde aykırılık' sayıldığı ve derhal fesih sebebi olduğu belirtilmiş.",
#         açıklama="KİRACI, KİRAYA VEREN’in yapacağı olağan denetim ve incelemeleri engeller veya sonuçsuz bırakırsa KİRAYA VEREN sözleşmeyi derhal feshedebilir.",
#         koşul="KİRAYA VEREN’in önceden bildirerek yapacağı denetimi KİRACI’nın engellemesi, müdahale etmesi veya izin vermemesi.",
#     ),
#     FesihMaddesi(
#         reason="Madde 18.9’da kiralananın KİRACI’nın kusuruyla kullanılamaz hâle gelmesi hâlinde KİRAYA VEREN’in derhal fesih hakkı düzenlenmiş.",
#         açıklama="KİRACI’nın kusurundan kaynaklanan bir olay sonucu kiralanan kullanılamaz hâle gelirse KİRAYA VEREN sözleşmeyi derhal fesheder; KİRACI cezai bedel öder.",
#         koşul="Kiralananın KİRACI’nın kusuruyla kullanılamaz duruma gelmesi.",
#     ),
#     FesihMaddesi(
#         reason="Madde 20.2’de tüzel kişide hisse/yönetim değişikliği sonrası KİRAYA VEREN’e 30 gün önceden bildirimle fesih yetkisi verilmiş.",
#         açıklama="KİRACI tüzel kişiliğinin hâkim ortaklarının, yönetiminin değişmesi, birleşme veya nev’i değişikliği gibi durumlar ortaya çıktığında KİRAYA VEREN dilerse 30 gün önceden bildirerek sözleşmeyi feshedebilir.",
#         koşul="KİRACI şirketinde pay sahipliği veya kontrol yapısının değişmesi, birleşme, nev’i değişikliği vs. ve KİRAYA VEREN’in fesih bildirimi.",
#     ),
# ]
