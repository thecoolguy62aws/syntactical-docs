# Introduction

Syntactical is a programming language. It's not a compiler or a interpreter. Instead, it's a transpiler. It transpiles the code you write into Python, then runs it.

**_THIS SECTION IS NOT FINISHED_**

# Installation

To install Syntactical, follow these steps depending on your package manager:

## pip

1. Open a terminal.
2. Type in: `pip install syntactical` (change command accordingly if you use `pip3`), then press enter.
3. Syntactical will be installed on your machine.
4. You can now use Syntactical with the `syn` or `syntactical` commands in your terminal.
5. If a new version of Syntactical gets released and you want to install it, type this command in your terminal: `python -m pip install --upgrade syntactical` (change command accordingly if you use `python3` and/or `pip3`), and press enter.

**Suggestion**: When using Syntactical, it's recomended to use Visual Studio Code with the [Syntactical extension](https://marketplace.visualstudio.com/items?itemName=thecoolguy62aws.syntactical).

The PyPi page for Syntactical can be found [here](https://pypi.org/project/syntactical/).

# Builtin Functions

Syntactical has built in functions. Some of them I will referance from their Python alternatives. Here's all the functions and what they do:

- `print()`, this function is not exactly like Python's `print()`. The only difference is that it doesn't make a newline after printing.
- `println()` is exactly the same as Python's `print()`
- `input()` is exactly the same as Python's `input()`
- `system()` runs a command on the user's operating system. When using this there will only be support for one OS (unless two OS's support one command). The command should be one string (with the arguments in the same string).
- `json_encodes()` is exactly the same as Python's `json.dumps()`
- `json_decodes()` is exactly the same as Python's `json.loads()`
- `json_encode()` is exactly the same as Python's `json.dump()`
- `json_decode()` is exactly the same as Python's `json.load()`
- Some other functions may be included that are not here yet.

This might not look like many, but it is not including the other features in the language.

**_THIS SECTION IS NOT FINISHED_**

# Modules

To add modules to your Syntactical file, use the `use` statement in your code. The `use` statement works exactly like Python's `import` statement. The `from` statement can also be used like in Python (except replace `import` with `use`). Here's a full list of the current supported modules in Syntactical (may be out of date):

- sys
- argparse
- os
- requests
- pathlib
- numpy
- json
- datetime
- re
- matplotlib
- django
- flask
- pygame
- tkinter
- time
- cryptography
- pynput
- pick

**_THIS SECTION IS NOT FINISHED_**


# Info
To view the source code, markdown, info, and license of this web page go [here](https://github.com/thecoolguy62aws/syntactical-docs/).