from typing import ClassVar

from pydantic.fields import FieldInfo

from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import (
    GeneralDocumentInfo,
    SozlesmeBaslangicTarihi,
    SozlesmeBitisTarihi,
    SozlesmeKonu,
    SozlesmeSure,
    SozlesmeYururluk,
    Teminat,
    Teminatlar,
    UyusmazlikCozumYeri,
)


class Yururluk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin yururlukte olup olmadigini belirler. SozlesmeYururluk node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="yururluk"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeYururluk


class SozlesmeKonusu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin konusunu. SozlesmeKonu node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="sozlesme_konusu"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeKonu


class BaslangicTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin basladigi tarihi belirler",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="baslangic_tarihi"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBaslangicTarihi


class BitisTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin bitigi, sonlandigi tarihi belirler",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="bitis_tarihi"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBitisTarihi


class SozlesmeSuresi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin suresini belirler. Sozlesmenin baslangic ve bitis tarihleri arasindaki sureyi ifade eder.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="sozlesme_suresi"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
        field_configs=[FieldConfig(field_name="relation_type", search_type=NebulaIndexType.EXACT)],
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeSure


class SozlesmeTeminatlari(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilip belitilmedigini belirler. Teminatlar nodundaki teminat_var degeri true ise bu iliski kurulur Teminatlar nodu yoksa veya False ise kurulmaz.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="teminatlar"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: Teminatlar


class TeminatListesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilmise bunlari SozlesmeTeminatlari node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_name", annotation=str, default="teminat_listesi")],
    )
    source_node: Teminatlar
    target_node: Teminat


class SozlesmeUyusmazlikCozumYeri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede uyusmazlik durumunda cozum yerini belirler. UyusmazlikCozumYeri node'u ile iliskilendirir.",
        extra_fields=[FieldInfo(alias="relation_type", annotation=str, default="uyusmazlik_yeri"), FieldInfo(alias="relation_name", annotation=str, default="has_relation")],
    )
    source_node: GeneralDocumentInfo
    target_node: UyusmazlikCozumYeri
