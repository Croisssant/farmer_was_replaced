from MazeUtil2 import wall_follow_left, wall_follow_right, move_towards_treasure

opposite_directions = {
	North: South,
	South: North,
	East: West,
	West: East,
}

DIRECTIONS = [North, South, East, West]

def create_maze():
	clear()
	plant(Entities.Bush)
	while get_entity_type()==Entities.Bush:
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		if num_items(Items.Weird_Substance) > substance:
			use_item(Items.Weird_Substance, substance)
			return 1
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		if num_items(Items.Fertilizer)==0:
			# I do not have trade unlocked
			#trade(Items.Fertilizer)
			return 0
			
		use_item(Items.Fertilizer)
	
def shuffle(lst):
	# Fisher–Yates shuffle algorithm
	n = len(lst)
	for i in range(n - 1, 0, -1):
		# pick a random index from 0 to i (inclusive)
		j = random() * (i + 1)
		# swap elements
		lst[i], lst[j] = lst[j], lst[i]
	return lst

def find_treasure(visited, directions):
	
	m = measure()
	if m == None:
		while measure() == None:
			return 1
				
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True 
	
	pos = (get_pos_x(), get_pos_y())
	if pos in visited:
		return False
	visited.add(pos)
	
	for direction in directions:
		if move(direction):
			if find_treasure(visited, directions):
				return True
			move(opposite_directions[direction])
	
	return False

def find_treasure_wrapper_1():
	visited = set()
	directions = [North, South, East, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_2():
	visited = set()
	directions = [North, South, West, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_3():
	visited = set()
	directions = [North, East, South, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_4():
	visited = set()
	directions = [North, East, West, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_5():
	visited = set()
	directions = [North, West, South, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_6():
	visited = set()
	directions = [North, West, East, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_7():
	visited = set()
	directions = [South, North, East, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_8():
	visited = set()
	directions = [South, North, West, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_9():
	visited = set()
	directions = [South, East, North, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_10():
	visited = set()
	directions = [South, East, West, North]
	return find_treasure(visited, directions)

def find_treasure_wrapper_11():
	visited = set()
	directions = [South, West, North, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_12():
	visited = set()
	directions = [South, West, East, North]
	return find_treasure(visited, directions)

def find_treasure_wrapper_13():
	visited = set()
	directions = [East, North, South, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_14():
	visited = set()
	directions = [East, North, West, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_15():
	visited = set()
	directions = [East, South, North, West]
	return find_treasure(visited, directions)

def find_treasure_wrapper_16():
	visited = set()
	directions = [East, South, West, North]
	return find_treasure(visited, directions)

def find_treasure_wrapper_17():
	visited = set()
	directions = [East, West, North, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_18():
	visited = set()
	directions = [East, West, South, North]
	return find_treasure(visited, directions)

def find_treasure_wrapper_19():
	visited = set()
	directions = [West, North, South, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_20():
	visited = set()
	directions = [West, North, East, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_21():
	visited = set()
	directions = [West, South, North, East]
	return find_treasure(visited, directions)

def find_treasure_wrapper_22():
	visited = set()
	directions = [West, South, East, North]
	return find_treasure(visited, directions)

def find_treasure_wrapper_23():
	visited = set()
	directions = [West, East, North, South]
	return find_treasure(visited, directions)

def find_treasure_wrapper_24():
	visited = set()
	directions = [West, East, South, North]
	return find_treasure(visited, directions)
	

def multi_drone_treasure_hunt():
	if get_entity_type() == Entities.Grass:
			return 1
	
	spawn_drone(wall_follow_left)
	spawn_drone(wall_follow_right)
	
	spawn_drone(find_treasure_wrapper_1)
	spawn_drone(find_treasure_wrapper_2)
	spawn_drone(find_treasure_wrapper_3)
	spawn_drone(find_treasure_wrapper_4)
	spawn_drone(find_treasure_wrapper_5)
	spawn_drone(find_treasure_wrapper_6)
	spawn_drone(find_treasure_wrapper_7)
	spawn_drone(find_treasure_wrapper_8)
	spawn_drone(find_treasure_wrapper_9)
	spawn_drone(find_treasure_wrapper_10)
	spawn_drone(find_treasure_wrapper_11)
	spawn_drone(find_treasure_wrapper_12)
	spawn_drone(find_treasure_wrapper_13)
	spawn_drone(find_treasure_wrapper_14)
	spawn_drone(find_treasure_wrapper_15)
	spawn_drone(find_treasure_wrapper_16)
	spawn_drone(find_treasure_wrapper_17)
	spawn_drone(find_treasure_wrapper_18)
	spawn_drone(find_treasure_wrapper_19)
	spawn_drone(find_treasure_wrapper_20)
	spawn_drone(find_treasure_wrapper_21)
	spawn_drone(find_treasure_wrapper_22)
	spawn_drone(find_treasure_wrapper_23)
	
	# Uses the bifurcation exploration strategy
	while num_drones() != max_drones():
		spawn_drone(move_towards_treasure)
		if get_entity_type() != Entities.Hedge:
			return 1
			
	find_treasure_wrapper_24()
	
	
if __name__ == "__main__":

	
	while True:
		if create_maze():
			if multi_drone_treasure_hunt():
				continue
	