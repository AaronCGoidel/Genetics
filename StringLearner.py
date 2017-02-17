import random
import string

populationSize = 2048  # starting population
MUTATION_RATE = 0.25  # rate at which mutation occur in the genome
ELITISM_RATE = 0.1  # superior race rate
CHAR_SET = string.ascii_letters + string.punctuation + string.whitespace + string.digits

TARGET = input("Input Target String: ")  # target string


def randomString():
    return "".join([random.choice(CHAR_SET) for characters in range(len(TARGET))])


def calcFitness(test):
    return sum([abs(ord(test[chars]) - ord(TARGET[chars])) for chars in range(len(TARGET))])


def mate(population, buffer):
    bourgeoisie = int(populationSize * ELITISM_RATE)  # calculate elites 

    for i in range(bourgeoisie):
        buffer[i] = population[i]

    for i in range(bourgeoisie, populationSize):  # loop over the proletariat
        randomPointA = random.randint(0, populationSize / 2)
        randomPointB = random.randint(0, populationSize / 2)

        pos = random.randint(0, len(TARGET))

        buffer[i] = population[randomPointA][:pos] + population[randomPointB][pos:]  # Make Babies!!!!

        if random.random() < MUTATION_RATE:  # mutate guys (TMNT)
            pos = random.randint(0, len(TARGET) - 1)
            buffer[i] = buffer[i][:pos] + random.choice(CHAR_SET) + buffer[i][pos + 1:]


def main():
    population = [randomString() for homies in range(populationSize)]
    buffer = [randomString() for peeps in range(populationSize)]

    generation = 0
    test = calcFitness(population[0])

    while calcFitness(population[0]):
        generation += 1

        population = sorted(population, key=lambda c: calcFitness(c))

        print("[%03d]: Best (%04d)\t%s" % (generation, calcFitness(population[0]), population[0]))

        mate(population, buffer)
        population, buffer = buffer, population


if __name__ == "__main__":
    main()
