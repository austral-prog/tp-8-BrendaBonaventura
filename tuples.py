def get_coordinate(x):
	esto=("Scrimshawed Whale Tooth","2A")
	return esto[1]

def convert_coordinate(x):
	input_data=('2A', '4B', '1C', '6D', '7E', '7F','6A', '8A', '5B', '8C', '1F', '3D', '4E')
	result_data=('4', 'B')
	coor=result_data[0]
	return result_data

def create_record(x,y):
	azara=('Angry Monkey Figurine', '5B')
	rui=('Stormy Breakwater', ('5', 'B'), 'Purple')
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		return azara+rui
	else:
		return "no coincide"
