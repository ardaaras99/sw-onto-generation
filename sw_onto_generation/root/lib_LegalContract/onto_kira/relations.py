from typing import ClassVar

from sw_onto_generation.base.base_relation import BaseRelation
from sw_onto_generation.base.configs import RelationModelConfig
from sw_onto_generation.common.common_nodes import GeneralDocumentInfo, Insan, Sirket
from sw_onto_generation.root.lib_LegalContract.onto_kira.nodes import (
    Demirbas,
    Demirbaslar,
    Depozito,
    KiraAmaci,
    KiraBedeli,
    KiraKonusuMulk,
    SimdikiDurum,
)


class HasKiralananMulk(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesme ile kiralanan mulku belirler. KiraKonusuMulk node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: KiraKonusuMulk


class HasKiraci(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sozlesmede yer alan kiracıyı belirler. Birden fazla kiracı olabilir. Kiraci Insan veya şirket olabilir, kiraci seklinde tanimlanabilir.",
        ask_llm=True,
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasKirayaVeren(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=True,
        description="Sozlesmede yer alan mulku kiraya vereni belirler. Birden fazla kiraya veren olabilir. Mal sahibi, kiraya veren olarak tanimlanabilir.kiraya veren Insan veya Sirket olabilir.",
        ask_llm=True,
    )
    source_node: GeneralDocumentInfo
    target_node: Insan | Sirket


class HasDepozito(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kira sozlesmesinde belirtilen depozitoyu gosterir. Sozlesmede bu bilgi varsa bu iliski kurulur. KiraDepozito node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Depozito


class HasKiraDemirbaslar(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmede demirbas olup olmadigini belirler. Demirbaslar nodundaki demirbas_var degeri true ise bu iliski kurulur Demirbaslar nodu yoksa veya False ise kurulmaz.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: Demirbaslar


class HasDemirbas(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Sozlesmede belirtilen demirbaslari KiraDemirbaslari node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: Demirbaslar
    target_node: Demirbas


class HasKiralamaBedeli(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kira sozlesmesinde belirtilen kira bedelidir. Kiracinin ne kadar odeyecegini belirler. KiraBedeli node'u ile iliskilendirir",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: KiraBedeli


class HasKiralamAmaci(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kiralanan seyin ne amacla kulkanilacagini belirtir. Sozlesmede bu bilgi varsa bu iliski kurulur. KiraAmaci node'u ile iliskilendirir",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: KiraAmaci


class HasSimdikiDurumu(BaseRelation):
    relation_config: ClassVar[RelationModelConfig] = RelationModelConfig(
        edge_index=False,
        description="Kiralanan seyin mevcut durumunu gosterir. Tamirat gerektiriyor mu, kiralanan seyin durumu nedir gibi bilgileri icerir. Sozlesmede bu bilgi varsa bu iliski kurulur. SimdikiDurum node'u ile iliskilendirir.",
        ask_llm=False,
    )
    source_node: GeneralDocumentInfo
    target_node: SimdikiDurum
