import matplotlib.pyplot as plt
import numpy as np


class Dice:
    def __init__(self, num_dice: int):
        self.num_dice = num_dice

    def play(self, number_of_times: int) -> np.ndarray:
        results: np.ndarray = np.random.randint(1, 7, size=(self.num_dice, number_of_times))
        results = results.sum(0)
        return results

    def plot(self, results: np.ndarray):
        xaxis = np.arange(self.num_dice, 6 * self.num_dice + 1)
        bincount = np.bincount(results, minlength=6 * self.num_dice + 1)[self.num_dice:]

        color = ["tab:blue"] * xaxis.size
        mean_value = np.mean(xaxis[[0, -1]])
        if mean_value % 1 == 0:
            color[np.where(xaxis == mean_value)[0].item()] = "tab:green"
        else:
            color[np.where(xaxis == np.floor(mean_value))[0].item()] = "tab:green"
            color[np.where(xaxis == np.ceil(mean_value))[0].item()] = "tab:green"

        plt.bar(xaxis, bincount, color=color)
        plt.xticks(xaxis)
        plt.show()


def main():
    num_dice = 3
    number_of_times = 10000

    dice = Dice(num_dice)
    results = dice.play(number_of_times)
    dice.plot(results)


if __name__ == "__main__":
    main()
