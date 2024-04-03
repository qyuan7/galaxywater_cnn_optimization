from Bio.PDB import PDBParser, PDBIO, Select

class NotAnisou(Select):
    def accept_atom(self,atom):
        return atom.get_name() != "ANISOU"
parser = PDBParser()
structure = parser.get_structure("1dy5", "1dy5.pdb")

model = structure[0]

chain_a = model['A']
new_structure = chain_a.get_parent()
io=PDBIO()
io.set_structure(new_structure)
io.save("1dy5_A.pdb", select=NotAnisou())
