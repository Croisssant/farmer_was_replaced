from maze_solver import create_maze, maze_solver 
from utils import partial

def generate_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def gold_farming_loop(target_amount):
	#change_hat(Hats.Golden_Gold_Hat)
	while num_items(Items.Gold) < target_amount:
		if num_drones() == 25:
			if get_entity_type() == Entities.Treasure:
				harvest()
			create_maze()

def multi_drone_gold_farming(target_amount):
	clear()
	list = []

	if max_drones() >= 25:
		set_world_size(5)
		while num_drones() <= 25:
			pos_x = get_pos_x()
			pos_y = get_pos_y()
			current = (pos_x, pos_y)
			if current not in list:
				list.append(current)
				spawn_drone(partial(gold_farming_loop, target_amount))
				move(North)
			else:
				move(East)

	elif max_drones() >= 16:
		set_world_size(4)
		while num_drones() <= 16:
			pos_x = get_pos_x()
			pos_y = get_pos_y()
			current = (pos_x, pos_y)
			if current not in list:
				list.append(current)
				spawn_drone(partial(gold_farming_loop, target_amount))
				move(North)
			else:
				move(East)

	elif max_drones() >= 9:
		set_world_size(3)
		while num_drones() <= 9:
			pos_x = get_pos_x()
			pos_y = get_pos_y()
			current = (pos_x, pos_y)
			if current not in list:
				list.append(current)
				spawn_drone(partial(gold_farming_loop, target_amount))
				move(North)
			else:
				move(East)

	elif max_drones() >= 4:
		set_world_size(2)
		while num_drones() <= 4:
			pos_x = get_pos_x()
			pos_y = get_pos_y()
			current = (pos_x, pos_y)
			if current not in list:
				list.append(current)
				spawn_drone(partial(gold_farming_loop, target_amount))
				move(North)
			else:
				move(East)

	else:
		maze_solver(target_amount)




# Get number of drones
# Determine maximum world size that can be set

# 2 * 2 = 4
# 3 * 3 = 9
# 4 * 4 = 16

# def begin_farm_loop(world_size, num_drones):
# 	set_world_size(4)
# 	while num_drones() <= 16:
# 		pos_x = get_pos_x()
# 		pos_y = get_pos_y()
# 		current = (pos_x, pos_y)
# 		if current not in list:
# 			list.append(current)
# 			spawn_drone(partial(gold_farming_loop, target_amount))
# 			move(North)
# 		else:
# 			move(East)