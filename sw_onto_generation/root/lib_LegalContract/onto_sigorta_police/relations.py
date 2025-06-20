from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_sigorta_police.nodes import (
    Acente,
    AciklamaVeOzelSartlar,
    Arac,
    Hasarkaydi,
    IndirimArtis,
    OzelSart,
    SigortaEttiren,
    SigortaKonusu,
    SigortaliKisi,
    SigortaPolice,
    SigortaPrimi,
    SigortaSirketi,
    TeminatKapsami,
)


class HasSigortaPolice(BaseRelation):
    """Relates contract to insurance policy information."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme ile sigorta poliçesi bilgilerini ilişkilendirir. SigortaPolice node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SigortaPolice


class HasSigortali(BaseRelation):
    """Relates contract to insured person/entity."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan sigortalıyı belirler. Sigortalı kişi veya kuruluş olabilir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasSigortaEttiren(BaseRelation):
    """Relates contract to insurance contractor."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan sigorta ettireni belirler. Sigorta sözleşmesini yapan taraftır.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasSigortaSirketi(BaseRelation):
    """Relates contract to insurance company."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmede yer alan sigorta şirketini belirler. Sigorta hizmetini veren kuruluştur.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Sirket


class HasAcente(BaseRelation):
    """Relates contract to insurance agent."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmede yer alan sigorta acentesini belirler. Poliçeyi düzenleyen acente veya broker bilgilerini Acente node'u ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Acente


class HasSigortaKonusu(BaseRelation):
    """Relates contract to subject of insurance."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta konusunu belirler. Sigortalanan mal, eşya veya risk alanını SigortaKonusu node'u ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SigortaKonusu


class HasArac(BaseRelation):
    """Relates contract to vehicle information."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Araç sigortalarında araç bilgilerini ilişkilendirir. Arac node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Arac


class HasTeminatKapsami(BaseRelation):
    """Relates contract to coverage scope."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta kapsamındaki teminatları ilişkilendirir. TeminatKapsami node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TeminatKapsami


class HasSigortaPrimi(BaseRelation):
    """Relates contract to insurance premium."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta primi ve ödeme bilgilerini ilişkilendirir. SigortaPrimi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: SigortaPrimi


class HasHasarKaydi(BaseRelation):
    """Relates contract to damage history."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta geçmişindeki hasar kayıtlarını ilişkilendirir. Hasarkaydi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Hasarkaydi


class HasIndirimArtis(BaseRelation):
    """Relates contract to discounts and surcharges."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta primindeki indirim ve artışları ilişkilendirir. IndirimArtis node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: IndirimArtis


class HasOzelSart(BaseRelation):
    """Relates contract to special conditions."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta poliçesindeki özel şartları ilişkilendirir. OzelSart node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: OzelSart


class HasAciklamaVeOzelSartlar(BaseRelation):
    """Relates contract to general explanations and special conditions."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Poliçedeki genel açıklamalar ve özel şartları ilişkilendirir. AciklamaVeOzelSartlar node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: AciklamaVeOzelSartlar


class HasLehtar(BaseRelation):
    """Relates contract to beneficiary."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sigorta lehdarını belirler. Özellikle hayat sigortası ve rehinli araçlarda önemlidir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


# Supporting relations for detailed information
class SigortaliInfo(BaseRelation):
    """Connects insured person to additional info."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigortalı kişi ile ek bilgilerini ilişkilendirir. SigortaliKisi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: Insan | Sirket
    target_node: SigortaliKisi


class SigortaEttirenInfo(BaseRelation):
    """Connects insurance contractor to additional info."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta ettiren ile ek bilgilerini ilişkilendirir. SigortaEttiren node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: Insan | Sirket
    target_node: SigortaEttiren


class SigortaSirketiInfo(BaseRelation):
    """Connects insurance company to additional info."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta şirketi ile ek bilgilerini ilişkilendirir. SigortaSirketi node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: Sirket
    target_node: SigortaSirketi


class AcenteBilgisi(BaseRelation):
    """Connects insurance company to agent information."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sigorta şirketi ile acente bilgilerini ilişkilendirir. Acente node'u ile bağlantı sağlar.",
        ask_llm=False,
    )

    source_node: Sirket
    target_node: Acente


class VehicleOwnership(BaseRelation):
    """Relates vehicle to its owner."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Aracın sahibini belirler. Araç ile sahip kişi/kuruluş arasındaki ilişkiyi tanımlar.",
        ask_llm=True,
    )

    source_node: Arac
    target_node: Insan | Sirket


class PoliceCoverage(BaseRelation):
    """Relates policy to specific coverage items."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Poliçe ile belirli teminat kapsamları arasındaki ilişkiyi tanımlar.",
        ask_llm=False,
    )

    source_node: SigortaPolice
    target_node: TeminatKapsami


class PolicyPremium(BaseRelation):
    """Relates policy to its premium structure."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Poliçe ile prim yapısı arasındaki ilişkiyi tanımlar.",
        ask_llm=False,
    )

    source_node: SigortaPolice
    target_node: SigortaPrimi


class PolicyDiscounts(BaseRelation):
    """Relates policy to discounts and surcharges."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Poliçe ile indirim/artış uygulamaları arasındaki ilişkiyi tanımlar.",
        ask_llm=False,
    )

    source_node: SigortaPolice
    target_node: IndirimArtis
