# word-rnn-tensorflow
[![Build Status](https://travis-ci.org/hunkim/word-rnn-tensorflow.svg?branch=master)](https://travis-ci.org/hunkim/word-rnn-tensorflow)

Multi-layer Recurrent Neural Networks (LSTM, RNN) for word-level language models in Python using TensorFlow.

Mostly reused code from https://github.com/sherjilozair/char-rnn-tensorflow which was inspired from Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

# Requirements
- [Tensorflow](http://www.tensorflow.org)

# Basic Usage

    cd /home/marcel/devel/word-rnn-tensorflow
    workon caffe
    python train.py --data_dir data/medosch/ --train_filename  input.txt --save_dir ./medosch --model lstm --save_every 100
    python sample.py --save_dir medosch --prime 'quantum'
