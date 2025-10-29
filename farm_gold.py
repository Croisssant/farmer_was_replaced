from utils import partial

def generate_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def gold_farming_loop(target_amount):
	change_hat(Hats.Golden_Gold_Hat)
	while num_items(Items.Gold) < target_amount:
		if num_drones() == 25:
			if get_entity_type() == Entities.Treasure:
				harvest()
			generate_maze()

def multi_drone_gold_farming(target_amount):
	clear()
	set_world_size(5)
	list = []

	while num_drones() < 26:
		pos_x = get_pos_x()
		pos_y = get_pos_y()
		current = (pos_x, pos_y)
		if current not in list:
			list.append(current)
			spawn_drone(partial(gold_farming_loop, target_amount))
			move(North)
		else:
			move(East)