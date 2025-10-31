from builtins import set
from multi_drone_planting import farm_weird_substance, multi_drone_weird_substance_farming
from utils import partial

DIRECTIONS = [North, East, South, West]
DIRECTIONS_INDEX = {
	North: 0,
	East: 1, 
	South: 2, 
	West: 3,
}

def create_maze():
	clear()

	plant(Entities.Bush)
		
	if get_entity_type() == Entities.Bush:
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

		if num_items(Items.Weird_Substance) >= substance:
			use_item(Items.Weird_Substance, substance)
			return 1
		
		else:
			#num_gold_required = target_amount - num_items(Items.Gold)
			# quick_print("Number of Substance needed")
			# quick_print(substance)
			if num_unlocked(Unlocks.Megafarm) == 0 or num_unlocked(Unlocks.Polyculture) == 0:
				farm_weird_substance(substance)
			else:
				multi_drone_weird_substance_farming(Items.Weird_Substance, substance)
		

def calc_left_right(index):
	turn_right_idx = (index + 1) % 4
	turn_right = DIRECTIONS[turn_right_idx]
	
	turn_left_idx = (index - 1) % 4
	turn_left = DIRECTIONS[turn_left_idx]

	return (turn_left_idx, turn_left), (turn_right_idx, turn_right)


def random_wall_hugger(index):
	(turn_left_idx, turn_left), (turn_right_idx, turn_right) = calc_left_right(index)
	
	if random() < 0.5:
		first_turn_direction = turn_left
		first_turn_idx = turn_left_idx
		
		second_turn_direction = turn_right
		second_turn_idx = turn_right_idx
		
	else:
		first_turn_direction = turn_right
		first_turn_idx = turn_right_idx
		
		second_turn_direction = turn_left
		second_turn_idx = turn_left_idx

	return (first_turn_idx, first_turn_direction), (second_turn_idx, second_turn_direction)


def right_wall_hugger(index):

	(turn_left_idx, turn_left), (turn_right_idx, turn_right) = calc_left_right(index)

	return (turn_right_idx, turn_right), (turn_left_idx, turn_left)


def left_wall_hugger(index):

	return calc_left_right(index)


def drone_navigating_fn(forward_direction, turning_decider):
	index = DIRECTIONS_INDEX[forward_direction]
	move(forward_direction)

	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True 
		
		(first_turn_idx, first_turn_direction), (second_turn_idx, second_turn_direction) = turning_decider(index)
		
		if can_move(first_turn_direction):
			move(first_turn_direction)
			forward_direction = first_turn_direction
			index = first_turn_idx
			
		elif can_move(forward_direction):
			move(forward_direction)
			
		elif can_move(second_turn_direction):
			move(second_turn_direction)
			forward_direction = second_turn_direction
			index = second_turn_idx
			
		else:
			# Turn Around
			index = (index - 2) % 4
			forward_direction = DIRECTIONS[index]
			move(forward_direction)


def drone_navigation_spawner(direction):
	rand_num = random() 
	if rand_num > 0.7:
		spawn_drone(partial(drone_navigating_fn, direction, random_wall_hugger))
	
	elif rand_num < 0.3:
		spawn_drone(partial(drone_navigating_fn, direction, left_wall_hugger))
		
	else:
		spawn_drone(partial(drone_navigating_fn, direction, right_wall_hugger))
	
		
def spawn_new_drone_decider(idx, opp_turn_direction, visited):
	turnaround_direction = DIRECTIONS[(idx - 2) % 4]
	curr_pos = (get_pos_x(), get_pos_y())
	
	if curr_pos in visited:
		return None
		
	if can_move(turnaround_direction) and can_move(opp_turn_direction) and num_drones() + 2 != max_drones():
		drone_navigation_spawner(turnaround_direction)
		drone_navigation_spawner(opp_turn_direction)
		return curr_pos
		
	return None

def drone_master():
	#change_hat(Hats.The_Farmers_Remains)
	# Visited to keep track of visited coordinates so that drone master doesn't spawn drones at the same location
	visited = set()
	forward_direction = North
	index = 0
	move(forward_direction)
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True
			
		m = measure()
		if m == None:
			while measure() == None:
				return 1
				
		turn_right_idx = (index + 1) % 4
		turn_right = DIRECTIONS[turn_right_idx]
		
		turn_left_idx = (index - 1) % 4
		turn_left = DIRECTIONS[turn_left_idx]
		
		if can_move(turn_left):
			
			pos = spawn_new_drone_decider(turn_left_idx, turn_right, visited)
			if pos != None:
				visited.add(pos)
				
			move(turn_left)
			forward_direction = turn_left
			index = turn_left_idx
			
		elif can_move(forward_direction):
			move(forward_direction)
			
		elif can_move(turn_right):
			
			pos = spawn_new_drone_decider(turn_right_idx, turn_left, visited)
			if pos != None:
				visited.add(pos)
				
			move(turn_right)
			forward_direction = turn_right
			index = turn_right_idx
			
		else:
			# Turn Around
			index = (index - 2) % 4
			turnaround_direction = DIRECTIONS[index]
			forward_direction = turnaround_direction
			move(turnaround_direction)
		
		
def maze_solver(target_amount):
	#change_hat(Hats.The_Farmers_Remains)
	while num_items(Items.Gold) < target_amount:
		if create_maze():
			if drone_navigating_fn(North, right_wall_hugger):
				continue
		else:
			break

def multi_drone_maze_solver(target_amount):
	#change_hat(Hats.The_Farmers_Remains)
	while num_items(Items.Gold) < target_amount:
		if create_maze():
			if drone_master():
				continue
		else:
			break

if __name__ == "__main__":
	#change_hat(Hats.The_Farmers_Remains)
	while True:
		if create_maze():
			if drone_master():
				continue
		else:
			break
			