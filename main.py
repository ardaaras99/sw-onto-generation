# %%
# import every class in Base, Common and SpecificOntologies to see they can build

from rich import print as rprint

from sw_onto_generation.Base.base_node import BaseNode
from sw_onto_generation.Base.base_relation import BaseRelation
from sw_onto_generation.Common.common_nodes import Adres, GeneralDocumentInfo, Insan, Sirket, SozlesmeBaslangicTarihi, SozlesmeBitisTarihi
from sw_onto_generation.Common.common_relations import HasKiracı

rprint(BaseNode.node_config)
rprint(BaseRelation.relation_config)
rprint(HasKiracı.relation_config)

# %%
