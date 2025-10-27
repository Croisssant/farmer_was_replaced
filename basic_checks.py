TILL_PLANTS = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]

def should_till(curr_plant):
	if curr_plant in TILL_PLANTS and get_ground_type() != Grounds.Soil:
			till()