from typing import ClassVar

from pydantic.fields import FieldInfo

from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.Ontologies.Specific.LegalContracts.KiraContract.KiraContracts_nodes import Demirbas, Demirbaslar, KiraAmaci, KiraBedeli, KiraDepozito, KiraKonusuMulk, SimdikiDurum


class KiralananMulk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesme ile kiralanan mulku belirler. KiraKonusuMulk node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="kiralanan_mulk"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: KiraKonusuMulk


class Kiraci(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede yer alan kiracıyı belirler. Birden fazla kiracı olabilir. Kiraci Insan veya şirket olabilir, kiraci seklinde tanimlanabilir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="kiracı"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class KirayaVeren(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede yer alan mulku kiraya vereni belirler. Birden fazla kiraya veren olabilir. Mal sahibi, kiraya veren olarak tanimlanabilir.kiraya veren Insan veya Sirket olabilir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="kiraya_veren"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class Depozito(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="""
        Kira sozlesmesinde belirtilen depozitoyu gosterir. .
        Sozlesmede bu bilgi varsa bu iliski kurulur. KiraDepozito node'u ile iliskilendirir.
        """,
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="depozito"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: KiraDepozito


class KiraDemirbaslari(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede demirbas olup olmadigini belirler. Demirbaslar nodundaki demirbas_var degeri true ise bu iliski kurulur Demirbaslar nodu yoksa veya False ise kurulmaz.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="demirbaslar"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: Demirbaslar


class DemirbasListesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede belirtilen demirbaslari KiraDemirbaslari node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_name", annotation=str, default="demirbas_listesi")],
    )
    source_node: Demirbaslar
    target_node: Demirbas


class KiralamaBedeli(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Kira sozlesmesinde belirtilen kira bedelidir. Kiracinin ne kadar odeyecegini belirler. KiraBedeli node'u ile iliskilendirir",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="kira_bedeli"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: KiraBedeli


class KiralamAmaci(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Kiralanan seyin ne amacla kulkanilacagini belirtir. Sozlesmede bu bilgi varsa bu iliski kurulur. KiraAmaci node'u ile iliskilendirir",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="kira_amaci"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: KiraAmaci


class SimdikiDurumu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="""
        Kiralanan seyin mevcut durumunu gosterir. Tamirat gerektiriyor mu, kiralanan seyin durumu nedir gibi bilgileri icerir.
        Sozlesmede bu bilgi varsa bu iliski kurulur. SimdikiDurum node'u ile iliskilendirir.
        """,
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="simdiki_durum"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: SimdikiDurum
