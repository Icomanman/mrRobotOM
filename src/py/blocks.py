
# returns the member selection object
def selectBeamByStorey(_struc, storey, elem = 1):
	# 1: code for I_OT_BAR
	if _struc.Storeys.Find(storey):
		memb_sel = _struc.Selections.CreateByStorey(elem,storey)
		print memb_sel.count,"elements selected from storey:", storey
	else:
		print "Selected storey not found. No members selected."
	return memb_sel

def getSelectedBeams(_struc):
	memb_sel =_str.Selections.Get(1) # 1: I_OT_BAR
	print (membSel.count, " bar objects selected.")
	return memb_sel

def getLCS(_struc, cases="1"):
	# 2: code for I_OT_CASE
	load_cases = _struc.Selections.Create(2)
	load_cases.AddText(cases)
	print ("selected load cases: ", cases)
	
	return load_cases

def getBeamId(memb_sel, elem_no = 1):
	bar_elem = memb_sel.Get(elem_no)
	return bar_elem

def getBeamGroup(memb_sel):
	nos = list()
	beam_group = list()
	total_count = memb_sel.count
	for x in range(total_count):
		beam_group.append(getBeamId(memb_sel,x))
		nos.append(x)
	del(x)

	print x

	for x in beam_group:
		print x, ":", beam_group[x]
	
	
	return beam_group
