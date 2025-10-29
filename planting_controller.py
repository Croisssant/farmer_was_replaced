from dino_movements import farming_bones_loop
from farm_gold import multi_drone_gold_farming
from farm_traversal import traverse_plot_with_fn
from maze_solver import maze_solver
from multi_drone_planting import multi_drone_plant_farming, multi_drone_weird_substance_farming, multi_drone_wood_farming
from planting_cactus import farming_cactus_loop, multi_drone_cactus_farming_loop
from planting_helpers import check_harvest_plant, sunflower_boost, alternate_planting, just_harvest, if_sunflower_then_plant, farm_weird_substance
from planting_pumpkin import multi_drone_pumpkin_farming
from utils import partial

def farm_plant(planting_fn, target_amount, resource):
	while num_items(resource) < target_amount:
		traverse_plot_with_fn(planting_fn)
		
def planting_controller(target_amount, resource):
    if num_unlocked(Unlocks.Sunflowers) == 0:
        if resource == Items.Hay:
            farm_plant(
                just_harvest,
                target_amount,
                resource
            )
                  
        elif resource == Items.Wood:
            if num_unlocked(Unlocks.Trees) == 0:
                farm_plant(
                    partial(check_harvest_plant, Entities.Bush),
                    target_amount,
                    resource
                )
            else:
                farm_plant(
                    partial(alternate_planting, Entities.Tree, Entities.Bush, check_harvest_plant),
                    target_amount,
                    resource
                )

        elif resource == Items.Carrot:
            farm_plant(
                partial(check_harvest_plant, Entities.Carrot),
                target_amount,
                resource
            )

        elif resource == Items.Pumpkin:
            farm_plant(
                partial(check_harvest_plant, Entities.Pumpkin),
                target_amount,
                resource
            )
                     
    else:
        if resource == Items.Hay:
            farm_plant(
                partial(sunflower_boost, Entities.Grass, if_sunflower_then_plant),
                target_amount,
                resource
            )

        elif resource == Items.Wood:
            farm_plant(
                partial(alternate_planting, Entities.Tree, Entities.Bush, sunflower_boost),
                target_amount,
                Items.Wood
            )

        elif resource == Items.Carrot:
            farm_plant(
                partial(sunflower_boost, Entities.Carrot),
                target_amount,
                resource
            )

        elif resource == Items.Pumpkin:
            farm_plant(
                partial(sunflower_boost, Entities.Pumpkin),
                target_amount,
                resource
            )
               
		
def resources_farming_controller(target_amount, resource):
    if resource in [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin]:
        planting_controller(target_amount, resource)

    elif resource == Items.Cactus:
        farming_cactus_loop(target_amount)

    elif resource == Items.Bone:
        farming_bones_loop(target_amount)

    elif resource == Items.Weird_Substance:
        farm_weird_substance(target_amount)

    elif resource == Items.Gold:
        maze_solver(target_amount)
 

def multi_drone_resources_farming_controller(target_amount, resource):
 
    if resource == Items.Hay:
        multi_drone_plant_farming(Entities.Grass, resource, target_amount)

    elif resource == Items.Carrot:
        multi_drone_plant_farming(Entities.Carrot, resource, target_amount)

    elif resource == Items.Wood:
        multi_drone_wood_farming(resource, target_amount)

    elif resource == Items.Pumpkin:
        multi_drone_pumpkin_farming(target_amount)

    elif resource == Items.Cactus:
        multi_drone_cactus_farming_loop(target_amount)

    elif resource == Items.Bone:
        farming_bones_loop(target_amount)

    elif resource == Items.Weird_Substance:
        multi_drone_weird_substance_farming(target_amount)

    elif resource == Items.Gold:
        multi_drone_gold_farming(target_amount)
            
if __name__ == "__main__":
	# References for calling these functions
	# traverse_plot_with_fn(partial(check_harvest_plant, Entities.Bush))
	
	# traverse_plot_with_fn(partial(sunflower_boost, Entities.Bush))
	
	# traverse_plot_with_fn(
	# 	partial(alternate_planting, sunflower_boost, Entities.Tree, Entities.Bush)
	# )
	
    farm_plant(
		partial(alternate_planting, sunflower_boost, Entities.Tree, Entities.Bush),
		19000000000,
		Items.Wood
	)
