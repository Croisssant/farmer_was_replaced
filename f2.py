def n_by_n_plot(size, plant):
	final_output = []
	for i in range(size):
		temp = []
		for j in range(size):
			temp.append(plant)
		final_output.append(temp)
	return final_output
		
def merge_plot_by_row(data):

	merged = []
	for _ in range(len(data[0])):
		merged.append([])
	
	for plot in data:
		for i in range(len(plot)):
			merged[i] =  merged[i] + plot[i]
	return merged
  
  
	
def merge_plot_by_col(plots_arr):
	merged = []
	for plot in plots_arr:
		merged = merged + plot
	return merged
	
plot_1 = n_by_n_plot(6, Entities.Bush)
plot_2 = n_by_n_plot(6, Entities.Grass)
plot_3 = n_by_n_plot(6, Entities.Tree)
plot_4 = n_by_n_plot(6, Entities.Grass)

row_1 = merge_plot_by_row([plot_1, plot_2])

row_2 = merge_plot_by_row([plot_3, plot_4])

final = merge_plot_by_col([row_1, row_2])

def check_and_harvest():
	if can_harvest():
		harvest()
		plant(final[get_pos_x()][get_pos_y()])
		
def move_untill_end(direction, ):
	for i in range(get_world_size() - 1):
		check_and_harvest()
		move(direction)

while True:	
	for i in range(get_world_size()):
		
		if i % 2 == 0:
			move_untill_end(North)
		else:
			move_untill_end(South)
		move(East)