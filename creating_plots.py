def n_by_n_plot(size, plant):
	final_output = []
	for i in range(size):
		temp = []
		for j in range(size):
			temp.append(plant)
		final_output.append(temp)
	return final_output

def n_by_n_plot_alternate(size, plant_a, plant_b):
	final_output = []
	for i in range(size):
		temp = []
		if i % 2 == 0:
			for j in range(size):
				if j % 2 == 0:
					temp.append(plant_a)
				else:
					temp.append(plant_b)
		else:
			for j in range(size):
				if j % 2 == 0:
					temp.append(plant_b)
				else:
					temp.append(plant_a)
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
	
PLOT_SIZE = 4

row_1 = merge_plot_by_row([n_by_n_plot_alternate(PLOT_SIZE, "Entities.Tree" , "Entities.Grass"), n_by_n_plot(PLOT_SIZE, "Entities.Cactus"), n_by_n_plot(PLOT_SIZE, "Entities.Carrot"), n_by_n_plot(PLOT_SIZE, "Entities.Cactus")])

row_2 = merge_plot_by_row([n_by_n_plot(PLOT_SIZE, "Entities.Pumpkin"), n_by_n_plot(PLOT_SIZE, "Entities.Carrot"), n_by_n_plot(PLOT_SIZE, "Entities.Pumpkin"), n_by_n_plot_alternate(PLOT_SIZE, "Entities.Tree" , "Entities.Grass")])

row_3 = merge_plot_by_row([n_by_n_plot_alternate(PLOT_SIZE, "Entities.Tree" , "Entities.Grass"), n_by_n_plot(PLOT_SIZE, "Entities.Pumpkin"), n_by_n_plot(PLOT_SIZE, "Entities.Carrot"), n_by_n_plot(PLOT_SIZE, "Entities.Pumpkin")])

row_4 = merge_plot_by_row([n_by_n_plot(PLOT_SIZE, "Entities.Pumpkin"), n_by_n_plot_alternate(PLOT_SIZE, "Entities.Tree" , "Entities.Grass"), n_by_n_plot(PLOT_SIZE, "Entities.Cactus"), n_by_n_plot_alternate(PLOT_SIZE, "Entities.Tree" , "Entities.Grass")])

final = merge_plot_by_col([row_1, row_2, row_3, row_4])

for row in final:
	print('[{}]'.format(', '.join(row)) + ",")