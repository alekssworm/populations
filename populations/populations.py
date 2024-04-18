import random


def fitness_function(individual):
    target_string = "Hello, World!"
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target_string[i]:
            fitness += 1
    return fitness

def create_individual(length):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?") for _ in range(length))

def create_population(population_size, individual_length):
    return [create_individual(individual_length) for _ in range(population_size)]


def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    selected_indices = random.choices(range(len(population)), weights=probabilities, k=2)
    return [population[i] for i in selected_indices]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(individual, mutation_rate):
    mutated_individual = ""
    for char in individual:
        if random.random() < mutation_rate:
            mutated_individual += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?")
        else:
            mutated_individual += char
    return mutated_individual


def genetic_algorithm(target_string, population_size, mutation_rate, generations):
    population = create_population(population_size, len(target_string))
    for generation in range(generations):
        fitness_scores = [fitness_function(individual) for individual in population]
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation+1}: Best individual: {best_individual}, Fitness: {max(fitness_scores)}")
        if max(fitness_scores) == len(target_string):
            break
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    return best_individual


target_string = "Hello, World!"
population_size = 100
mutation_rate = 0.01
generations = 1000
best_individual = genetic_algorithm(target_string, population_size, mutation_rate, generations)
print(f"\nBest individual found: {best_individual}")

