from move_to_coord import move_to_xy
from planting_helpers import just_harvest, check_harvest_plant, water_n_times
from utils import partial, should_till, get_xy
from multi_drone_fn import multi_drone_await_fn, multi_drone_fn_split

# Just use polyculture with multi drone as it is much more worth it
def polyculture_fn(moving_direction=West):
    move(moving_direction)

    while True:
        original_x_pos, original_y_pos = get_xy()
        polyculture_data = get_companion()
        
        if polyculture_data:
            plant_type, (x, y) = polyculture_data
            move_to_xy(x, y)
            just_harvest()
            should_till(plant_type)
            plant(plant_type)
            move_to_xy(original_x_pos, original_y_pos)
        
        move(moving_direction)
		

# Specialized polyculture function to target trees
def polyculture_fn_targeted(moving_direction=West, target_entity=Entities.Tree):
    move(moving_direction)

    while True:
        original_x_pos, original_y_pos = get_xy()
        curr_entity = get_entity_type()
        
        if curr_entity == target_entity:
            polyculture_data = get_companion()
            
            if polyculture_data:
                plant_type, (x, y) = polyculture_data
                move_to_xy(x, y)
                just_harvest()
                should_till(plant_type)
                plant(plant_type)
                move_to_xy(original_x_pos, original_y_pos)
        
        move(moving_direction)
		

def multi_drone_planting_wrapper(curr_plant, planting_fn=check_harvest_plant, moving_direction=East):
	while True:
		planting_fn(curr_plant)
		move(moving_direction)
		

def farm_weird_substance():
	while True:
		for i in range(get_world_size()):
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
    while True:
        for i in range(get_world_size()):
            curr_plant = Entities.Tree
            if i % 2 == 0:
                curr_plant = Entities.Bush
                
            check_harvest_plant(curr_plant)
            move(East)
				
		
def plant_while_sufficient_water_loop(curr_plant, moving_direction=East):
	while get_water() > 0.5:
		check_harvest_plant(curr_plant)
		move(moving_direction)


def water_and_plant_loop(curr_plant):
	while True:
		move_to_xy(0, 0)
		multi_drone_await_fn(water_n_times, North)
		multi_drone_await_fn(partial(plant_while_sufficient_water_loop, curr_plant), North)
		

if __name__ == "__main__":
	# multi_drone_fn(water_10_times, North)
	multi_drone_fn_split(harvest_and_plant_wood, polyculture_fn, North)