#!/bin/bash
gcc -o fork fork.c
./fork
python graph_process.py
