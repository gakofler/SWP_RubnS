import random

l = []
rounds = 1000
number_range = 45
statistics_dic = {}


def generate_lotto_numbers():
    generated_numbers = []

    local_number_range = number_range
    local_list = l.copy()

    for count in range(6):
        generated_number = random.randint(0, local_number_range - 1)

        element = local_list.pop(generated_number)
        generated_numbers.append(element)
        local_number_range -= 1

    return generated_numbers


def update_statistics(numbers):
    for number in numbers:
        statistics_dic[number] += 1


l = list(range(1, number_range + 1))

for i in range(1, number_range + 1):
    statistics_dic[i] = 0

print("Liste:", l)

for round in range(rounds):
    update_statistics(generate_lotto_numbers())

print("Statistik der gezogenen Zahlen:", statistics_dic)

