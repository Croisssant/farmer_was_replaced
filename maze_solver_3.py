from MazeUtil2 import create_maze
from left_wall_huggers import drone_navigation_spawner_left_huggers
from random_wall_huggers import drone_navigation_spawner_random_huggers
from treasure_hunter import find_treasure

directions = [North, East, South, West]

def drone_navigating_fn(index, forward_direction):
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True 
		turn_right_idx = (index + 1) % 4
		turn_right = directions[turn_right_idx]
		
		turn_left_idx = (index - 1) % 4
		turn_left = directions[turn_left_idx]
		
		if can_move(turn_right):
			move(turn_right)
			forward_direction = turn_right
			index = turn_right_idx
			
		elif can_move(forward_direction):
			move(forward_direction)
			
		elif can_move(turn_left):
			move(turn_left)
			forward_direction = turn_left
			index = turn_left_idx
			
		else:
			# Turn Around
			index = (index - 2) % 4
			turnaround_direction = directions[index]
			forward_direction = turnaround_direction
			move(turnaround_direction)
			
def drone_navigating_fn_starting_north():
	forward_direction = North
	index = 0
	move(forward_direction)
	
	drone_navigating_fn(index, forward_direction)
	
def drone_navigating_fn_starting_south():
	forward_direction = South
	index = 2
	move(forward_direction)
	
	drone_navigating_fn(index, forward_direction)

def drone_navigating_fn_starting_east():
	forward_direction = East
	index = 1
	move(forward_direction)
	
	drone_navigating_fn(index, forward_direction)
	
def drone_navigating_fn_starting_west():
	forward_direction = West
	index = 3
	move(forward_direction)
	
	drone_navigating_fn(index, forward_direction)

def drone_navigation_spawner(direction):
	rand_num = random() 
	if rand_num > 0.7:
		drone_navigation_spawner_random_huggers(direction)
	
	elif rand_num < 0.3:
		drone_navigation_spawner_left_huggers(direction)
		
	else:
		if direction == North:
			spawn_drone(drone_navigating_fn_starting_north)
		
		if direction == South:
			spawn_drone(drone_navigating_fn_starting_south)
		
		if direction == East:
			spawn_drone(drone_navigating_fn_starting_east)
		
		if direction == West:
			spawn_drone(drone_navigating_fn_starting_west)
	
		
def spawn_new_drone_decider(idx, opp_turn_direction, visited):
	turnaround_direction= directions[(idx - 2) % 4]
	curr_pos = (get_pos_x(), get_pos_y())
	
	if curr_pos in visited:
		return None
		
	if can_move(turnaround_direction) and can_move(opp_turn_direction) and num_drones() + 2 != max_drones():
		drone_navigation_spawner(turnaround_direction)
		drone_navigation_spawner(opp_turn_direction)
		return curr_pos
	
	#elif can_move(turnaround_direction) and num_drones() != max_drones():
		#drone_navigation_spawner(turnaround_direction)
		#return curr_pos
		
	#elif can_move(opp_turn_direction) and num_drones() != max_drones():
		#drone_navigation_spawner(opp_turn_direction)
		#return curr_pos
		
	return None

def drone_master():
	change_hat(Hats.The_Farmers_Remains)
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
		turn_right = directions[turn_right_idx]
		
		turn_left_idx = (index - 1) % 4
		turn_left = directions[turn_left_idx]
		
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
			turnaround_direction = directions[index]
			forward_direction = turnaround_direction
			move(turnaround_direction)
		
	
if __name__ == "__main__":
	change_hat(Hats.The_Farmers_Remains)
	while True:
		if create_maze():
			if drone_master():
				continue
			