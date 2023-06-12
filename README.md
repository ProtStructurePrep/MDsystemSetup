[Installation](#installation) |  [Requirements](#requirements) | [Contributing](#contributing) |  [Acknowledgment](#acknowledgment)

Complex-Ligand System Setup in Molecular Dynamics Simulations 
=================


Protein-Ligand Complex MD simulations
=================
The aim of this repository is to facilitate and automatize the MD simulations procedure. The project can be divided into two major blocks. The first one contains the basic steps for parsing proteins and selecting its ligands. Also, in this first block you can find the steps for preparing the protein and ligand structures, by fixing errors in their respective PDB files. In the second block you can find the steps for simulating the protein and the protein-ligand complex.

For a better understanding of the different functionalities of this program you can use this [Google Colab](https://colab.research.google.com/drive/1x0s3Ui5VQVVR1Esj5_JbqmH5w-PkJGl5?usp=sharing). Here you will find an example pipeline to get familiar with the program.

Table of contents
=================

* [Installation](#installation)
* [Binding Pose Metadynamics Integration](#BPMD)
* [Tutorials](#tutorials)
* [Requirements](#requirements)
* [Contributing](#contributing)
* [Acknowledgment](#acknowledgment)


Installation
============
To install ....

- Available on [PyPI](https://pypi.python.org/pypi/nglview/)

```bash
   pip install 
```

Binding Pose Metadynamics Integration
============
In addition to the program’s MD simulations capabilities, it also offers the ability to perform BPMD, a computational technique that uses the MD simulations to explore the binding process between a ligand and its target receptor. Accurately predicting the binding pose of a ligand within a protein binding site remains challenging. Because of this, being able to incorporate BPMD in the program can enhance computer-aided drug discovery efforts.


Requirements
=================
* [MDTraj](https://github.com/mdtraj/mdtraj)
* [MDAnalysis](https://github.com/MDAnalysis/mdanalysis)
* [nglview](https://github.com/nglviewer/nglview)
* [OpenMM](https://github.com/openmm/openmm) and [OpenMM Forcefields](https://github.com/openmm/openmmforcefields)
* [RDKit](https://github.com/rdkit/rdkit)
* [PDBFixer](https://github.com/openmm/pdbfixer)
* [OpenFF](https://github.com/openforcefield)



