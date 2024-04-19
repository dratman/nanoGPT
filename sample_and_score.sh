#!/bin/bash
python sample.py --out_dir="out-arith-char" >sampled.txt
python score_arithmetic.py <sampled.txt
