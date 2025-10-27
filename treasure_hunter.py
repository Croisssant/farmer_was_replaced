opposite_directions = {
	North: South,
	South: North,
	East: West,
	West: East,
}


def find_treasure(visited, directions):
	
	if get_entity_type() == Entities.Treasure:
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		return True 
	
	pos = (get_pos_x(), get_pos_y())
	if pos in visited:
		return False
	visited.add(pos)
	
	for direction in directions:
		if can_move(direction):
			move(direction)
			if find_treasure(visited, directions):
				return True
			move(opposite_directions[direction])
	
	return False
		
def treasure_hunting_wrapper_drone_a():
	visited = set()
	if find_treasure(visited, [East, West, North, South]):
		return True
	else:
		return False

def treasure_hunting_wrapper_drone_b():
	visited = set()
	if find_treasure(visited, [North, South, East, West]):
		return True
	else:
		return False

def treasure_loop(i):
	drone_b = spawn_drone(treasure_hunting_wrapper_drone_b)
	if wait_for(treasure_hunting_wrapper_drone_a()) or wait_for(drone_b):
		print(i)
		return True
	return False
		
if __name__ == "__main__":
	for i in range(296):
		visited = set()
		if find_treasure(visited, [North, South, East, West]):
			print(i)
		else:
			print("Oh no")
		
	