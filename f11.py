from Ultimate_Planting import traverse_plot_with_fn, check_and_harvest
from s_walk import plant_sunflower
from targeted_move import move_to, move_to_xy

def infinite_planting():
	while True:
		traverse_plot_with_fn(check_and_harvest)
		
if __name__ == "__main__":
	if spawn_drone(infinite_planting):
		move_to_xy(11, 0)
		infinite_planting()