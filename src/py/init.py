
# main server
import helpers
import blocks as bb

def run(rob):
    _struc = rob.Project.Structure
    sel_memb = bb.selectBeamByStorey(_struc, "2F", 1)

    beam_group = bb.getBeamGroup(sel_memb)