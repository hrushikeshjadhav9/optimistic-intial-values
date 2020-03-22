import random
import matplotlib.pyplot as plt
import numpy as np

class Slot_machine():
    """ a simple slot machine """

    def __init__(self, mean):
        """

        :param mean: actual win rate
        mean_estimate: current mean estimate
        N: number of plays a the slot machine
        """
        self.mean = mean
        self.mean_estimate = 0
        self.N = 0
        self.x = 0

    def pull(self):
        """ modeled pull operation in a slot machine """
        self.x = self.mean + random.gauss(0,0.05)
        self.update()
        return self.x

    def update(self):
        """ updates mean estimate and tracks number of pulls """
        self.N += 1
        self.mean_estimate = (1.0 - (1.0 / self.N)) * self.mean_estimate + (1.0 / self.N) * self.x




def experiment(N, eps, *means):
    """ compares epsilon values given by user """
    all_sm = []
    for mean in means:
        all_sm.append(Slot_machine(mean))

    # choosing a random initial sm
    # current_best_sm = random.choice(all_sm)
    current_best_sm = all_sm[0]

    # records actual mean values of pulled slot machines
    all_pulls = []

    # records random values generated that decide between exploration / exploitation
    all_values = []

    current_best_values = []

    for _ in range(N):
        value = random.uniform(0,1)
        all_values.append(value)

        if value < eps:
            random_sm = random.choice(all_sm)
            random_sm.pull()
            all_pulls.append(random_sm.mean_estimate)

        else:
            index = np.argmax([sm.mean_estimate for sm in all_sm])
            current_best_sm = all_sm[index]
            current_best_sm.pull()
            all_pulls.append(current_best_sm.mean_estimate)

        current_best_values.append(current_best_sm.mean_estimate)

    return current_best_values, all_pulls


N = 100
eps03 = experiment(N, 0.03, 0.1, 0.3, 0.5)
eps05 = experiment(N, 0.05, 0.1, 0.3, 0.5)
eps1 = experiment(N, 0.1, 0.1, 0.3, 0.5)

plt.plot(eps03[0], label = "eps = 0.03")
plt.plot(eps05[0], label = "eps = 0.05")
plt.plot(eps1[0], label = "eps = 0.1")
plt.legend()

plt.ylabel("best mean estimate")
plt.xlabel("iteration")
plt.show()

plt.plot(eps03[1], label = "eps = 0.03")
plt.plot(eps05[1], label = "eps = 0.05")
plt.plot(eps1[1], label = "eps = 0.1")
plt.legend()

plt.ylabel("pulls")
plt.xlabel("iteration")
plt.show()
