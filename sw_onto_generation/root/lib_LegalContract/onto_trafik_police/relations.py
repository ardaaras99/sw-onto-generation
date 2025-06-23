from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_trafik_police.nodes import (
    Acente,
    Arac,
    SigortaPrimi,
    Teminat,
    Teminatlar,
    TrafikPolice,
)


class HasTrafikPolice(BaseRelation):
    """Relates contract to insurance policy information."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme ile trafik poliçesi bilgilerini ilişkilendirir. TrafikPolice node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TrafikPolice


class HasOncekiAcente(BaseRelation):
    """Relates contract to previous insurance agent."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme ile önceki trafik poliçesi acentesini ilişkilendirir. OncekiAcente node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Acente


class HasAcente(BaseRelation):
    """Relates contract to insurance agent."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmede yer alan trafik poliçesi acentesini belirler. Poliçeyi düzenleyen acente veya broker bilgilerini Acente node'u ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Acente


class HasSigortali(BaseRelation):
    """Relates contract to insured person/entity."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan sigortalıyı belirler. Sigortalı gerçek kişi veya kuruluş olabilir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasDuzenleyenKisi(BaseRelation):
    """Relates contract to insurance contractor."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan trafik poliçesi düzenleyen acentede çalışan kişiyi belirler. Trafik poliçesi sözleşmesini yapan taraftır.",
        ask_llm=True,
    )

    source_node: Acente
    target_node: Insan


class HasTrafikPoliceEttiren(BaseRelation):
    """Relates contract to insurance contractor."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan trafik poliçesi ettiren kisiyi belirler. Trafik poliçesi sözleşmesini yapan taraftır.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasTrafikPoliceSigortaSirketi(BaseRelation):
    """Relates contract to insurance company."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan trafik poliçesi veren şirketi belirler. Trafik poliçesi hizmetini veren sigorta şirketidir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Sirket


class HasEskiTrafikPoliceSigortaSirketi(BaseRelation):
    """Relates contract to previous insurance company."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme ile önceki trafik poliçesi veren şirketi ilişkilendirir. EskiSigortaSirketi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Sirket


class HasArac(BaseRelation):
    """Relates contract to vehicle information."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Trafik poliçesinde sigortalanan araç bilgilerini ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Arac


class HasTeminatlar(BaseRelation):
    """Relates contract to coverage scope."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta kapsamındaki teminatları ilişkilendirir. Teminatlar node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Teminatlar


class HasTeminat(BaseRelation):
    """Relates contract to coverage scope."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta kapsamındaki teminatları ilişkilendirir. Teminat node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: Teminatlar
    target_node: Teminat


class HasSigortaPrimi(BaseRelation):
    """Relates contract to insurance premium."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta primi ve ödeme bilgilerini ilişkilendirir. SigortaPrimi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SigortaPrimi


class HasAracSahibi(BaseRelation):
    """Relates vehicle to its owner."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Aracın sahibini belirler. Araç ile sahip kişi/kuruluş arasındaki ilişkiyi tanımlar.",
        ask_llm=True,
    )

    source_node: Insan | Sirket
    target_node: Arac
