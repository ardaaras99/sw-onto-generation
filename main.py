# %%
from rich import print as rprint

from sw_onto_generation.Ontologies.Base.base_node import BaseNode
from sw_onto_generation.Ontologies.Base.base_relation import BaseRelation
from sw_onto_generation.Ontologies.Specific.LegalContracts.KiraContract.relations import HasKiracı

rprint(BaseNode.node_config)
rprint(BaseRelation.relation_config)
rprint(HasKiracı.relation_config)

# %%
