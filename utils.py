TILL_PLANTS = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]

def should_till(curr_plant):
	if curr_plant in TILL_PLANTS and get_ground_type() != Grounds.Soil:
			till()

def get_xy():
	return (get_pos_x(), get_pos_y())

def isEven(num):
	return num % 2 == 0

def partial(fn, arg):
	def wrapper():
		return fn(arg)
	
	return wrapper