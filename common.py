# %%
from typing import ClassVar

from pydantic import BaseModel, Field

from base import BaseNode
from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, NodeProp, SearchType


class GeneralDocumentInfo(BaseNode):
    update_dict: ClassVar[dict] = {
        DGraphProps.__name__: DGraphProps(
            node_prop=NodeProp(dgraph_type="generalDocumentInfo"),
            field_props=[FieldProp(field_name="baslik", search_type=SearchType.VECTOR)],
        ),
        LLMHelperProps.__name__: LLMHelperProps(
            description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
        ),
    }
    baslik: str = Field(description="Belgenin başlığı")


# rprint("BaseNode model config")
# rprint(BaseNode.model_config)
# rprint("GeneralDocumentInfo model config")
# rprint(GeneralDocumentInfo.model_config)
# %%


class Adres(BaseModel):
    cadde: str = Field(description="Adresin cadde veya sokak adı")
    mahalle: str = Field(description="Adresin bulunduğu mahalle")
    apartman: str = Field(description="Adresin bulunduğu apartman adi veya numarasi veya kapi numarası veya her ikisi de olabilir")
    ilçe: str = Field(description="Adresin bulunduğu ilçe")
    il: str = Field(description="Adresin bulunduğu il")
    posta_kodu: str = Field(description="Adresin posta kodu")


class Insan(BaseNode):
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


class Sirket(BaseNode):
    unvan: str = Field(description="Şirketin ticaret unvani, resmi adı")
    vkn: str = Field(description="Şirketin vergi kimlik numarası, vergi numarası, 10 haneli bir sayı olmalıdır")
    adres: Adres = Field(description="Şirketin adresi, işyeri adresi")


# %%
