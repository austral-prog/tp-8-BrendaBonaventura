def get_coordinate(x):
	esto=("Scrimshawed Whale Tooth","4B")
	return esto[1]

def convert_coordinate(x):
	input_data=('2A', '4B', '1C', '6D', '7E', '7F','6A', '8A', '5B', '8C', '1F', '3D', '4E')
	result_data=('2', 'A')
	coor=result_data[0]
	return result_data

def create_record(x,y):
	azara=("Brass Spyglass","4B")
	rui=("Abandoned Lighthouse","4B","Blue")
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		return azara+rui
	else:
		return "no coincide"
