import scipy.io
import re
import glob
import numpy as np
from scipy import misc
from PIL import Image

root_directory = '/Users/vihanggodbole/Developer/restaurant-menu-ocr/training_data/'

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


class Data(object):

    def __init__(self):
        self.training_input = None
        self.training_labels = None
        self.validation_input = None
        self.validation_labels = None
        self.test_inputs = None
        self.test_labels = None

    def load_data(self):

        # get paths of images
        paths = sorted(glob.glob(root_directory + '**/*.png'),
                       key=numericalSort)
        r_state = np.random.get_state()
        np.random.shuffle(paths)    # shuffle paths
        # get images
        images = []
        for path in paths:
            # get image in grayscale. shape(28,28)
            grayscale_image = misc.imread(path, mode='L')
            # shape is (784, 1). NOT (784, )
            images.append(grayscale_image.reshape(784, 1))

        # get classification labels
        mat = scipy.io.loadmat('lists_var_size.mat')
        training_labels = mat['list'][0, 0][
            'ALLlabels']    # shape = (62992, 1)
        # shuffle training data

        np.random.set_state(r_state)
        # shuffle the vector in the same way as images
        np.random.shuffle(training_labels)

        # first 50000 images as trainig data
        self.training_input = images[:50000]
        self.validation_input = images[50000:]

        temp = []
        for i in range(62292):
            # since training_lables[i] returns an ndarray. of 1x1
            j = training_labels[i][0] - 1
            # eg: if the sample is 'z' then training_labels[i] = 62. Thus,
            # temp[0] = [0,0...0,1]
            t = np.zeros((62, 1), dtype=np.int)
            t[j] = 1
            temp.append(t)

        self.training_labels = temp[:50000]
        self.validation_labels = temp[50000:]

    def wrap_train_data(self):
        return [(x, y) for x, y in zip(self.training_input, self.training_labels)]

    def wrap_validation_data(self):
        return [(x, y) for x, y in zip(self.validation_input, self.validation_labels)]
