from farm_traversal import traverse_plot_with_fn

def farm_plant(planting_fn, target_amount, some_amount, plant):
    while some_amount < target_amount:
        traverse_plot_with_fn(planting_fn(plant))