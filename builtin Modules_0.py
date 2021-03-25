import random
ran_num = random.randint(1, 5)
# 1-5 random num generate garxa
print(ran_num)

ran_float_num = random.random()
print(ran_float_num)

# random.random function le parameter bhitra kunai pani argument linna
# ani random float no. haru 0-1 matra linxa
# 0 to bhanda badi ko no. lina xa bhane tyo code ko last ma desired end no. le multiply garni
ran_float_num = random.random()*100
print(ran_float_num)

lisy = ["Naruto", "One Piece", "Attack on Titan"]
ran_word = random.choice(lisy)
print(ran_word)