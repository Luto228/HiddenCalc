<div align="center">

# HiddenCalc

**A digital prototype of a real calculator with hidden games.**

Calculate now. Discover more as the project grows.

</div>

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

The calculator is usable. Entering `sqrt(14+24)` currently triggers a hidden input check, but game selection and the mini-games are not implemented yet. The ideas below may change as the project develops.

Once the digital version is ready, the plan is to bring HiddenCalc to a physical device.

## Planned mini-games

After entering the secret expression, the plan is to choose a game by typing `1`, `2`, or `3`:

1. **Quick math:** Solve a randomly generated math problem as fast as you can.
2. **Countdown:** Type a number shown on screen before it decreases again (for example, `947 → 946 → 945`).
3. **Number builder:** Press digits to add them to a running total. Starting at `0`, pressing `9` and then `3` produces `12`. Build the highest total you can before time runs out.

## License

Released under the [MIT License](LICENSE).
