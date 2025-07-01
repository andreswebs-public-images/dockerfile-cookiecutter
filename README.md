# dockerfile-cookiecutter

[Cookiecutter](https://www.cookiecutter.io/) template to generate a basic Dockerfile
project.

## Pre-requisites

### cookiecutter

Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable).

We recommend using [uv](https://docs.astral.sh/uv/) to manage the Python environment. Below is one way to get started for [Homebrew](https://brew.sh) users. Follow the [cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html) for other methods.

```sh
brew install uv
```

```sh
# uv python install ## (Optional) if you haven't installed python with uv yet
uv venv
source .venv/bin/activate
uv pip install cookiecutter
```

## Run

```sh
cookiecutter gh:andreswebs-public-images/dockerfile-cookiecutter
```

## Authors

**Andre Silva** - [@andreswebs](https://github.com/andreswebs)

## License

This project is licensed under the [Unlicense](UNLICENSE).
