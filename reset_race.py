from builtins import dict, sorted
from dino_movements import farm_bones
from farm_traversal import traverse_plot_with_fn
from maze_solver import maze_solver
from planting_cactus import farm_cactus
from planting_controller import resources_farming_controller, multi_drone_resources_farming_controller
from planting_helpers import alternate_planting, check_harvest_plant, just_harvest
from planting_pumpkin import pumpkin_farming
from utils import partial

items_with_underlying_cost = [Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Gold, Items.Bone]

def recursive_get_cost(item, amount, cost_accumulated=None):
	items_to_entity = {
		Items.Carrot: Entities.Carrot,
		Items.Pumpkin: Entities.Pumpkin, 
		Items.Cactus: Entities.Cactus,
		Items.Bone: Entities.Apple,
	}
	
	if cost_accumulated == None:
		cost_accumulated = {}

	# Base Case
	if item not in items_with_underlying_cost:
		if item in cost_accumulated:
			cost_accumulated[item] = cost_accumulated[item] + amount
		else:
			cost_accumulated[item] = amount
		
		return cost_accumulated
	
	else:

		# Special Case for Items.Gold
		if item == Items.Gold:
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			cost_accumulated[Items.Weird_Substance] = substance
			cost_accumulated[item] = amount

			return cost_accumulated

		# Add the current item itself to show intermediate requirements
		if item in cost_accumulated:
			cost_accumulated[item] = cost_accumulated[item] + amount
		else:
			cost_accumulated[item] = amount
		
		underlying_cost = get_cost(items_to_entity[item])
		for underlying_items in underlying_cost:
			cost_accumulated = recursive_get_cost(underlying_items, underlying_cost[underlying_items] * amount, cost_accumulated)
	
	return cost_accumulated
	

def calculate_total_cost(cost):
	total_cost = {}

	# Process each original item
	for item in cost:
		quantity = cost[item]
		if item in items_with_underlying_cost:
			# For items with underlying costs, use recursive_get_cost (which includes the item itself)
			recursive_cost = recursive_get_cost(item, quantity)
			
			for recursive_item in recursive_cost:
				recursive_quantity = recursive_cost[recursive_item]
				if recursive_item in total_cost:
					total_cost[recursive_item] = total_cost[recursive_item] + recursive_quantity
				else:
					total_cost[recursive_item] = recursive_quantity
		else:
			# For items without underlying costs, just add them directly
			if item in total_cost:
				total_cost[item] = total_cost[item] + quantity
			else:
				total_cost[item] = quantity

	return total_cost


def compute_farming_sequence(total_cost):
	custom_order = [Items.Weird_Substance, Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Bone, Items.Gold]
	reordered = {}

	# First, add the items that are in the custom order
	for key in custom_order:
		if key in total_cost:
			reordered[key] = total_cost[key]

	# Then, add everything else (in their original order)
	for key in total_cost:
		value = total_cost[key]  # Corrected indentation here
		if key not in custom_order:
			reordered[key] = value

	return reordered

compute_farming_sequence({ Items.Hay: 26316800, Items.Pumpkin: 100, Items.Wood: 26317300, Items.Carrot: 51400 })


def reset_race(unlocks_sequence):
	for unlocks, num in unlocks_sequence:

		unlock_cost = get_cost(unlocks, num)
		if Items.Carrot in unlock_cost:
			unlock_cost[Items.Carrot] = unlock_cost[Items.Carrot] * 3

		total_cost =  compute_farming_sequence(calculate_total_cost(unlock_cost))

		
		
		while not unlock(unlocks):
			# quick_print("Unlocking: ")
			# quick_print(unlocks)
			# quick_print(num)
			for item in total_cost:
				quantity = total_cost[item]
				clear()
				if num_unlocked(Unlocks.Megafarm) == 0:
					resources_farming_controller(quantity, item)
				else:
					multi_drone_resources_farming_controller(quantity, item)
		

if __name__ == "__main__":
	reset_race([
		(Unlocks.Plant, 0),
		(Unlocks.Expand, 0),
		(Unlocks.Speed, 0),
		(Unlocks.Carrots, 0),
		(Unlocks.Expand, 1),
		(Unlocks.Trees, 0),
		(Unlocks.Expand, 2),
		(Unlocks.Speed, 1),
		(Unlocks.Speed, 2),
		(Unlocks.Speed, 3),
		(Unlocks.Grass, 1),
		(Unlocks.Grass, 2),
		(Unlocks.Trees, 1),
		(Unlocks.Trees, 2),

		(Unlocks.Grass, 3),
		(Unlocks.Trees, 3),
		(Unlocks.Carrots, 1),
		
		(Unlocks.Grass, 4),
		(Unlocks.Trees, 4),
		(Unlocks.Carrots, 2),
		(Unlocks.Carrots, 3),
		(Unlocks.Carrots, 4),
		(Unlocks.Speed, 4),

		(Unlocks.Pumpkins, 0),
		(Unlocks.Watering, 0),
		(Unlocks.Fertilizer, 0),
		(Unlocks.Fertilizer, 1),
		(Unlocks.Fertilizer, 2),
		(Unlocks.Fertilizer, 3),
		#(Unlocks.Sunflowers, 0),
		(Unlocks.Cactus, 0),
		(Unlocks.Expand, 3),
		(Unlocks.Expand, 4),
		
		# (Unlocks.Expand, 5),

		# Upgrade Hay and Wood here again
		(Unlocks.Grass, 5),
		(Unlocks.Trees, 5),
		(Unlocks.Carrots, 5),

		(Unlocks.Grass, 6),
		(Unlocks.Trees, 6),
		(Unlocks.Carrots, 6),

		(Unlocks.Dinosaurs, 0),
		(Unlocks.Mazes, 0),

		# (Unlocks.Megafarm, 0),
		# (Unlocks.Megafarm, 1),
		# (Unlocks.Megafarm, 2),
		# (Unlocks.Megafarm, 3),
		# (Unlocks.Megafarm, 4),

		# (Unlocks.Polyculture, 0),
		# (Unlocks.Expand, 5),
		# (Unlocks.Expand, 6),
		
		(Unlocks.Trees, 7),
		(Unlocks.Grass, 7),
		(Unlocks.Carrots, 7),

		(Unlocks.Grass, 8),
		(Unlocks.Trees, 8),
		(Unlocks.Carrots, 8),

		(Unlocks.Grass, 9),
		(Unlocks.Trees, 9),
		(Unlocks.Carrots, 9),

		# (Unlocks.Leaderboard, 0),
		# (Unlocks.Expand, 6),
	])
	clear()
	traverse_plot_with_fn(just_harvest)
	
	clear()
	traverse_plot_with_fn(partial(alternate_planting, Entities.Tree, Entities.Bush, check_harvest_plant))
	traverse_plot_with_fn(just_harvest)

	clear()
	traverse_plot_with_fn(partial(check_harvest_plant, Entities.Carrot))
	traverse_plot_with_fn(just_harvest)

	clear()
	for _ in range(6):
		pumpkin_farming()

	for _ in range(16):
		farm_cactus()

	for _ in range(512):
		farm_bones()

	clear()
	maze_solver(1000000)
	unlock(Unlocks.Leaderboard)