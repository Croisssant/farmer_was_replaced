from move_to_coord import limited_move_to, move_to_xy
from planting_helpers import traverse_plant_and_harvest_sunflower


def get_first_apple_coords():
	for i in range(get_world_size()):	
		if i % 2 == 0:
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Apple:
					init_x, init_y = measure()
					return (init_x, init_y)
				
				if i == (get_world_size() - 1):
					move(East)
				else:
					move(North)
		else:
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Apple:
					init_x, init_y = measure()
					return (init_x, init_y)
				
				if i == (get_world_size() - 1):
					move(East)
				else:
					move(South)
		

def initial_apple_search(next_x, next_y):
	EDGE = get_world_size() - 1
	
	for i in range(EDGE):
		limited_move_to(next_y, "y")
		limited_move_to(next_x, "x")
		
		# Recheck the apple's logic
		if get_entity_type() == Entities.Apple:
			next_x, next_y = measure()
		
		curr_y = get_pos_y()
		if  curr_y == next_y:
			if get_world_size() - curr_y > 2:
				move(North)
				move(North)
			else:
				move(South)
				move(South)
			
		
		if i % 2 == 0:
			limited_move_to(EDGE, "x")
		else:
			limited_move_to(0, "x")
	
	if get_pos_x() == 0:
		limited_move_to(4, "y")
		limited_move_to(EDGE, "x")
		limited_move_to(0, "y")
		limited_move_to(0, "x")
	else:
		limited_move_to(0, "y")
		limited_move_to(0, "x")
		

def s_walk_loop():
	edge_minus_one = get_world_size() - 2
	edge = get_world_size() - 1
	
	while True:
		for _ in range((get_world_size() - 2) / 2):
			move(North)
			limited_move_to(edge_minus_one, "x")
			move(North)
			limited_move_to(0, "x")
		if move(North):
			limited_move_to(edge, "x")
			limited_move_to(0, "y")
			limited_move_to(0, "x")
		else:
			break
		


def farming_bones_loop(target_amount):
    while num_items(Items.Bone) < target_amount:
        change_hat(Hats.Sunflower_Hat)
        move_to_xy(0, 0)
        traverse_plant_and_harvest_sunflower()
        
        change_hat(Hats.Dinosaur_Hat)
        init_x, init_y = get_first_apple_coords()
        initial_apple_search(init_x, init_y)
        s_walk_loop()