import random
'''
This function will calculate the result of the dice roll based on the dice roll pattern
'''


def cubes(pattern):
    cubes_type = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")
    for each in cubes_type:
        patter_split = pattern.split(each)
        if len(patter_split) == 2:
            throw_num = int(patter_split[0])
            modifier = int(patter_split[1])
            our_cube = int(each.split("D")[1])
            throw_result = 0
            for i in range(throw_num):
                throw = random.randint(1, our_cube)
                throw_result += throw
            return throw_result + modifier
    else:
        return "No cube like this"


print(cubes("3D6+10"))
