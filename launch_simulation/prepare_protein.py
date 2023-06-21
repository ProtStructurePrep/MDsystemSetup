import pprep.utils_mdanalysis as umda
import pprep.utils_rdkit as urk
import pprep.utils_pdbfixer as updbfix
import pprep.MDutils as umd
import argparse


def main(args):
	updbfix.prepare_protein(args.protein_pdb, args.output_prepared_prot)
	return None

if __name__ == "__main__":
    """ This is executed when run from the command line """
    # Parse the CLI arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Correct the receptor pdb and save it into a new pdb file.')

    parser.add_argument("-p", "--protein_pdb", type=str, default='protein.pdb',
                        help='pdb file of the protein (default: %(default)s)')
    parser.add_argument("-o", "--output_prepared_prot", type=str, default='prepared_protein.pdb',
                        help='output file name of the prepared protein (default: %(default)s)')

    args = parser.parse_args()
    main(args)
