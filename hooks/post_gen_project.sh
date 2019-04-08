#!/usr/bin/env bash

set -e

USERNAME="{{ cookiecutter.github_username }}"
REPO_NAME="{{ cookiecutter.github_repository }}"
REPO_DESCRIPTION="{{ cookiecutter.description }}"

hub init
hub create
travis enable --com --no-interactive
echo "Setting up PyPi package release:"
echo -n "PyPi password: "
read -s PASSWORD
echo "            secure: $(travis encrypt --com --no-interactive "$PASSWORD")" >> .travis.yml
unset PASSWORD

hub add --all
hub commit -m 'Initial package boilerplate'
hub push --set-upstream origin master
open "https://github.com/$USERNAME/$REPO_NAME"
