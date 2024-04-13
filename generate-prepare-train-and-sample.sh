#!/bin/bash
# To train and sample arith (xxx) data for nanoGPT:
# (Maybe adjust training params in train_xxx_char.py, which is a
# config file, not an ordinary .py file)
# Generate training data file as one long text file

cd ~/rdLLMScape/nanoGPT
python data/arith_char/generate_multiplication_facts.py

# Copy generated training data file to data/xxx_char/input.txt
# (where xxx = arith, shakespeare, etc.)
# (watch out for xxx-char vs xxx_char naming screwups)

cp random_multiplication_examples.txt data/arith_char/input.txt
cd data/arith_char

python prepare.py

cd ~/rdLLMScape/nanoGPT

python train.py config/train_arith_char.py
python sample.py --out_dir=out-arith-char
