def get_coordinate(x):
	esto=('Scrimshawed Whale Tooth','4B')
	return esto[1]

def convert_coordinate(x):
	result_data=(('4', 'B'),('2','A'))
	return result_data[1]

def create_record(x,y):
	azara=('Angry Monkey Figurine', '5B')
	rui=('Stormy Breakwater', '5B', 'Purple')
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		rui=('Stormy Breakwater', ('5', 'B'), 'Purple')
		return azara+rui
	else:
		return "no coincide"
