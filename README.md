# Welkin Documentation

[![Regularly check links](https://github.com/elastisys/welkin/actions/workflows/checklinks.yml/badge.svg)](https://github.com/elastisys/welkin/actions/workflows/checklinks.yml)

This is the main repository for documentation about the Welkin project. For Welkin code, please refer to:

- [`compliantkubernetes-kubespray`](https://github.com/elastisys/compliantkubernetes-kubespray) for setting up a vanilla Kubernetes Cluster on top of a compliant cloud provider;
- [`compliantkubernetes-apps`](https://github.com/elastisys/compliantkubernetes-apps) for augmenting a vanilla Kubernetes Cluster with security and observability.

## Prerequisites

```sh
make verify-prerequisites
```

## Usage

> [!NOTE]
> For Mac users, you might have to install Cairo: `brew install cairo`

```sh
make serve
```

## Advanced Usage

```sh
make help
```

## Tech Stack

- [make](https://linux.die.net/man/1/make)
- [mkdocs](https://www.mkdocs.org/)
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages](https://pages.github.com/)
- [Graphviz](https://graphviz.org/)
- [mike](https://github.com/jimporter/mike)
- [sass](https://www.npmjs.com/package/sass)

## Deployment

GitHub Actions will deploy the `main` branch automatically.

## Known Issues

### `nodeenv` provided with Ubuntu 24.04 is old

If you get the following errors:

```console
$ pre-commit run --all
[...]
An unexpected error has occurred: CalledProcessError: command: ('/usr/bin/python3', '-mnodeenv', '--prebuilt', '--clean-src', '/home/cklein/.cache/pre-commit/repoxgjtxt_g/node_env-default')
[...]
      File "/usr/lib/python3/dist-packages/nodeenv.py", line 881, in main
        opt.node = get_last_stable_node_version()

                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Then this could be caused by the version of `nodeenv` delivered with Ubuntu 24.04.
You have two options.

#### Option 1: Run pre-commit from a virtual environment

1. Remove Ubuntu's pre-commit and `nodeenv`: `sudo apt purge nodeenv --autoremove`.
1. Activate the virtual environment you created above: `. .venv/bin/activate`.
1. Install pre-commit in the virtual environment: `pip install pre-commit`.
1. Run pre-commit from the virtual environment: `pre-commit run --all`.

#### Option 2: Break system package

```shell
sudo apt install pre-commit
sudo apt install python3-pip
sudo pip install nodeenv --break-system-packages --upgrade
```

## 📜 Licensing Information

All source files in this repository are licensed under the Apache License, Version 2.0 unless otherwise stated.
See the [LICENSE](LICENSE.md) file for full details.
