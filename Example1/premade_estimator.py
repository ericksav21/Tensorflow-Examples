from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf

import iris_data

def main(argv):
	(train_x, train_y), (test_x, test_y) = iris_data.load_data()
	print(train_x)

if __name__ == '__main__':
	tf.logging.set_verbosity(tf.logging.INFO)
	tf.app.run(main)