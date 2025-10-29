from utils import should_till, get_xy, isEven, partial
from farm_traversal import traverse_plot_with_fn


def traverse_plant_and_harvest_sunflower():
	traverse_plot_with_fn(partial(check_harvest_plant, Entities.Sunflower))
	traverse_plot_with_fn(harvest)

def plant_weird_substance():
	if can_harvest():
		harvest()
		use_item(Items.Fertilizer)

def farm_weird_substance(target_amount):
	while num_items(Items.Weird_Substance) < target_amount:
		traverse_plot_with_fn(plant_weird_substance)

def just_harvest():
	if can_harvest():
		harvest()
		
def if_sunflower_then_plant(curr_plant):
    if can_harvest():
        harvest()
        if curr_plant == Entities.Sunflower:
            plant(Entities.Sunflower)

def check_harvest_plant(curr_plant):
	if can_harvest():
		harvest()
		should_till(curr_plant)
		plant(curr_plant)
		
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		
	if get_entity_type() == None:
		plant(curr_plant)
		
 
def sunflower_boost(curr_plant, planting_fn=check_harvest_plant):
	pos_x, pos_y = get_xy()
	
	should_plant_sunflower_top = (pos_y == (get_world_size() - 1) and isEven(pos_x))
	should_plant_sunflower_bottom = pos_y == 0 and not isEven(pos_x)
	if should_plant_sunflower_top or should_plant_sunflower_bottom:
		curr_plant = Entities.Sunflower

	planting_fn(curr_plant)


def alternate_planting(plant_a, plant_b, planting_fn):
	pos_x, pos_y = get_xy()

	if isEven(pos_x):
		if isEven(pos_y):
			planting_fn(plant_a)
		else:
			planting_fn(plant_b)
	else:
		if isEven(pos_y):
			planting_fn(plant_b)
		else:
			planting_fn(plant_a)


def targeted_planting(plot_layout):
	pos_x, pos_y = get_xy()
	curr_plant = plot_layout[pos_y][pos_x]
	check_harvest_plant(curr_plant)


def water_n_times(n=5, moving_direction=East):
	for _ in range(get_world_size() * n):
		use_item(Items.Water)
		move(moving_direction)