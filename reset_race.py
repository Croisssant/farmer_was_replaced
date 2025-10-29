from planting_controller import resources_farming_controller, multi_drone_resources_farming_controller

# Prints a dictionary of total cost
total_cost = get_cost(Unlocks.Leaderboard, 0)
 


# Prints the cost of planting a carrot, therefore, before the final loop, multiply each needed resource with carrot(the target), then first farm for the required basic resources
# then only farm for carrot
print(get_cost(Entities.Carrot))

def calculate_cost(target_unlock):
	total_cost = get_cost(Unlocks.Leaderboard, 0)

# for item in total_cost:
#     print(item)
#     print(total_cost[item])
# clear()
# set_world_size(16)
# multi_drone_resources_farming_controller(85500000000000, Items.Gold)
