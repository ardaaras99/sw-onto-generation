from typing import ClassVar

from pydantic.fields import FieldInfo

from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Base.configs import FieldConfig, NebulaIndexType, RelationModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import GeneralDocumentInfo, SozlesmeBaslangicTarihi, SozlesmeBitisTarihi, SozlesmeKonu, SozlesmeYururluk


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
