import pprep.utils_mdanalysis as umda
import pprep.utils_rdkit as urk
import pprep.utils_pdbfixer as updbfix
import pprep.MDutils as umd
import parmed
import argparse


def main(args):
	simulate_complex(args.ligand_pdb, args.resname, args.smiles, args.protein_file)
	return None
	
def simulate_complex(ligand_pdb, resname, smiles, receptor_file):
    """Simulate the protein-ligand complex
    
    Parameters
    -----------
    rdkit_ligand:
        prepared ligand to simulate
    receptor_file: string
        prepared receptor file to simulate
    equilibration_steps: int
        steps to perform the equilibration
    num_steps: int
        number of steps to run the simulation
    reporting interval: int
        interval at whcih the reporters are added
    output_traj_pdb: string
        name of the pdb output trajectory file
    output_traj_dcd: string
        name of the dcd output trajectory file
    """
    
    ligand = urk.prepare_ligand(ligand_pdb, resname, smiles) 
    receptor = umd.load_prepared_receptor(receptor_file)
    system, modeller, parm = umd.prepare_system(receptor, ligand, solvate=True)
    structure = parmed.openmm.load_topology(modeller.topology, system, xyz=modeller.positions)
    bond_type = parmed.BondType(1.0, 1.0, list=structure.bond_types)
    structure.bond_types.append(bond_type)
    for bond in structure.bonds:
        if bond.type is None:
            bond.type = bond_type
    structure.save("solvated.rst7", overwrite=True)  
    structure.save("solvated.parm7", overwrite=True)  
	
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    # Parse the CLI arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Simulate the protein-ligand complex.')

    parser.add_argument("-l", "--ligand_pdb", type=str, default='ligand.pdb',
                        help='pdb file of the ligand (either a pdb ID or a pdb file) (default: %(default)s)')
    parser.add_argument("-rn", "--resname", type=str, default='03P',
                        help='name of the ligand (default: %(default)s)')
    parser.add_argument("-s", "--smiles", type=str, default='O=C(CC(O)(C)C)NCCn1ccc2c1c(ncn2)Nc1ccc(c(c1)Cl)Oc1cccc(c1)C(F)(F)F',
                        help='smiles of the ligand (default: %(default)s)')
    parser.add_argument("-p", "--protein_file", type=str, default='prepared_protein.pdb',
                        help='pdb file of the prepared receptor (default: %(default)s)')              
                        

    args = parser.parse_args()
    main(args)


