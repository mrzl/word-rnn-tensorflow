#!/bin/bash

python word_level_rnn/train.py --data_dir data/ --train_filename /mnt/drive1/data/eco/pdf_to_text_postprocessed/wark_mckenzie-a_hacker_manifesto.txt --save_dir ./word_level_rnn/saved/wark_mckenzie-a_hacker_manifesto --model lstm --save_every 100