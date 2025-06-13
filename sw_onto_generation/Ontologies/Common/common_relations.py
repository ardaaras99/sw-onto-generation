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


class HasYururluk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin yururlukte olup olmadigini belirler. SozlesmeYururluk node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeYururluk


class HasSozlesmeKonusu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin konusunu. SozlesmeKonu node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeKonu


class HasBaslangicTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin basladigi tarihi belirler",
        edge_index=True,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBaslangicTarihi


class HasBitisTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin bitigi, sonlandigi tarihi belirler",
        edge_index=True,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBitisTarihi


class HasSozlesmeSuresi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin suresini belirler. Sozlesmenin baslangic ve bitis tarihleri arasindaki sureyi ifade eder.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeSure


class HasTeminatlar(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilip belitilmedigini belirler. Bir tane teminat olursa bu iliski kurulur. Teminatlar node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Teminatlar


class HasTeminat(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede teminat belirtilmise bunlari HasTeminatlar node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: Teminatlar
    target_node: Teminat


class HasSozlesmeUyusmazlikCozumYeri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede uyusmazlik durumunda cozum yerini belirler. UyusmazlikCozumYeri node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: UyusmazlikCozumYeri


class HasKefalet(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmenin kefillerini belirler. Sozlesmede kefil varsa bu iliski kurulur.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Kefil


class HasSozlesmeEkler(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede ek olup olmadigini belirler. Mutlaka Ek olarak belirtilmesi gerekir. Ekler node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Ekler


class HasEk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        description="Sozlesmede Ek belirtilmise bunlari Ekler node'u ile iliskilendirir.",
        edge_index=False,
        ask_llm=False,
    )
    source_node: Ekler
    target_node: Ek
