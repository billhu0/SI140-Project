import numpy as npy
import scipy.stats as st
import matplotlib.pyplot as plt

N: int = 6001
realProb = npy.array([0.8, 0.6, 0.5])  # real probability of arms

rea = npy.array([1,3,4,3,2,2,2,2,3])

rea.argmax

def EpsilonGreedy(epsilon: float) -> int:
    sumOfResult: int = 0  # sum of rewards
    theta = npy.zeros(3)  # experienced (posterior) probability
    count = npy.zeros(3)  # pulling count for each arm
    # Generate an r.v. with Bern(epsilon) distribution
    option = npy.random.binomial(1, epsilon, N)
    for t in range(N):
        # exploitation and exploration trade-off
        if option[t] == 0: # exploitation 
            # choose the arm with currently known greatest probability 
            arm = npy.argmax(theta)      
        else:              # exploration
            # randomly choose an arm to explore new possibilities
            arm = npy.random.randint(3)  
        # pull the arm and get the result
        reward = npy.random.binomial(1, realProb[arm])
        sumOfResult += reward
        # update 'count' and 'posterior probability'
        count[arm] += 1
        theta[arm] += (reward - theta[arm]) / count[arm]
    # after the whole game, return the sum of rewards
    return sumOfResult

def RepeatEpsilon(Repeats=200) -> None:
    result = npy.zeros(Repeats)
    epsilon_list = [0.2, 0.4, 0.6, 0.8]
    plt.figure(figsize=(13, 12))
    for k in range(4):
        ep = epsilon_list[k]
        for i in range(Repeats):
            result[i] = EpsilonGreedy(epsilon=ep)
        avg: float = npy.average(result)
        plt.subplot(2, 2, k+1)
        plt.bar(npy.arange(1, len(result)+1, 1), result)
        plt.title("Epsilon={}, avg reward={}".format(ep, avg))
        plt.xlabel("Game Rounds");  plt.ylabel("Sum of outcome")
        plt.xlim(1, len(result)+1); plt.ylim(3500, 5000)
        print("When epsilon={}, average result is {}, variance is {}".format(ep, avg, npy.var(result)))
    plt.show()

if __name__ == '__main__':
    RepeatEpsilon(Repeats=200)
