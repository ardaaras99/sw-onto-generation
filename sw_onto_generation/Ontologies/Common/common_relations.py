from typing import ClassVar

from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Base.configs import RelationModelConfig
from sw_onto_generation.Ontologies.Common.common_nodes import (
    Ek,
    Ekler,
    GeneralDocumentInfo,
    Kefil,
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
        edge_type="has_yururluk",
        edge_index=False,
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeYururluk


class SozlesmeKonusu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin konusunu. SozlesmeKonu node'u ile iliskilendirir.",
        edge_type="has_sozlesmekonusu",
        edge_index=False,
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeKonu


class BaslangicTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin basladigi tarihi belirler",
        edge_type="has_baslangictarihi",
        edge_index=True,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBaslangicTarihi


class BitisTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin bitigi, sonlandigi tarihi belirler",
        edge_type="has_bitistarihi",
        edge_index=True,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBitisTarihi


class SozlesmeSuresi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin suresini belirler. Sozlesmenin baslangic ve bitis tarihleri arasindaki sureyi ifade eder.",
        edge_type="has_sozlesmesuresi",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeSure


class SozlesmeTeminatlari(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilip belitilmedigini belirler. Teminatlar nodundaki teminat_var degeri true ise bu iliski kurulur Teminatlar nodu yoksa veya False ise kurulmaz.",
        edge_type="has_sozlesmeteminatlari",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Teminatlar


class TeminatListesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilmise bunlari SozlesmeTeminatlari node'u ile iliskilendirir.",
        edge_type="has_teminat",
        edge_index=False,
        ask_llm=False,
    )
    source_node: Teminatlar
    target_node: Teminat


class SozlesmeUyusmazlikCozumYeri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede uyusmazlik durumunda cozum yerini belirler. UyusmazlikCozumYeri node'u ile iliskilendirir.",
        edge_type="has_uyusmazlikcozumyeri",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: UyusmazlikCozumYeri


class Kefalet(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin kefillerini belirler. Sozlesmede kefil varsa bu iliski kurulur.",
        edge_type="has_kefalet",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Kefil


class SozlesmeEkleri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede ek olup olmadigini belirler. Ekler nodundaki ek_var degeri true ise bu iliski kurulur Ekler nodu yoksa veya False ise kurulmaz.",
        edge_type="has_sozlesmeteminatlari",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Ekler


class EkListesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede Ek belirtilmise bunlari SozlesmeEkleri node'u ile iliskilendirir.",
        edge_type="has_ek",
        edge_index=False,
        ask_llm=False,
    )
    source_node: Ekler
    target_node: Ek
