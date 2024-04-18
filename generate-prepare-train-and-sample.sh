#!/bin/bash
# To train and sample (xxx) data for nanoGPT:
# (Adjust training params in train_xxx_char.py, which
# is a config file, not an ordinary .py file)
# Generate training data file as one long text file

python generate_multiplication_facts.py

# Copy generated training data file to a designated output folder

cp random_multiplication_examples.txt data/arith_999x9999/input.txt
cd data/arith_999x9999

python arith_999x9999/prepare.py

cd ../..

python train.py config/train_arith_999x9999.py

python sample.py --out_dir=out/arith_999x9999
