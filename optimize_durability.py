import random
import sys


def display_data(hash):
    print("=========\n")
    print("Stats for Unbreaking I: \n")
    print(f"Average blocks broken: {hash['unbreaking_I']['avg']}")
    # print(f"Stats: {hash['unbreaking_I']['data']}")

    print("=========\n")
    print("Stats for Unbreaking II: \n")
    print(f"Average blocks broken: {hash['unbreaking_II']['avg']}")
    # print(f"Stats: {hash['unbreaking_II']['data']}")

    print("=========\n")
    print("Stats for Unbreaking III: \n")
    print(f"Average blocks broken: {hash['unbreaking_III']['avg']}")
    # print(f"Stats: {hash['unbreaking_III']['data']}")


def get_avg(hash):
    hash["unbreaking_I"]["avg"] = round((
        sum(hash["unbreaking_I"]["data"]) / len(hash["unbreaking_I"]["data"])), 0)

    hash["unbreaking_II"]["avg"] = round((
        sum(hash["unbreaking_II"]["data"]) / len(hash["unbreaking_II"]["data"])), 0)

    hash["unbreaking_III"]["avg"] = round((
        sum(hash["unbreaking_III"]["data"]) / len(hash["unbreaking_III"]["data"])), 0)


def get_probability_data():
    sample_size = int(input("Sample size: "))
    pickaxe_type = input(
        "Pickaxe type: ['wood', 'stone', 'iron', 'gold', 'diamond', 'netherite']\n").lower()

    base_stats = {"wood": 60, "stone": 132, "iron": 251,
                  "gold": 33, "diamond": 1562, "netherite": 2032}

    print("pickaxe type: ", pickaxe_type)
    if pickaxe_type in base_stats:
        base = base_stats[pickaxe_type]
    else:
        sys.exit("Error: not a valid pickaxe type.")

    hash = {"unbreaking_I": {"avg": [], "data": []}, "unbreaking_II": {
        "avg": [], "data": []}, "unbreaking_III": {"avg": [], "data": []}}

    for _ in range(sample_size):
        get_unbreaking_I_data(hash, base)
        get_unbreaking_II_data(hash, base)
        get_unbreaking_III_data(hash, base)

    get_avg(hash)
    return hash


def get_unbreaking_I_data(hash, base):
    counter = 0
    while base > 0:
        probability = random.randrange(2)
        if probability == 0:
            base -= 1
            counter += 1
        else:
            counter += 1
    hash["unbreaking_I"]["data"].append(counter)
    return hash


def get_unbreaking_II_data(hash, base):
    counter = 0
    while base > 0:
        probability = random.randrange(3)
        if probability == 0:
            base -= 1
            counter += 1
        else:
            counter += 1
    hash["unbreaking_II"]["data"].append(counter)
    return hash


def get_unbreaking_III_data(hash, base):
    counter = 0
    while base > 0:
        probability = random.randrange(4)
        if probability == 0:
            base -= 1
            counter += 1
        else:
            counter += 1
    hash["unbreaking_III"]["data"].append(counter)
    return hash


if __name__ == "__main__":

    hash = get_probability_data()
    display_data(hash)
