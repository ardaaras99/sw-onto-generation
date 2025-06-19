import importlib
import inspect
from typing import Literal

from sw_onto_generation import DIR_STRUCTURE
from sw_onto_generation.base.base_node import BaseNode
from sw_onto_generation.base.base_relation import BaseRelation

COMMON_NODE_MODULE_NAME = "sw_onto_generation.common.common_nodes"
COMMON_RELATION_MODULE_NAME = "sw_onto_generation.common.common_relations"


def check_valid_lib_and_ontology(lib_name: str, ontology_name: str):
    if lib_name not in DIR_STRUCTURE:
        raise ValueError(f"Lib {lib_name} not found, valid values: {DIR_STRUCTURE.keys()}")
    if ontology_name not in DIR_STRUCTURE[lib_name]:
        raise ValueError(f"Ontology {ontology_name} not found, valid values: {DIR_STRUCTURE[lib_name]}")


def get_specific_module_name(lib_name: str, ontology_name: str, module_type: Literal["nodes", "relations"]):
    return f"sw_onto_generation.root.lib_{lib_name}.onto_{ontology_name}.{module_type}"


def find_classes_in_modules(module_names: list[str]):
    node_classes = set()
    relation_classes = set()
    for module_name in module_names:
        try:
            module = importlib.import_module(module_name)
            for name in dir(module):
                obj = getattr(module, name)
                if inspect.isclass(obj):
                    if issubclass(obj, BaseNode) and obj != BaseNode:
                        node_classes.add(obj)
                    elif issubclass(obj, BaseRelation) and obj != BaseRelation:
                        relation_classes.add(obj)
                    else:
                        continue
        except (ImportError, AttributeError) as e:
            raise e

    return list(node_classes), list(relation_classes)


def get_all_common_and_specific_root_classes(lib_name: str, ontology_name: str):
    check_valid_lib_and_ontology(lib_name, ontology_name)

    module_names = [
        COMMON_NODE_MODULE_NAME,
        COMMON_RELATION_MODULE_NAME,
        get_specific_module_name(lib_name, ontology_name, "nodes"),
        get_specific_module_name(lib_name, ontology_name, "relations"),
    ]

    return find_classes_in_modules(module_names)


def get_all_common_and_root_classes():
    node_module_names = []

    for lib_name in DIR_STRUCTURE:
        for ontology_name in DIR_STRUCTURE[lib_name]:
            node_module_names.append(get_specific_module_name(lib_name, ontology_name, "nodes"))

    relation_module_names = []
    for lib_name in DIR_STRUCTURE:
        for ontology_name in DIR_STRUCTURE[lib_name]:
            relation_module_names.append(get_specific_module_name(lib_name, ontology_name, "relations"))

    module_names = [COMMON_NODE_MODULE_NAME, COMMON_RELATION_MODULE_NAME] + node_module_names + relation_module_names

    return find_classes_in_modules(module_names)


# %%
