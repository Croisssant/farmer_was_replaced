def move_untill_end(direction, fn):
	for i in range(get_world_size()):
		fn()
		
		if i == (get_world_size() - 1):
			move(East)
		else:
			move(direction)

def traverse_plot_with_fn(fn):
	for i in range(get_world_size()):	
		if i % 2 == 0:
			move_untill_end(North, fn)
		else:
			move_untill_end(South, fn)	

if __name__ == "__main__":
	traverse_plot_with_fn(harvest)