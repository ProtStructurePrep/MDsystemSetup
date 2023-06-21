import pprep.utils_mdanalysis as umda
import pprep.utils_rdkit as urk
import pprep.utils_pdbfixer as updbfix
import pprep.MDutils as umd
import argparse


def main(args):
	simulate_complex(args.ligand_pdb, args.resname, args.smiles, args.protein_file, 
                     args.equilibration_steps, args.num_steps, args.reporting_interval,
                     args.output_traj_pdb, args.output_traj_dcd)
	return None
	
def simulate_complex(ligand_pdb, resname, smiles, receptor_file, 
                     equilibration_steps, num_steps, reporting_interval,
                     output_traj_pdb, output_traj_dcd):
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
    system, complex_structure = umd.prepare_system(receptor, ligand)
    simulation = umd.setup_openmm_simulation(system, complex_structure)
    simulation = umd.minimize_and_equilibrate(simulation, equilibration_steps)
    umd.run_simulation(simulation, num_steps, reporting_interval, output_traj_pdb, output_traj_dcd)

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
    parser.add_argument("-es", "--equilibration_steps", type=int, default='200',
                        help='output file name of the prepared protein (default: %(default)s)')
    parser.add_argument("-ns", "--num_steps", type=int, default='1000',
                        help='output file name of the prepared protein (default: %(default)s)')
    parser.add_argument("-ri", "--reporting_interval", type=int, default='10',
                        help='output file name of the prepared protein (default: %(default)s)')
    parser.add_argument("-opdb", "--output_traj_pdb", type=str, default='out_traj.pdb',
                        help='output file name of the prepared protein (default: %(default)s)')
    parser.add_argument("-odcd", "--output_traj_dcd", type=str, default='out_traj.dcd',
                        help='output file name of the prepared protein (default: %(default)s)')                    
                        

    args = parser.parse_args()
    main(args)

