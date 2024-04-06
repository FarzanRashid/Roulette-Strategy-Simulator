# Roulette Game Strategy Simulator

Roulette is a popular casino game known for its spinning wheel and various betting options. In this game, players place bets on where they think a ball will land on a spinning wheel divided into numbered compartments. The game offers a variety of betting options, ranging from betting on a single number to various combinations of numbers, colors, and whether the number will be odd or even.

## About the Project

This project is a Python-based simulator for exploring various strategies in the game of roulette. It allows users to test different betting strategies and analyze their performance over multiple rounds of simulated gameplay.

## Features

- Simulate different strategies in the game of roulette.
- Analyze the performance of strategies over multiple rounds.
- Support for various types of bets including straight bets, split bets, street bets, and more.
- Adjustable parameters such as starting balance, bet size, and number of rounds.
- Visualizations to display results and statistics.

## Installation

1. Ensure you have Python 3.10 or above installed. If not, download and install Python from
   [python.org](https://www.python.org/downloads/).

2. Clone the repository:

    ```bash
    git clone https://github.com/FarzanRashid/Roulette-Strategy-Simulator.git
    ```

3. Navigate to the project directory:

    ```bash
    cd /path/to/roulette-strategy-simulator
    ```

4. Set the `src` folder in the Python path:

    - **Windows**:
      ```cmd
      set PYTHONPATH=%PYTHONPATH%;./src
      ```

    - **Unix/Linux/Mac**:
      ```bash
      export PYTHONPATH=$PYTHONPATH:./src
      ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the simulator:

    ```bash
    python3 -m roulette
    ```

2. Follow the on-screen instructions to select a strategy and start the simulation.

3. Analyze the results displayed after the simulation completes.

Alternatively, you can use Docker to run the simulator without worrying about Python dependencies.

1. Ensure you have Docker installed on your system. If not, download and install Docker from [docker.com](https://www.docker.com/get-started).

2. Build the Docker image:

    ```bash
    docker build -t roulette-simulator .
    ```

3. Run the Docker container:

    ```bash
    docker run -it roulette-simulator
    ```

This will start the simulator inside a Docker container, allowing you to explore different strategies in the game of roulette. Follow the on-screen instructions to select a strategy and start the simulation. After the simulation completes, you can analyze the results displayed.

## Strategies

The simulator currently includes the following strategies:

- **Martingale**: Double the bet amount after each loss, reset to the initial bet amount after a 
  win.
- **Cancellation**: A cancellation system where the player decides on a goal amount of winnings and 
  writes down a list of positive numbers that sum to the pre-determined amount.
- **Fibonacci**: Bet according to the Fibonacci sequence (each bet amount is the sum of the two 
  preceding bet amounts ) after losses, reset to the initial bet after a win.
- **SevenReds**: The SevenReds strategy waits for a sequence of seven consecutive red outcomes on 
  the roulette wheel and then starts betting on black. After a loss, the bet amount is multiplied, 
  and it's reset to the table minimum after a win. 
- **Random**: The Random strategy involves placing bets on the roulette table based purely on 
  chance, without any specific pattern or system. Each bet outcome is chosen randomly.
- **1-3-2-6**: In the 1-3-2-6 strategy, the player increases their bet after each win in a 
  predetermined sequence: the sequence starts with betting 1x the amount  of the table minimum, 
  bet 3x of the table minimum after the first win, bet 2x of the table minimum for the second 
  consecutive win and for the third win bet 6x the amount of table minimum. After a loss or 
  reaching the fourth consecutive win, the betting sequence resets to 1x of the table minimum.
