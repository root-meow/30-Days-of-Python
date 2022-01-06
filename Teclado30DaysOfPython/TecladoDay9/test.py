fav_flowers = ("Roses", "Gardenias", "Tulips")
flower_lovers = ("Moses", "Daniel", "Abe", "Gabe") # When the two items are diff lengths, past where lengths are same, it is ignored

flower_lovers_and_fav_flowers = zip(flower_lovers, fav_flowers)

print(tuple(flower_lovers_and_fav_flowers))

"""for fav_flowers, flower_lovers in zip(fav_flowers, flower_lovers):
	print(f"{flower_lovers} loves {fav_flowers}.")"""
