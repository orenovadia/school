'''
Plot theta as a function of thetha' for an object that emits uniformly in space
and moving in a reletivistic speed of beta
this is an assignment from class 2



'''
import matplotlib.pyplot as plt
import numpy as np

from my_plot import My_Plot

plt.subplot(111, projection='polar')
my_plt = My_Plot(increment_colors=True)
c = 3 * 10 * 18


def gama_of_beta(beta):
    return 1 / np.sqrt(1 - beta ** 2)


def calc_new_theta(thetha_tag, beta):
    gama = gama_of_beta(beta)
    tan_thetha = np.sin(thetha_tag) / (gama * (np.cos(thetha_tag) + beta))
    return np.arctan(tan_thetha)


def main():
    rows, cols = 4, 4
    for i, beta in enumerate([0.1, 0.3, 0.6, 0.7, 0.8, 0.9, 0.95, 0.97, 0.999]):
        thetha_tag = np.linspace(-np.pi / 2.1, np.pi / 2.1, 30)
        theta_front = calc_new_theta(thetha_tag, beta)
        theta_back = calc_new_theta(thetha_tag, -beta)
        theta = np.concatenate((theta_front, np.pi + theta_back), axis=0)
        thetha_tag = np.concatenate((thetha_tag, np.pi + thetha_tag), axis=0)

        ax = plt.subplot(rows, cols, i + 1, projection='polar')
        ax.set_rmax(2.0)
        ax.grid(True)
        ax.scatter(theta, np.ones_like(theta), color='r', linewidth=1)
        ax.scatter(thetha_tag, np.ones_like(theta) - 0.5, color='b', linewidth=1)
        ax.set_title("Theta with beta=%s" % beta, va='bottom')
    plt.show()


if __name__ == '__main__':
    main()
