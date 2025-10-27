from for_all import for_all
def farm_weird_substance():
	if can_harvest():
		harvest()
		use_item(Items.Fertilizer)
for_all(harvest)
	