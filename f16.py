from targeted_move import move_to_xy
from basic_checks import should_till
plant_type, (x, y) = get_companion()
move_to_xy(x, y)

if can_harvest():
	harvest()
should_till(plant_type)
plant(plant_type)