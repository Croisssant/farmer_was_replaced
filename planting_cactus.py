from Ultimate_Planting import traverse_plot_with_fn
from basic_checks import should_till

def plant_cactus():
	curr_plant = Entities.Cactus
	should_till(curr_plant)
	plant(curr_plant)

traverse_plot_with_fn(plant_cactus)