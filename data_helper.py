import scipy.io
import re
import glob
import numpy as np
from scipy import misc

root_directory = '/Users/vihanggodbole/Developer/restaurant-menu-ocr/English/Fnt/'

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


class Data(object):

    def __init__(self):
        self.training_input = np.zeros((50000, 16384))
        self.training_labels = np.zeros((50000, 62))
        self.test_input = np.zeros((12992, 16384))
        self.test_labels = np.zeros((12992, 62))

    def load_data(self):

        # get paths of images
        paths = sorted(glob.glob(root_directory + '**/*.png'),
                       key=numericalSort)
        r_state = np.random.get_state()
        np.random.shuffle(paths)    # shuffle paths

        # get images
        for index, path in enumerate(paths):
            # get image in grayscale. shape(28,28) and reshape it
            grayscale_image = misc.imread(path, mode='L').reshape(1, 16384)
            if index < 50000:
                self.training_input[index] = grayscale_image
            else:
                self.test_input[index - 50000] = grayscale_image

        # get classification labels
        mat = scipy.io.loadmat('lists_var_size.mat')
        training_labels = mat['list'][0, 0][
            'ALLlabels']    # shape = (62992, 1)

        # shuffle training data
        np.random.set_state(r_state)
        # shuffle the vector in the same way as images
        np.random.shuffle(training_labels)

        for i in range(len(paths)):
            # since training_lables[i] returns an ndarray. of 1x1
            j = training_labels[i][0] - 1
            # eg: if the sample is 'z' then training_labels[i] = 62. Thus,
            # temp[0] = [0,0...0,1]
            t = np.zeros((1, 62), dtype=np.int)
            t[0][j] = 1
            if i < 50000:
                self.training_labels[i] = t
            else:
                self.test_labels[i - 50000] = t
