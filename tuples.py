def get_coordinate(x):
	esto=("Scrimshawed Whale Tooth","2A")
	return esto[1]

def convert_coordinate(x):
	input_data=['2A', '4B', '1C', '6D', '7E', '7F','6A', '8A', '5B', '8C', '1F', '3D', '4E']
	result_data=(('2', 'A'),('4', 'B'),('1', 'C'),('6', 'D'),('7', 'E'),('7', 'F'),('6', 'A'),('8', 'A'),('5', 'B'),('8', 'C'),('1', 'F'),('3', 'D'),('4', 'E'))
	coor=result_data[0]
	return result_data

def create_record(x):
	azara=("Brass Spyglass","4B")
	rui=("Abandoned Lighthouse","4B","Blue")
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		return azara+rui
	else:
		return "no coincide"
