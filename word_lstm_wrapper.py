import tensorflow as tf

import os
from six.moves import cPickle

from model import Model


class WordLevelLSTM(object):
    def __init__(self, load_dir):
        with open(os.path.join(load_dir, 'config.pkl'), 'rb') as f:
            saved_args = cPickle.load(f)
        with open(os.path.join(load_dir, 'words_vocab.pkl'), 'rb') as f:
            self.words, self.vocab = cPickle.load(f)
        self.model = Model(saved_args, True)
        with tf.Session() as self.sess:
            tf.initialize_all_variables().run()
            saver = tf.train.Saver(tf.all_variables())
            ckpt = tf.train.get_checkpoint_state(load_dir)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(self.sess, ckpt.model_checkpoint_path)

    def sample(self, input, sample=1, output_length=200):
        return self.model.sample(self.sess, self.words, self.vocab, output_length, input, sample)