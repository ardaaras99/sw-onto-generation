from __future__ import annotations

from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_abonelik.nodes import (
    AbonelikBedeli,
    BildirimBilgisi,
    CaymaBedeli,
    Donanim,
    Donanimlar,
    EkSozlesme,
    EkSozlesmeler,
    EkUcret,
    EkUcretler,
    FaturaBilgisi,
    GecikmeFaizi,
    HizmetSeviyesi,
    KampanyaBilgisi,
    KurulumBedeli,
    ServisKesinti,
    TaahhutIhlalKosullari,
    TaahhutKapsamiHizmet,
    TaahhutKapsamiHizmetler,
    Taahhutname,
    TaksitSecenegi,
)


# New Taahhütname relations
class HasTaahhutname(BaseRelation):
    """Sözleşme ile taahhütname bilgilerini ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sözleşme ile taahhütname bilgilerini Taahhutname düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Taahhutname


class HasTaahhutEkSozlesmeler(BaseRelation):
    """Taahhütname ile ek sözleşmelerin varlığını ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Taahhütname ile ek sözleşmelerin varlığını EkSozlesmeler düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: EkSozlesmeler


class HasEkSozlesme(BaseRelation):
    """Ek sözleşmeler ile tek tek ek sözleşmeleri ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="EkSozlesmeler düğümünü tek tek EkSozlesme öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: EkSozlesmeler
    target_node: EkSozlesme


class HasTaahhutKapsamiHizmetler(BaseRelation):
    """Taahhüt kapsamında hizmetlerin varlığını ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Taahhüt kapsamında hizmetlerin varlığını TaahhutKapsamiHizmetler düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TaahhutKapsamiHizmetler


class HasTaahhutKapsamiHizmet(BaseRelation):
    """Taahhüt kapsamı hizmetler ile tek tek hizmetleri ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="TaahhutKapsamiHizmetler düğümünü tek tek TaahhutKapsamiHizmet öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: TaahhutKapsamiHizmetler
    target_node: TaahhutKapsamiHizmet


class HasDonanimlar(BaseRelation):
    """Donanım bilgilerinin varlığını ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Donanım bilgilerinin varlığını Donanimlar düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: Donanimlar


class HasDonanim(BaseRelation):
    """Donanımlar ile tek tek donanım bilgilerini ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Donanimlar düğümünü tek tek Donanim öğeleriyle ilişkilendirir.",
        ask_llm=False,
    )

    source_node: Donanimlar
    target_node: Donanim


class HasTaahhutIhlalKosullari(BaseRelation):
    """Taahhüt ihlal koşullarını ilişkilendirir."""

    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Taahhüt ihlal koşullarını TaahhutIhlalKosullari düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: TaahhutIhlalKosullari


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


class HasHizmetSeviyesi(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Hizmet seviyesi (SLA / QoS) parametrelerini HizmetSeviyesi düğümü ile ilişkilendirir.",
        ask_llm=False,
    )

    source_node: GeneralDocumentInfo
    target_node: HizmetSeviyesi


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


class HasTaksitSecenegi(BaseRelation):
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
