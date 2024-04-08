# Compliant Kubernetes Documentation

[![Regularly check links](https://github.com/elastisys/compliantkubernetes/actions/workflows/checklinks.yml/badge.svg)](https://github.com/elastisys/compliantkubernetes/actions/workflows/checklinks.yml)

This is the main repository for documentation about the Compliant Kubernetes project. For Compliant Kubernetes code, please refer to:

* [`compliantkubernetes-kubespray`](https://github.com/elastisys/compliantkubernetes-kubespray) for setting up a vanilla Kubernetes cluster on top of a compliant cloud provider;
* [`compliantkubernetes-apps`](https://github.com/elastisys/compliantkubernetes-apps) for augmenting a vanilla Kubernetes cluster with security and observability.

## Prerequisites

Python 3. Should already be present on any decent Linux/macOS.


For generating figures, please install:

```
sudo apt-get install graphviz make
```

For generating `docs/stylesheets/style.css`, please install:

```
npm install -g sass
```

## Usage

To view locally:

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

mike serve
```

* To re-generate figures: `make -C docs/img`. **For simplicity, please commit generated figures. Prefer PNG (width == 1200px), to facilitate embedded logos.**
* For continuous preview of figures: `make -C docs/img preview`.
* To generate `docs/stylesheets/style.css`, please use `sass extra_sass/style.css.scss > docs/stylesheets/style.css`.

## Tech Stack

* [mkdocs](https://www.mkdocs.org/)
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
* [GitHub Pages](https://pages.github.com/)
* [Graphviz](https://graphviz.org/)
* [mike](https://github.com/jimporter/mike)
* [sass](https://www.npmjs.com/package/sass)

## Deployment

GitHub Actions will deploy the `main` branch automatically.
