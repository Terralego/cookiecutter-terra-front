# {{cookiecutter.name.upper()}}

# Initialise your development environment

All following commands must be run only once at project installation.

## First clone

```sh
git clone --recursive {{cookiecutter.git_project_url}}
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

## Install

```commandline
npm i
```

## Launch

```commandline
npm start
```

## Tests

```commandline
npm test
```

## Notes

### Add Library in mode dev

```commandline
npm i {nameModule}` -D
```

### Mode debug map/layer in console

```js
localStorage.debug='terralego:*'
```

### Update a specific module

```commandline
npm i mc-tf-test
```

# Doc for deployment on environments
- [See here](./.ansible/README.md)

## how to test locally

build dockers
```
./control.sh build
```

build js app
```
./control.sh usershell npm run-script build
```

run node/devserver
```
./control.sh fg
```

run nginx
```
./control.sh up --force-recreate nginx
```

run shell in node/devserver
```
./control.sh usershell npm run-script build
./control.sh shell npm run-script build  # as root
```

run shell nginx
```
APP_CONTAINER=nginx ./control.sh shell
```
