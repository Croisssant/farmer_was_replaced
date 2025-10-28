from dino_movements import farming_bones_loop
from farm_traversal import traverse_plot_with_fn
from planting_cactus import farming_cactus_loop
from planting_helpers import check_harvest_plant, sunflower_boost, alternate_planting, just_harvest, if_sunflower_then_plant, plant_weird_substance
from utils import partial

def farm_plant(planting_fn, target_amount, resource):
	while num_items(resource) < target_amount:
		traverse_plot_with_fn(planting_fn)
		
def planting_controller(target_amount, resource):
    if num_unlocked(Unlocks.Sunflowers) == 0:
        match resource:
            case Items.Hay:
                  farm_plant(
                        just_harvest,
                        target_amount,
                        resource
                    )
                  
            case Items.Wood:
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

            case Items.Carrot:
                farm_plant(
                    partial(check_harvest_plant, Entities.Carrot),
                    target_amount,
                    resource
                )

            case Items.Pumpkin:
                farm_plant(
                    partial(check_harvest_plant, Entities.Pumpkin),
                    target_amount,
                    resource
                )
                     
    else:
        match resource:
            case Items.Hay:
                farm_plant(
                    partial(sunflower_boost, Entities.Carrot, if_sunflower_then_plant),
                    target_amount,
                    resource
                )

            case Items.Wood:
                farm_plant(
                    partial(alternate_planting, Entities.Tree, Entities.Bush, sunflower_boost),
                    target_amount,
                    Items.Wood
                )

            case Items.Carrot:
                farm_plant(
                    partial(sunflower_boost, Entities.Carrot),
                    target_amount,
                    resource
                )

            case Items.Pumpkin:
                farm_plant(
                    partial(sunflower_boost, Entities.Pumpkin),
                    target_amount,
                    resource
                )
               
		
def resources_farming_controller(target_amount, resource):
    match resource:
        case Items.Hay | Items.Wood | Items.Carrot | Items.Pumpkin:
            planting_controller(target_amount, resource)

        case Items.Cactus:
            farming_cactus_loop(target_amount)

        case Items.Bone:
            farming_bones_loop(target_amount)

        case Items.Weird_Substance:
            plant_weird_substance()

        case Items.Gold:
            print()
 
            
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
