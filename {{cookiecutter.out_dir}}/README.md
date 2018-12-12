# Initialise your development environment

All following commands must be run only once at project installation.

## First clone

```sh
git clone --recursive {{cookiecutter.git_url}}
git submodule init --recursive  # only the fist time
git submodule upate
```

## Install NVM

follow official procedures for
[nvm](https://github.com/creationix/nvm#install-script) 


# Use your development environment

## Update submodules

Never forget to grab and update regulary the project submodules:

```sh
git pull
git submodule init --recursive  # only the fist time
git submodule upate
```

## Always use npm using nvm

```sh
nvm install && nvm use  # only once per launched shell
nvm $args
```

## Doc for deployment on environments
- [See here](./.ansible/README.md)
