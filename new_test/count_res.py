from Bio.PDB import PDBParser
import pandas as pd


def count_residues_and_waters(pdb_file):
    # Create a PDB parser object
    parser = PDBParser(QUIET=True)
    
    # Parse the PDB file
    structure = parser.get_structure('structure', pdb_file)
    
    # Initialize counters
    residue_count = 0
    water_count = 0
    
    # Iterate over each model in the structure
    for model in structure:
        # Iterate over each chain in the model
        for chain in model:
            # Iterate over each residue in the chain
            for residue in chain:
                # Check if the residue is a water molecule
                if residue.get_resname().strip() == 'HOH':
                    water_count += 1
                else:
                    residue_count += 1
    
    return residue_count, water_count

# Example usage
with open("new_test.txt") as f:
    data = f.readlines()
fnames = []
for line in data:
    fnames.append(line.strip())
n_residues = []
n_waters = []
for fname in fnames:
    pdb_file = f'pdbs1/{fname}.pdb'
    residue_count, water_count = count_residues_and_waters(pdb_file)
    print(f"Number of residues: {residue_count}")
    print(f"Number of water molecules: {water_count}")
    n_residues.append(residue_count)
    n_waters.append(water_count)
df = pd.DataFrame()
df["pdb"] = fnames
df["nres"] = n_residues
df["nwater"] = n_waters
df.to_csv("new_test_summary.csv", index=False)
