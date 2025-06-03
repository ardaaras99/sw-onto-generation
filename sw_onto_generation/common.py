# %%
from typing import ClassVar

from pydantic import Field

from sw_onto_generation.base_node import BaseNode
from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, NodeProp, SearchType


class GeneralDocumentInfo(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=[
                NodeProp(dgraph_type="generalDocumentInfo"),
                NodeProp(dgraph_type="generalDocumentInfo2"),
            ],
            field_props=[FieldProp(field_name="documan_ismi", search_type=SearchType.VECTOR)],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
            cardinality=False,
        ),
    }

    documan_ismi: str = Field(description="Belgenin başlığı")


class Adres(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="Adres"), field_props=[FieldProp(field_name="il", search_type=SearchType.EXACT), FieldProp(field_name="ilçe", search_type=SearchType.EXACT)]
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="adres bilgilerini tanımlar. Adres, cadde, sokak, mahalle, apartman, ilçe, il ve posta kodu gibi bilgileri içerebilir.",
            cardinality=True,
        ),
    }
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
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="Insan"),
            field_props=[
                FieldProp(field_name="tckn", search_type=SearchType.EXACT),
                FieldProp(field_name="soyad", search_type=SearchType.TERM),
                FieldProp(field_name="ad", search_type=SearchType.TERM),
            ],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="Döküman icinde bulunan gercek kisileri yani insanlari tanimlar. Bu insanlar, sözleşmeyi imzalayan veya sözleşmede adı geçen gerçek kişilerdir.",
            cardinality=True,
        ),
    }

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
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="Sirket"), field_props=[FieldProp(field_name="vkn", search_type=SearchType.EXACT), FieldProp(field_name="unvan", search_type=SearchType.TERM)]
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="Döküman icinde bulunan tuzel kisileri yani sirketler, kamukurumlari, dernekler, vakiflar veya organizasyonlari tanimlar. Bu sirketler, sözleşmeyi imzalayan veya sözleşmede adı geçen tuzel kişilerdir.",
            cardinality=True,
        ),
    }
    unvan: str = Field(description="Şirketin ticaret unvani, resmi adı")
    vkn: str = Field(description="Şirketin vergi kimlik numarası, vergi numarası, 10 haneli bir sayı olmalıdır")
    adres: Adres = Field(description="Şirketin adresi, işyeri adresi. Cadde, sokak, il, ilce, mahelle, kapi no, posta kodu, ulke gibi bilgiler içerebilir")
    kepadresi: str | None = Field(default=None, description="Şirketin KEP (Kayıtlı Elektronik Posta) adresi, resmi yazışmalar için kullanılabilir")
    mersisno: str | None = Field(default=None, description="Şirketin MERSİS numarası, Türkiye'de ticaret sicil kaydı için kullanılan numara")


class SozlesmeBaslangicTarihi(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="SozlesmeBaslangicTarihi"),
            field_props=[FieldProp(field_name="baslangic_tarihi", search_type=SearchType.EXACT)],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="""
                Documanin baslangic tarihini belirler.Cogunlukla sozlesmenin baslangic tarihi, sozlesmenin imzalandigi tarih veya sozlesmenin yurutulecegi tarih olarak kullanilir. 
                Kesin bir tarih olabilecegi gibi imzalandigi tarihte gecerli olacagi da belirtilebilir. Bu durumda 0000-00-00 olarak doldurun lutfen
                """,
            cardinality=True,
        ),
    }

    baslangic_tarihi: str = Field(description="Sozlesmenin başlangıç tarihi, sözleşmenin yürürlüğe girdiği tarih. YYYY-MM-DD formatında doldurun lutfen.")


class SozlesmeBitisTarihi(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="SozlesmeBitisTarihi"),
            field_props=[
                FieldProp(field_name="bitis_tarihi", search_type=SearchType.EXACT),
            ],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="""
                Documanin gecerli oldugu tarihin sonunu belirtir. Cogunlukle Bitis tarihi olarak belirtilir. Kesin bir tarih verilmeyip Baslangic tarihinden itibaren bir sure de belirtilebilir.
                """,
            cardinality=True,
        ),
    }

    bitis_tarihi: str = Field(description="Sozlesmenin bitis tarihi, sözleşmenin sona erdigi tarih. YYYY-MM-DD formatında doldurun lutfen.")


# %%
# Finansal Miktar, Fesih Maddesi, Sözleşme Maddesi, Mülkiyet
# HasKiracıTaraf, HasKirayaVerenTaraf, HasBitişTarihi, HasBaşlangıçTarihi, HasFinansalMiktar, HasFesihMaddesi, HasSözleşmeMaddesi, BitişTarihiniEtkiler
