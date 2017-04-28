import numpy as np
import os
from data_helper import Data
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from scipy import misc

def save_model():
    model.save('neural_net.h5')


data = Data()
data.load_data()

training_data = data.training_input
training_labels = data.training_labels
test_data = data.test_input
test_labels = data.test_labels

model = Sequential()

if os.path.isfile('neural_net.h5'):
	load_choice = raw_input('Do you want to load the previously saved neural network?[Y/n]')
	if load_choice.lower() == 'y':
	    model = load_model('neural_net.h5')
	else:
	    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

	    model.add(Dense(30, activation='sigmoid', input_shape=(784,)))
	    model.add(Dense(62, activation='sigmoid'))
	    model.compile(loss='mean_squared_error', optimizer=sgd)

	    print('Starting to train...')

	    history = model.fit(training_data, training_labels, epochs=20, batch_size=10)
	    score = model.evaluate(test_data, test_labels, batch_size=32)

	    print('\nTest accuracy: ', score)

	    save_choice = raw_input('Do you want to save this model? [Y/n]')
	    if save_choice.lower() == 'y':
	        save_model()

image = misc.imread('12.png', mode='L').reshape(1,784)
classes = model.predict(image)
print(np.argmax(classes))
