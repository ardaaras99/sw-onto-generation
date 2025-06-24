from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_ihtiyac_kredisi.nodes import (
    CaymaHakki,
    ErkenOdemeCezasi,
    FaizBilgisi,
    GeriOdemePlani,
    KrediAmaci,
    KrediTutari,
    Masraf,
    Masraflar,
    SigortaBilgisi,
    TahsisUcreti,
    TemerrutBilgisi,
    TeminatBilgisi,
    VadeBilgisi,
)


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
    """Kredi sözleşmesinde kefil olup olmadığını gösterir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Kredi sözleşmesinde kefil olup olmadığını gösterir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasTemerrutBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Ödeme gecikmesi (temerrüt) hâlinde uygulanacak hükümleri TemerrutBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TemerrutBilgisi


class HasCaymaHakki(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi kullanımından cayma koşullarını CaymaHakki düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: CaymaHakki


class HasTeminatBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi sözleşmesindeki teminat bilgilerini TeminatBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TeminatBilgisi


# Supporting relations for additional information
class KrediAlanBilgileri(BaseRelation):
    """Connects loan recipient to additional personal info if needed."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kredi alan ile ek kişisel bilgilerini ilişkilendirir.",
        ask_llm=False,
    )

    source_node: Insan | Sirket
    target_node: GeneralDocumentInfo


class TeminatSahibi(BaseRelation):
    """Relates collateral to its owner."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Teminatın sahibini belirler. Teminat ile sahip kişi/kuruluş arasındaki ilişkiyi tanımlar.",
        ask_llm=True,
    )

    source_node: TeminatBilgisi
    target_node: Insan | Sirket
