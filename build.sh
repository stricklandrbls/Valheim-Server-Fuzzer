#!/bin/bash
DIR_BUILD="$PWD/build"

# Functions
clean(){
  echo "Removing build directory: $DIR_BUILD"
  rm -rf "$DIR_BUILD"
}
configure(){
  echo "Configuring project"
  cmake -S . -B "$DIR_BUILD"
}
build(){
  echo "Building project"
  cmake --build "$DIR_BUILD"
}
# Script Execution
case "$1" in
  -clean | -C)
    clean
  ;;
  -configure | -c)
    configure
  ;;
  -reinit | -R)
    clean && configure
  ;;
  -build | -b)
    build
  ;;
  *)
    echo "Invalid option $1"
  ;;
esac