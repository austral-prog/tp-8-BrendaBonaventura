def get_coordinate(x):
	esto=('Scrimshawed Whale Tooth','4B')
	return esto[1]

def convert_coordinate(x):
	result_data=(('4', 'B'),('2','A'))
	return result_data[0]

def create_record(x,y):
	azara=('Carved Wooden Elephant', '8C')
	rui=('Foggy Seacave', ('8C'), 'Purple')
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		rui=('Foggy Seacave', ('8', 'C'), 'Purple')
		return azara+rui
	else:
		return "no coincide"
