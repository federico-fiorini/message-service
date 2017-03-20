#!/bin/bash

case "$1" in
--help)
  printf "\nUsage:  ./start-docker-compose.sh [OPTION]\n\nStart docker containers\n\nOptions:\n  update    re-build images\n\n"
  ;;
"")
  printf "\nStarting docker containers\n"
  docker-compose up -d
  ;;
update)
  printf "\nRe-building images and starting docker containers\n"
  docker-compose up --build -d
  ;;
*)
  printf "\nUnknown option '$1'\nRun './start-docker-compose.sh --help' for more information\n\n"
  ;;
esac