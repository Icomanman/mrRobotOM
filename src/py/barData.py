
def selectedBeams(rob):

	_str = rob.Project.Structure

	bar_obj = _str.Bars.GetAll()
	membSel =_str.Selections.Get(1)

	print membSel.count

	return membSel

def getNodes(rob, memb, cases="1001to1149"):
	memb_id = memb.Get(0)
	member = rob.Project.Structure.Bars.Get(memb_id)
	print memb_id
	print member.Length
	
	return