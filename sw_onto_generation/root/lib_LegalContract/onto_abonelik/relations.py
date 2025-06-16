from __future__ import annotations

from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_abonelik.nodes import (
    AbonelikBedeli,
    AbonelikHizmeti,
    AbonelikNumarasi,
    BildirimBilgisi,
    CaymaBedeli,
    Ekipman,
    Ekipmanlar,
    EkUcret,
    EkUcretler,
    FaturaBilgisi,
    GecikmeFaizi,
    HizmetSeviyesi,
    KampanyaBilgisi,
    KurulumBedeli,
    ServisKesinti,
    TaksitSecenegi,
)


class HasAbonelikHizmeti(BaseRelation):
    """Sözleşme kapsamında sağlanan hizmeti belirtir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme kapsamında sağlanan hizmeti AbonelikHizmeti düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: AbonelikHizmeti


class HasAbone(BaseRelation):
    """Sözleşmedeki aboneyi (tüketici / son kullanıcı) ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmedeki aboneyi (tüketici / son kullanıcı) Insan veya Sirket düğümü ile ilişkilendirir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasHizmetSaglayici(BaseRelation):
    """Sözleşmedeki hizmet sağlayıcıyı ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sözleşmedeki hizmet sağlayıcıyı Insan veya Sirket düğümü ile ilişkilendirir.",
        ask_llm=True,
    )

    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasAbonelikBedeli(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Abonelik için ödenecek periyodik ücreti AbonelikBedeli düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: AbonelikBedeli


class HasKurulumBedeli(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kurulum / aktivasyon ücretini KurulumBedeli düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: KurulumBedeli


class HasCaymaBedeli(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Taahhüt süresi dolmadan fesih hâlinde uygulanacak cayma bedelini CaymaBedeli düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: CaymaBedeli


class HasAbonelikEkipmanlar(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşmede ekipman tahsisi olup olmadığını Ekipmanlar düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Ekipmanlar


class HasHizmetSeviyesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Hizmet seviyesi (SLA / QoS) parametrelerini HizmetSeviyesi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: HizmetSeviyesi


class HasAbonelikNumarasi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Abonelik / müşteri numarasını AbonelikNumarasi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: AbonelikNumarasi


class HasFaturaBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Fatura bilgilerini FaturaBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: FaturaBilgisi


class HasEkUcretler(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Ek ücretler düğümünü EkUcretler düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: EkUcretler


class HasKampanyaBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kampanya / promosyon bilgilerini KampanyaBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: KampanyaBilgisi


class HasBildirimBilgisi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Bildirim bilgilerini BildirimBilgisi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: BildirimBilgisi


class HasGecikmeFaizi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Gecikme faizi bilgilerini GecikmeFaizi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: GecikmeFaizi


class HasServisKesinti(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Servis kesintisi / tazminat bilgilerini ServisKesinti düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: ServisKesinti


class HasEkipman(BaseRelation):
    """Ekipmanlar düğümünden tek tek ekipman öğelerine ilişki."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Ekipmanlar düğümünü tek tek Ekipman öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: Ekipmanlar
    target_node: Ekipman


class HasTaksitSecenegi(BaseRelation):
    """AbonelikBedeli düğümünden taksit seçenekleri düğümüne ilişki."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Abonelik bedelini TaksitSecenegi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: AbonelikBedeli
    target_node: TaksitSecenegi


class HasEkUcret(BaseRelation):
    """EkUcretler düğümünden tek tek ek ücret öğelerine ilişki."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="EkUcretler düğümünü tek tek EkUcret öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: EkUcretler
    target_node: EkUcret
