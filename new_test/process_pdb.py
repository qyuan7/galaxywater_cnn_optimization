import requests
from Bio.PDB import PDBParser, PDBIO, Select

def get_pdb(pdb_id):
    #pdb_id = '1dy5'
    url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
    response=requests.get(url)
    with open(f"{pdb_id}.pdb", 'w') as f:
        f.write(response.text)


class NotAnisou(Select):
    def accept_atom(self,atom):
        return atom.get_name() != "ANISOU"

def get_chain(pdb_id):
    parser = PDBParser()
    structure = parser.get_structure(pdb_id, f"{pdb_id}.pdb")

    model = structure[0]

    chain_a = model['A']
    new_structure = chain_a.get_parent()
    io=PDBIO()
    io.set_structure(new_structure)
    io.save(f"{pdb_id}_A.pdb", select=NotAnisou())

if __name__ == "__main__":
    with open("new_test.txt") as f:
        data = f.readlines()
    get_pdb("4unu")
    get_chain("4unu")
    #for d in data:
    #    pdb_id = d.strip().split('_')[0]
    #    print(pdb_id)
    #    get_pdb(pdb_id)
    #    get_chain(pdb_id)
