import pprep.utils_mdanalysis as umda
import pprep.utils_rdkit as urk
import pprep.utils_pdbfixer as updbfix
import pprep.MDutils as umd
import argparse


def main(args):
	parse_complex(args.pdb_name, args.output_ligand, args.output_prot)
	return None
	
def parse_complex(pdb_name, output_ligand, output_prot):
    """Select the receptor and the ligand from a protein ligand complex
    
    Parameters
    ----------
    pdb_name: string
        it can be either the pdb file path or the pdb id of the protein
    output_ligand: string
        name of the output pdb file of the ligand
    output_prot: string
        name of the output pdb file of the protein
    """
    u = umda.load_pdb(pdb_name)
    u, ligand_name = umda.find_potential_ligand(u)
    ligand = umda.select_ligand(u, ligand_name, output_ligand)
    protein = umda.select_protein(u, output_prot)
    print(f'ligand name: {ligand_name}')
    return ligand, protein

if __name__ == "__main__":
    """ This is executed when run from the command line """
    # Parse the CLI arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Separate the ligand from the receptor and create one pdb for the ligand and one for the receptor.')

    parser.add_argument("-pdb", "--pdb_name", type=str, default='3poz',
                        help='input pdb file name (either a pdb ID or a pdb file) (default: %(default)s)')
    parser.add_argument("-ol", "--output_ligand", type=str, default='ligand.pdb',
                        help='output ligand file name (default: %(default)s)')
    parser.add_argument("-op", "--output_prot", type=str, default='protein.pdb',
                        help='output protein file name (default: %(default)s)')

    args = parser.parse_args()
    main(args)
