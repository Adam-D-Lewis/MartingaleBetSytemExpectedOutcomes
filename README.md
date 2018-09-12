# Martingale Betting System Expected Outcomes
A common gambling strategy is known as the Martingale System (https://en.wikipedia.org/wiki/Martingale_(betting_system)).
I was curious what the expected outcomes were of using it in Roulette, so I calculated them and I plot them here in a 3d plot.

The idea is you play roulette, betting on red each time.  You double your bet each time you lose, and you only reset your bet to the original value once you win.  Seems like a sure thing, but let's calculate the expected outcomes.  That fact that tables have min and max bet limits throws a wrench in things.

The expected outcome is how much on average you will lose or win each "set" where you play until you have either won, or can no longer increase bet by your increase factor without exceeding the table max bet limit.

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

As can be seen, all expected outcomes are negative for the player.  The "steps" in the plot come from the fact that you will play a different number of games based on your initial bet amount and your bet increase factor.  
```
If your initial bet is $500 and the max table limit is $500.  You will play only a single game.
The expected outcome is your (win proabability-loss probability) * the bet amount (0.48-0.52)*500=-$20.
This agrees with the results shown in the plot.
```

## Authors

* **Adam Lewis** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
