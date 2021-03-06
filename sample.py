from __future__ import print_function
import tensorflow as tf

import word_lstm_wrapper

import argparse
import os
from six.moves import cPickle

from model import Model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save',
                       help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=200,
                       help='number of words to sample')
    parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')

    args = parser.parse_args()
    return args


def sample(args):
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, 'words_vocab.pkl'), 'rb') as f:
        words, vocab = cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            while True:
                input = raw_input('input: ')
                print(model.sample(sess, words, vocab, args.n, input, args.sample))

if __name__ == '__main__':
    args = vars(main())
    #sample(args)
    save_dir = args['save_dir']
    wr = word_lstm_wrapper.WordLevelLSTM(save_dir)
    while True:
        input = raw_input('input: ')
        answer = wr.sample(input=input)
        print(answer)