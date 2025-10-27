from utils import should_till, get_xy, isEven

def check_harvest_plant(curr_plant):

    if can_harvest():
        harvest()
        should_till(curr_plant)
        plant(curr_plant)
		
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
		
    if get_entity_type() == None:
        plant(curr_plant)
		
 
def sunflower_boost(planting_fn, curr_plant):
    pos_x, pos_y = get_xy()
    
    should_plant_sunflower_top = (pos_y == (get_world_size() - 1) and pos_x % 2 == 0)
    should_plant_sunflower_bottom = pos_y == 0 and pos_x % 2 != 0
    if should_plant_sunflower_top or should_plant_sunflower_bottom:
        curr_plant = Entities.Sunflower

    planting_fn(curr_plant)


def alternate_planting(planting_fn, plant_a, plant_b):
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

