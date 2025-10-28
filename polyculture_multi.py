from move_to_coord import move_to_xy
from utils import should_till
from multi_drone import multi_drone_fn, water_10_times

def multi_drone_fn_split(fn_1, fn_2, move_direction):

	for _ in range(get_world_size()):
		drone_1 = spawn_drone(fn_1)
		drone_2 = spawn_drone(fn_2)
		
		if not drone_2:
			fn_2()
		if not drone_1:
			fn_1()
			
		move(move_direction)
		move(move_direction)
		

def polyculture_fn():
	move(West)
	original_x_pos = get_pos_x()
	original_y_pos = get_pos_y()

	while True:
		polyculture_data = None
		
		if get_entity_type() == Entities.Tree:
			polyculture_data = get_companion()
			
		if polyculture_data != None and get_entity_type() != None:
			plant_type, (x, y) = polyculture_data
			move_to_xy(x, y)
			
			if can_harvest():
				harvest()
				
			should_till(plant_type)
			plant(plant_type)
			move_to_xy(original_x_pos, original_y_pos)
			
			
		move(West)
		original_x_pos = get_pos_x()
		original_y_pos = get_pos_y()
		
		
def harvest_and_plant():
	while True:
		should_till(Entities.Carrot)
		
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		
		if get_entity_type() == None:
			plant(Entities.Carrot)
		move(East)

def farm_weird_substance():
	WORLD_LENGTH = get_world_size()
	while True:
		for i in range(WORLD_LENGTH):
			curr_plant = Entities.Tree
			
			if i % 2 == 0:
				curr_plant = Entities.Bush
				
			if can_harvest():
				harvest()
				plant(curr_plant)
				if curr_plant == Entities.Tree:
					use_item(Items.Fertilizer)
		
			if get_entity_type() == None:
				plant(curr_plant)
				
			move(East)
			
def harvest_and_plant_wood():
	WORLD_LENGTH = get_world_size()
	while True:
		for i in range(WORLD_LENGTH):
			curr_plant = Entities.Tree
			
			if i % 2 == 0:
				curr_plant = Entities.Bush
				
			if can_harvest():
				harvest()
				plant(curr_plant)
				
				while get_water() < 0.5:
					if num_items(Items.Water) > 1000:
						use_item(Items.Water)
					else:
						break
					
		
			if get_entity_type() == None:
				plant(curr_plant)
				
			move(East)

if __name__ == "__main__":
	multi_drone_fn(water_10_times, North)
	multi_drone_fn_split(harvest_and_plant_wood, polyculture_fn, North)