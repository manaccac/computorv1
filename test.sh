#!/bin/bash

equations=(
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    "2 * X^0 + 4 * X^1 = 1 * X^0"
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 + 2 - 5 = 1 * X^0"
    "2 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^1"
    "3 * X^0 + 2 * X^1 - 7 * X^2 = 0"
    "X^2 - 5 * X + 6 = 0"
    "2 * X^2 + 4 * X + 2 = 0"
    "4 * X^2 - 16 = 0"
    "X^2 + X + 1 = 0"
    "X^2 - 6 * X + 9 = 0"
    "X^3 + 2 * X^2 - X - 2 = 0"
    "3 * X^1 + 6 = 0"
    "2 * X^0 - 9 = 0"
    "X^2 + 1 = 0"
)

for equation in "${equations[@]}"; do
    python3 ./computor.py "$equation"
    echo
    echo
    echo
    echo "--------------------------"
    echo
    echo
    echo

done
