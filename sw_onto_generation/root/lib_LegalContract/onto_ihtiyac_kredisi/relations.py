from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_ihtiyac_kredisi.nodes import (
    ErkenOdemeCezasi,
    FaizBilgisi,
    GeriOdemePlani,
    Kefil,
    Kefiller,
    KrediAmaci,
    KrediTutari,
    Masraf,
    Masraflar,
    SigortaBilgisi,
    TahsisUcreti,
    VadeBilgisi,
)

# ---------------------------------------------------------------------------
# Birincil İlişkiler – GeneralDocumentInfo çıkışlı
# ---------------------------------------------------------------------------


class HasKrediTutari(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi sözleşmesindeki toplam kredi tutarını KrediTutari düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: KrediTutari


class HasFaizBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Krediye uygulanacak faiz bilgilerini FaizBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: FaizBilgisi


class HasVadeBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredinin vade süresini VadeBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: VadeBilgisi


class HasGeriOdemePlani(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi geri ödeme planını GeriOdemePlani düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: GeriOdemePlani


class HasKrediAmaci(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredinin kullanım amacını KrediAmaci düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: KrediAmaci


class HasTahsisUcreti(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi tahsis / dosya ücretini TahsisUcreti düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TahsisUcreti


class HasErkenOdemeCezasi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Erken ödeme cezasını ErkenOdemeCezasi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: ErkenOdemeCezasi


class HasSigortaBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi kapsamında yapılan sigorta bilgilerini SigortaBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SigortaBilgisi


class HasMasraflar(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Krediye ilişkin ek masraf bilgilerini Masraflar düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Masraflar


class HasKefiller(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi sözleşmesindeki kefil bilgilerini Kefiller düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Kefiller


class HasKrediAlan(BaseRelation):
    """Krediyi kullanan borçlu (gerçek veya tüzel kişi)."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Krediyi kullanan borçluyu Insan veya Sirket düğümü ile ilişkilendirir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasKrediSaglayan(BaseRelation):
    """Krediyi sağlayan banka / finans kuruluşu."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Krediyi sağlayan kurum veya bankayı Insan veya Sirket düğümü ile ilişkilendirir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasMasraf(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Masraflar düğümünü tek tek Masraf öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: Masraflar
    target_node: Masraf


class HasKefil(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kefiller düğümünü tek tek Kefil öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: Kefiller
    target_node: Kefil
