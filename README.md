[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

This code uses a bash script to search through a csv file containing various information and pull out the number of fires in a particular country and print out those values.

## Assignment 4 (Testing) – v3.0
- Added mean, median, standard_deviation functions in my_utils.py.
- print_fires.py now supports --op (mean|median|std) to compute a statistic; otherwise it prints the raw list.
- test_my_utils.py (pytest) has random, positive, and negative tests.
- test_print_fires.sh is a simple bash test file that checks normal behavior and error exit codes.
- mini_agro.csv is a tiny dataset used for functional tests.
How to run:
  ./test_print_fires.sh
  pytest -q
  ./run.sh