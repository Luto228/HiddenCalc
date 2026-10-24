# HiddenCalc

A Python calculator with hidden mini-games.

## About

HiddenCalc is currently a Python-based digital prototype. The long-term goal is to turn it into a real, physical calculator with hidden mini-games. This version is where the calculator and game ideas are being developed.

## Features

- Calculate with `+`, `-`, `*`, `/`, and `%`.
- Find square roots with `sqrt(x)`.
- Keep entering expressions until you type `exit`.
- Get a clear error message for division by zero or an invalid expression.

## Getting started

You'll need Python 3. No third-party packages are required.

Clone the repository and start the calculator:

```bash
git clone https://github.com/Luto228/HiddenCalc.git
cd HiddenCalc
python main.py
```

On Windows, you can use `py main.py` if `python` isn't available as a command.

## Example

```text
Calculator is running. Type 'exit' to quit.
Supported operations: +, -, *, /, %, sqrt(x)

Input expression: 12 * 3
Result: 36

Input expression: sqrt(144)
Result: 12.0

Input expression: exit
Exiting the calculator.
```

> [!NOTE]
> This is an early prototype. Expressions are evaluated with Python's `eval()`, so only enter expressions you trust.

## Project status

The calculator is usable, and all three hidden games can be launched from the menu. Enter `sqrt(14+24)` in the calculator, then choose `1` for **Quick math**, `2` for **Guess the number**, or `3` for **Target sum**. The third game is playable, with more features planned.

Quick math is complete and accepts decimal answers. For a non-integer result, enter it rounded to three digits after the decimal point (for example, `22 / 49` becomes `0.449`).

Once the digital version is ready, the plan is to bring HiddenCalc to a physical device.

## Mini-games

After entering the secret expression, type `1`, `2`, or `3` to choose a game:

1. **Quick math (ready):** Solve randomly generated math problems until you give an incorrect answer. Round non-integer answers to three decimal places.
2. **Guess the number (ready):** Guess a randomly chosen integer from `1` to `1000`. After each incorrect guess, the game indicates whether the secret number is higher or lower. Keep guessing until you find it.
3. **Target sum (playable):** The game picks a target number from `10` to `634`. Enter one digit (`0` to `9`) at a time to add it to your total and reach the target as quickly as you can. If your total goes over the target, you lose. A timer and a limit on how often each digit can be used are planned.

## License

Released under the [MIT License](LICENSE).
