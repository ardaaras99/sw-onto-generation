# %%
from rich import print as rprint

from sw_onto_generation.common import GeneralDocumentInfo, Sirket
from sw_onto_generation.configs import DGraphProps, FieldProp, LLMHelperProps, NodeProp, SearchType

# Working on GeneralDocumentInfo
## append field description for baslik


## modify model config
update_dict = {
    DGraphProps.__name__: DGraphProps(
        ### adding dgraph type for general document info
        node_prop=NodeProp(dgraph_type="generalDocumentInfo"),
        ### adding vector search type for baslik field
        field_props=[FieldProp(field_name="baslik", search_type=SearchType.VECTOR)],
    ),
    LLMHelperProps.__name__: LLMHelperProps(
        description="Döküman hakkinda genel bilgileri tanımlar, sozlesme ismi veya basligi en onemli bilgidir. Her sozlesmede mutlak bir sekilde bulunmalidir.",
        cardinality=False,
    ),
}

rprint("Model config of GeneralDocumentInfo in Common")
rprint(GeneralDocumentInfo.model_config)
rprint("Model config of GeneralDocumentInfo in Kira")
GeneralDocumentInfo.modify_model_config(update_dict)
rprint(GeneralDocumentInfo.model_config)


rprint("Model fields of GeneralDocumentInfo in Common")
rprint(GeneralDocumentInfo.model_fields)
rprint("Model fields of GeneralDocumentInfo in Kira")
GeneralDocumentInfo.append_field_description(field_name="baslik", additional_description="Kira sozlesmesi veya kiralama sozlesmesi olma ihtimali yuksektir", seperator=" ")
rprint(GeneralDocumentInfo.model_fields)

# %%

# Working On Sirket Node
## append field description for vkn

## modify model config
update_dict = {
    DGraphProps.__name__: DGraphProps(
        ### adding dgraph type for sirket
        node_prop=NodeProp(dgraph_type="sirket"),
        field_props=[
            FieldProp(field_name="vkn", search_type=SearchType.EXACT),
            FieldProp(field_name="unvan", search_type=SearchType.VECTOR),
        ],
    ),
    LLMHelperProps.__name__: LLMHelperProps(
        description="Tüzel kişi,kamu kuruluslari, vakif, dernek veya organizasyonları tanımlar, genelde vknleri olur.",
        cardinality=True,
    ),
}
rprint("Model config of Sirket in Common")
rprint(Sirket.model_config)
rprint("Model config of Sirket in Kira")
Sirket.modify_model_config(update_dict)
rprint(Sirket.model_config)

rprint("Model fields of Sirket in Common")
rprint(Sirket.model_fields)
rprint("Model fields of Sirket in Kira")
Sirket.append_field_description(field_name="vkn", additional_description="Her sirketin mutlaka bir vergi numarasi olmalidir", seperator=" ")
rprint(Sirket.model_fields)

# %%

# %%
