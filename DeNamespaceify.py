# Bake all namespaces into symbol name strings directly. For example,
# this script would convert a symbol named "MyFunction" in the "MyClass"
# namespace to a symbol named "MyClass::MyFunction" in the global
# namespace.
# @author RoadrunnerWMC
# @category Data

symTable = currentProgram.getSymbolTable()

for sym in symTable.getSymbolIterator():
    name_without_namespace = sym.getName(False)
    name_with_namespace = sym.getName(True)
    if name_without_namespace != name_with_namespace:
        sym.setNameAndNamespace(
            name_with_namespace,
            sym.getProgram().getGlobalNamespace(),
            sym.getSource(),
        )
        print(u'De-namespace-ified {}'.format(name_with_namespace))
