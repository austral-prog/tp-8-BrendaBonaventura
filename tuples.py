def get_coordinates():
	esto=("Scrimshawed Whale Tooth","2A")
	return esto[1]

def convert_coordinate():
	coor="2A"
	c1=coor[0]
	c2=coor[1]
	return (f"{c1}",f"{c2}")

def create_record():
	azara=("Brass Spyglass","4B")
	rui=("Abandoned Lighthouse","4B","Blue")
	dos=azara[1]
	uno=rui[1]
	if dos==uno:
		return azara+rui
	else:
		return "no coincide"
