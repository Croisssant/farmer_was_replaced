from farm_traversal import traverse_plot_with_fn
from planting_helpers import check_harvest_plant, sunflower_boost, alternate_planting, just_harvest
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
						Items.Hay
					)
				  
			case Items.Wood:
				if num_unlocked(Unlocks.Trees) == 0:
					farm_plant(
						partial(check_harvest_plant, Entities.Bush),
						target_amount,
						Items.Wood
					)
				else:
					farm_plant(
						partial(alternate_planting, check_harvest_plant, Entities.Tree, Entities.Bush),
						target_amount,
						Items.Wood
					)

			case Items.Carrot:
				print()

			case Items.Pumpkin:
				print()

			case Items.Cactus:
				print()

			case Items.Bone:
				print()

			case Items.Weird_Substance:
				print()

			case Items.Gold:
				print()
					 
	else:
		match resource:
			case Items.Wood:
				farm_plant(
					partial(alternate_planting, sunflower_boost, Entities.Tree, Entities.Bush),
					target_amount,
					Items.Wood
				)
			   
		
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
