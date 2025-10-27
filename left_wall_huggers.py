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
		
		if can_move(turn_left):
			move(turn_left)
			forward_direction = turn_left
			index = turn_left_idx
			
		elif can_move(forward_direction):
			move(forward_direction)
			
		elif can_move(turn_right):
			move(turn_right)
			forward_direction = turn_right
			index = turn_right_idx
			
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
	

def drone_navigation_spawner_left_huggers(direction):
	if direction == North:
		spawn_drone(drone_navigating_fn_starting_north)
	
	if direction == South:
		spawn_drone(drone_navigating_fn_starting_south)
	
	if direction == East:
		spawn_drone(drone_navigating_fn_starting_east)
	
	if direction == West:
		spawn_drone(drone_navigating_fn_starting_west)