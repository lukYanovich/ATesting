import sys
import random as r

# var 5-3
count = 5  # число особей в популяции
size = 5  # диапазон
p1 = 0.07
p2 = 0.05


def create_population():
    bodies = []
    for i in range(count):
        body = [r.randint(-size, size) for j in range(5)]
        bodies.append(body)
    answer = [(fitness(*i), i) for i in bodies]
    return answer


def fitness(u, w, x, y, z):
    elem1 = w ** 2 * y
    elem2 = u ** 2 * w * x
    elem3 = w * x ** 2 * y ** 2
    elem4 = x * y ** 2
    elem5 = u * x * y ** 2
    result = -44
    return abs(elem1 + elem2 + elem3 + elem4 + elem5 - result)


def get_winner(koef_fitness):
    koef = [1 / koef_fitness[i] for i in range(len(koef_fitness))]
    _sum = sum(koef)
    position = r.uniform(0, _sum)
    winner, temp = 0, koef[0]
    for i in range(1, len(koef) + 1):
        if position <= temp:
            winner = i - 1
            break
        temp += koef[i]
    return winner


def reproduction(population):
    def mutation():
        def create_mutant(index, p):
            arr = []
            for i in range(len(children[index][1])):
                win = get_winner([1 / p, 1 / (1 - p)])
                if win == 0:
                    arr.append(r.randint(-size, size))
                else:
                    arr.append(children[index][1][i])
            child_mutant = fitness(*arr), arr
            return child_mutant

        koef_fitness_children = [i[0] for i in children]
        index_best = koef_fitness_children.index(min(koef_fitness_children))
        index_worse = koef_fitness_children.index(max(koef_fitness_children))
        children[index_best] = create_mutant(index_best, p1)
        children[index_worse] = create_mutant(index_worse, p2)

    def find_parent():
        parent_index = get_winner(koef_fitness)
        parent = temp_population[parent_index][1]
        parent_koef = temp_population[parent_index][0]
        del temp_population[parent_index]
        del koef_fitness[parent_index]
        return parent_index, parent, parent_koef

    children = []
    temp_population = population.copy()
    koef_fitness = [i[0] for i in temp_population]
    while len(temp_population) > 1:
        father_index, father, father_koef = find_parent()
        mother_index, mother, mother_koef = find_parent()
        arr = []
        for i in range(len(father)):
            win = get_winner([father_koef, mother_koef])
            if win == 0:
                arr.append(father[i])
            else:
                arr.append(mother[i])
        child = fitness(*arr), arr
        children.append(child)
    mutation()
    population.extend(children)


def selection(population):
    temp = []
    for i in range(count):
        win = r.randint(0, len(population) - 1)
        temp.append(population[win])
        del population[win]
    population.clear()
    population.extend(temp)


def find_answer(population):
    answer = -1, []
    for i in population:
        if i[0] == 0:
            answer = i
            break
    return answer


if __name__ == "__main__":
    def check():
        print(population)
        global answer
        answer = find_answer(population)
        return answer[0] != -1


    population = create_population()
    answer = 0, []
    while True:
        if check():
            break
        reproduction(population)
        if check():
            break
        selection(population)
    print(answer)
    sys.exit(0)
