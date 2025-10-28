TILL_PLANTS = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]

def use_weird_substance_maze():
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def should_harvest():
	if can_harvest():
		harvest()

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

def partial(fn, arg_1, arg_2=None, arg_3=None):
	def wrapper():
		if arg_3:
			return fn(arg_1, arg_2, arg_3)
		
		elif arg_2:
			return fn(arg_1, arg_2)
		
		return fn(arg_1)
	
	return wrapper