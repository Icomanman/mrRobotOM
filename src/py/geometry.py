
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

# get beam ID from a specified robot bar selection, used individually or in a loop
# elem_no is the index from the selection
def getBeamId(memb_sel, elem_no = 1):
	bar_elem = memb_sel.Get(elem_no)
	return bar_elem

def getBeamGroup(memb_sel):
	total_count = memb_sel.count
	nos = list()
	beam_group = list()
	for x in range(total_count):
		beam_group.append(getBeamId(memb_sel, x + 1))
		nos.append(x + 1)
		# print x, ":", beam_group[x]
	del(x)
	
	return beam_group

def getNodeCoords(one_node):
	coordinates = ['x','y','z']
	return coordinates

# get beam data by ID, use getBeamId
def getBeamData(one_bar):
	data = dict()
	data['node_id'] = range(2)

	# start node
	data['node_id'][0] = one_bar.StartNode
	# end node 
	data['node_id'][1] = one_bar.EndNode 

	print "Extracted node data for bar no.", one_bar.Number


	return data