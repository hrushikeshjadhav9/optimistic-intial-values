import random
import matplotlib.pyplot as plt
import numpy as np

class Slot_machine():
    """ a simple slot machine """

    def __init__(self, mean, upper_limit):
        """

        :param mean: actual win rate
        mean_estimate: current mean estimate
        N: number of plays a the slot machine
        """
        self.mean = mean
        self.mean_estimate = upper_limit
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




def experiment(N, upper_limit,  *means):
    """ compares epsilon values given by user """
    all_sm = [Slot_machine(mean, upper_limit) for mean in means]

    # records actual mean estimates of pulled slot machines
    all_pulls = np.empty(N)

    for i in range(N):

        index = np.argmax([sm.mean_estimate for sm in all_sm])
        x = all_sm[index].pull()
        all_pulls[i] = x

        # Tracking progress through time
        cumulative_average = np.cumsum(all_pulls)/(np.arange(N)+1)

    return all_pulls, cumulative_average


if __name__ == "__main__":

    # Number of plays / pulls.
    N = 1000
    pulls, cumulative_average = experiment(N, 1, 0.1, 0.3, 0.5)

    # plt.plot(pulls)
    # plt.ylabel("all slot machine pulls")
    # plt.xlabel("iteration")
    # plt.show()

    plt.plot(cumulative_average)
    plt.ylabel("cumulative average")
    plt.xlabel("pull count")
    plt.show()
