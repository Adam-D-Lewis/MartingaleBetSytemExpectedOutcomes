# Martingale Betting System Expected Outcomes
A common gambling strategy is known as the Martingale System (https://en.wikipedia.org/wiki/Martingale_(betting_system)).
I was curious what the expected outcomes were of using it in Roulette, so I calculated them and I plot them here in a 3d plot.

The idea is you play roulette, betting on red each time.  You double your bet each time you lose, and you only reset your bet to the original value once you win.  Seems like a sure thing, but let's calculate the expected outcomes.  That fact that tables have min and max bet limits throws a wrench in things.

This code lets you vary the amount you increase your bet by as well (rather than only doubling your bet, you could increase by 1.05 for example), as well as changing your initial bet amount.

## Getting Started

### Prerequisites
Numpy, matplotlib

### How to Run
Simply run the main.py file to generate the plot.  Feel free to modify the initial bet and bet increase factor (b0 and f) ranges as well as
the max and min bet amounts.

The monteCarloRouletteSim.py file was used to validate the results of the main.py script.

## Results
The results are included here for convenience.
![Results](./MartingaleResults.JPG)

## Authors

* **Adam Lewis** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
