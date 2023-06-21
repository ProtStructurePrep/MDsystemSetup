[Installation](#installation) |  [Requirements](#requirements) | [Contributing](#contributing) |  [Acknowledgment](#acknowledgment)


Protein-Ligand Complex MD simulations
=================
The aim of this repository is to facilitate and automatize the MD simulations procedure. The project can be divided into two major blocks.

![FIGURE](https://github.com/ProtStructurePrep/MDsystemSetup/blob/master/summary_blocks.png)

The first one contains the basic steps for parsing proteins and selecting its ligands. Also, in this first block you can find the steps for preparing the protein and ligand structures, by fixing errors in their respective PDB files. In the second block you can find the steps for simulating the protein and the protein-ligand complex. Additionally, in this last block you can also find an integration of the program to perform BPMD with the OpenBPMD engine.

For a better understanding of the different functionalities of this program you can use this [Google Colab](https://colab.research.google.com/drive/13XqJ4Mp3TsDX2YZ8tikngBOFXW5fHFey#scrollTo=3bJ68NQnYAVz). Here you will find an example pipeline to get familiar with the program.

Requirements
=================
* [MDTraj](https://github.com/mdtraj/mdtraj)
* [MDAnalysis](https://github.com/MDAnalysis/mdanalysis).
* [nglview](https://github.com/nglviewer/nglview)
* [OpenMM](https://github.com/openmm/openmm) and [OpenMM Forcefields](https://github.com/openmm/openmmforcefields)
* [RDKit](https://github.com/rdkit/rdkit)
* [PDBFixer](https://github.com/openmm/pdbfixer)


