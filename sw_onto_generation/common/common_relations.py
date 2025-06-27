from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import (
    Ek,
    Ekler,
    FaizMaddeleri,
    FaizMaddesi,
    FesihMaddeleri,
    FesihMaddesi,
    GeneralDocumentInfo,
    Insan,
    Istisna,
    Istisnalar,
    Sirket,
    SozlesmeBaslangicTarihi,
    SozlesmeBitisTarihi,
    SozlesmeKonu,
    SozlesmeSure,
    SozlesmeYururluk,
    UyusmazlikCozumYeri,
)


class HasYururluk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmenin yururlukte olup olmadigini belirler. SozlesmeYururluk node'u ile iliskilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeYururluk


class HasSozlesmeKonusu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmenin konusunu. SozlesmeKonu node'u ile iliskilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SozlesmeKonu


class HasBaslangicTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sozlesmenin basladigi tarihi belirler",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBaslangicTarihi


class HasBitisTarihi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sozlesmenin bitigi, sonlandigi tarihi belirler",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeBitisTarihi


class HasSozlesmeSuresi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmenin suresini belirler. Sozlesmenin baslangic ve bitis tarihleri arasindaki sureyi ifade eder.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SozlesmeSure


class HasSozlesmeUyusmazlikCozumYeri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmede uyusmazlik durumunda cozum yerini belirler. UyusmazlikCozumYeri node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: UyusmazlikCozumYeri


class HasKefil(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmenin kefillerini belirler. Sozlesmede kefil varsa bu iliski kurulur.",
        ask_llm=True,
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasSozlesmeEkler(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmede ek olup olmadigini belirler. Mutlaka Ek olarak belirtilmesi gerekir. Ekler node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Ekler


class HasEk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmede Ek belirtilmise bunlari Ekler node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: Ekler
    target_node: Ek


class HasFesihMaddeleri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmede fesih maddelerinin bulunup bulunmadığını belirtir. FesihMaddeleri düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: FesihMaddeleri


class HasFesihMaddesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmedeki her bir fesih maddesini FesihMaddeleri düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: FesihMaddeleri
    target_node: FesihMaddesi


class HasFaizMaddeleri(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmede faiz maddelerinin bulunup bulunmadığını belirtir. FaizMaddeleri düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: FaizMaddeleri


class HasFaizMaddesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmedeki her bir faiz maddesini FaizMaddeleri düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: FaizMaddeleri
    target_node: FaizMaddesi


class HasIstisnalar(BaseRelation):
    """Relates contract to insurance premium."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kasko priminde uygulanan istisnaları ilişkilendirir. Istisnalar node'u ile bağlantı sağlar.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Istisnalar


class HasIstisna(BaseRelation):
    """Relates contract to insurance premium."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kasko priminde uygulanan istisnaları ilişkilendirir. Istisna node'u ile bağlantı sağlar.",
        ask_llm=False,
    )
    source_node: Istisnalar
    target_node: Istisna
