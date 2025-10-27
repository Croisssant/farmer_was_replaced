from farm_traversal import traverse_plot_with_fn
from utils import should_till

def plant_cactus():
	curr_plant = Entities.Cactus
	should_till(curr_plant)
	plant(curr_plant)

traverse_plot_with_fn(plant_cactus)