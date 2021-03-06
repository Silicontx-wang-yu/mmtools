#=============================================================================================
# Find the maximal common GAFF substructure among a number of different ligands and write
# this structure to a mol2 file.
# 
# Written by John D. Chodera <jchodera@gmail.com> 2008-02-08
#=============================================================================================

#=============================================================================================
# IMPORTS
#=============================================================================================

from openeye.oechem import *
from mmtools.moltools.ligandtools import *
from mmtools.moltools.relativefeptools import *
import os
import os.path
from numpy import *

#=============================================================================================
# PARAMETERS
#=============================================================================================

# base path for all parameterized ligand files
ligand_basepath = '/home/mrs5pt/preptools/mmtools/relativetools/Examples/JNK3/ligands-parameterized/'

# Target ligand group.
#ligand_name_list = [ ('jnk.aff-%d' % index) for index in (8, 10, 11, 15, 22, 26, 32, 38, 52) ] # group 1
ligand_name_list = [ ('jnk.aff-%d' % index) for index in (13, 16, 53) ] # group 2


# Filename of mol2 file for generated intermediate structure to write.
intermediate_filename = 'intermediate.mol2'

#=============================================================================================
# SUBROUTINES
#=============================================================================================

#=============================================================================================
# MAIN
#=============================================================================================

# read all ligands
ligands = list()
for ligand_name in ligand_name_list:
    # attempt to load the ligand with GAFF parameters
    ligand = loadGAFFMolecule(ligand_basepath, ligand_name)
    # skip if no ligand found
    if not ligand: continue
    # append to list
    ligands.append(ligand)
print "%d ligands loaded" % len(ligands)

# find common substructure
common_substructure = determineCommonSubstructure(ligands, debug = True)

# find RMS-fit charges
common_substructure = determineMinimumRMSCharges(common_substructure, ligands, debug = True)

# write out molecule
writeMolecule(common_substructure, intermediate_filename)

