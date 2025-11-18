# Exports a file with lines in the form
# "symbolName 0xADDRESS function_or_label", where "f" indicates a
# function and "l" a label, suitable for importing with Ghidra's
# built-in ImportSymbolsScript.py.
# @author RoadrunnerWMC
# @category Data
#

from ghidra.program.database.function import FunctionDB

f = askFile('Choose a file to write to', 'Go!')

COLUMN_2 = 32
COLUMN_3 = 48

symTable = currentProgram.getSymbolTable()

num_functions = 0
num_labels = 0

with file(f.absolutePath, 'w') as fd:
    for sym in symTable.getSymbolIterator():
        name = sym.getName(True)
        addr = sym.getAddress().getOffset()

        if isinstance(sym.getObject(), FunctionDB):
            function_or_label = u'f'
            num_functions += 1
        else:
            function_or_label = u'l'
            num_labels += 1

        line = name
        line += u' ' * max(COLUMN_2 - len(line), 1)
        line += u'0x{:08X}'.format(addr)
        line += u' ' * max(COLUMN_3 - len(line), 1)
        line += function_or_label

        fd.write((line + u'\n').encode('utf-8'))

num_total = num_functions + num_labels
print(u'Exported {} symbols ({} functions, {} labels)'.format(num_total, num_functions, num_labels))
