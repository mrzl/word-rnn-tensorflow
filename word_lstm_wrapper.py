import tensorflow as tf

import os
from six.moves import cPickle

from model import Model


class WordLevelLSTM(object):
    def __init__(self, load_dir, varscope):
        self.load_dir = load_dir
        self.varscope = varscope
        self.load_dir = load_dir
        self.name = None

    def sample(self, input, sample=1, output_length=200):
        print('Loading from ' + self.load_dir)
        with open(os.path.join(self.load_dir, 'config.pkl'), 'rb') as f:
            self.saved_args = cPickle.load(f)
        with open(os.path.join(self.load_dir, 'words_vocab.pkl'), 'rb') as f:
            self.words, self.vocab = cPickle.load(f)
        tf.reset_default_graph()
        model = Model(self.saved_args, infer=True, varscope=self.varscope)
        vars = [k for k in tf.all_variables() if k.name.startswith(self.varscope)]
        with tf.Session() as sess:
            saver = tf.train.Saver(vars)
            ckpt = tf.train.get_checkpoint_state(self.load_dir)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
            answer = model.sample(sess, self.words, self.vocab, output_length, input, sample)
            sess.close()
            return answer

    def sample2(self, input, sample=1, output_length=200):
        print('Loading from ' + self.load_dir)
        with open(os.path.join(self.load_dir, 'config.pkl'), 'rb') as f:
            self.saved_args = cPickle.load(f)
        with open(os.path.join(self.load_dir, 'words_vocab.pkl'), 'rb') as f:
            self.words, self.vocab = cPickle.load(f)
        tf.reset_default_graph()
        model = Model(self.saved_args, infer=True, varscope=self.varscope)
        vars = [k for k in tf.all_variables() if k.name.startswith(self.varscope)]
        with tf.Session() as sess:
            saver = tf.train.Saver(vars)
            ckpt = tf.train.get_checkpoint_state(self.load_dir)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
            answer = model.sample2(sess, self.words, self.vocab, output_length, input, sample)
            sess.close()
            return answer