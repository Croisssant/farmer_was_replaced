from planting_controller import resources_farming_controller, multi_drone_resources_farming_controller

items_with_underlying_cost = [Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Gold, Items.Bone]

# Prints a dictionary of total cost
#total_cost = get_cost(Unlocks.Cactus, 0)
#print(total_cost)


# Prints the cost of planting a carrot, therefore, before the final loop, multiply each needed resource with carrot(the target), then first farm for the required basic resources
# then only farm for carrot
#print(get_cost(Entities.Pumpkin))


def reset_race(unlocks_sequence):
	for unlocks, num in unlocks_sequence:
		cost =  get_cost(unlocks, num)
		calculate_underlying_cost(cost)


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
		underlying_cost = get_cost(items_to_entity[item])
		#print("Under")
		#print(underlying_cost)
		for underlying_items in underlying_cost:
			cost_accumulated = recursive_get_cost(underlying_items, underlying_cost[underlying_items] * amount, cost_accumulated)
			

	
	return cost_accumulated
	
def calculate_underlying_cost(cost):
	total_cost = {}

	for item in cost:
		quantity = cost[item]
		if item in items_with_underlying_cost:
			total_cost[item] = cost[item]
			further_underlying_cost = recursive_get_cost(item, quantity)

			for further_item in further_underlying_cost:
				further_item_quantity = further_underlying_cost[further_item]
				if further_item in total_cost:
					total_cost[further_item] = total_cost[further_item] + further_item_quantity
				else:
					total_cost[further_item] = further_item_quantity
		
		else:
			if item in total_cost:
				total_cost[item] = total_cost[item] + quantity
			else:
				total_cost[item] = quantity

	return total_cost
# => { Items.Wood: 1524, Items.Carrot: 200, Items.Hay: 1024, Items.Pumpkin: 100 }

# Answer should be
# => { Items.Wood: 26214900, Items.Carrot: 51200, Items.Hay: 26214400, Items.Pumpkin: 100 }

# print(get_cost(Entities.Carrot)) => { Items.Wood: 512, Items.Hay: 512 }
# print(get_cost(Entities.Pumpkin)) => { Items.Carrot: 512 }
# for item in total_cost:
#     print(item)
#     print(total_cost[item])
# clear()
# set_world_size(16)
# multi_drone_resources_farming_controller(85500000000000, Items.Gold)


# reset_race([
# 	#(Unlocks.Cactus, 0), 
# 	(Unlocks.Pumpkins, 0)
# ])



# calculate_underlying_cost(get_cost(Unlocks.Pumpkins, 0))
print(calculate_underlying_cost({ Items.Wood: 500, Items.Carrot: 200, Items.Pumpkin: 100 }))