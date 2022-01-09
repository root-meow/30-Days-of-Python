anime_titles = set()
animes = {"One Punch Man", "One Piece", "Bleach", "Kuroko no Basket", "HunterxHunter"}

anime_titles.update(animes)

other_animes = {"Stein's Gate", "Solo Leveling", "One Piece", "Tokyo Ghoul"}

animes_union = anime_titles.union(other_animes)
animes_sdifference = anime_titles.symmetric_difference(other_animes)
animes_intersect = anime_titles.intersection(other_animes)

print(animes_union)
print(animes_sdifference)
print(animes_intersect)