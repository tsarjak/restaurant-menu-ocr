import numpy as np
import os
from data_helper import Data
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout, Flatten, Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from scipy import misc
from PIL import Image

def save_model():
    model.save('neural_net.h5')


data = Data()
data.load_data()

training_data = data.training_input
training_labels = data.training_labels
test_data = data.test_input
test_labels = data.test_labels

# ------- TEST -------
training_data = training_data.reshape(training_data.shape[0], 1, 128, 128)
test_data = test_data.reshape(test_data.shape[0], 1, 128, 128)

training_data = training_data.astype('float32')
test_data = test_data.astype('float32')

training_data /= 255
test_data /=255

model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1,128,128)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(62, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(training_data, training_labels, epochs=10, batch_size=10)
score = model.evaluate(test_data, test_labels, verbose=0)
model.save('conv_net.h5')
print('saved')
print(model.output_shape)
print(training_data.shape)
print(score)
image = misc.imread('31-1.png', mode='L')
image = image.reshape(1, 1, 128, 128)
classes = model.predict(image)
print(np.argmax(classes))

'''
if os.path.isfile('neural_net.h5'):
    load_choice = input(
        'Do you want to load the previously saved neural network?[Y/n]')
    if load_choice == 'y' or load_choice == 'Y':
        model = load_model('neural_net.h5')
    else:
        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

        model.add(Dense(30, activation='sigmoid', input_dim=16384))
        model.add(Dense(62, activation='sigmoid'))
        model.compile(loss='mean_squared_error', optimizer=sgd)

        print('Starting to train...')

        history = model.fit(training_data, training_labels,
                            epochs=10, batch_size=10)
        score = model.evaluate(test_data, test_labels, batch_size=32)

        print('\nTest accuracy: {}'.format(1-score))

        save_choice = input('Do you want to save this model? [Y/n]')
        if save_choice == 'y' or save_choice == 'Y':
            model.save('neural_net.h5')

# image = misc.imread('31-1.png', mode='L').reshape(1, 16384)
# im = Image.open('31-1.png')
# image = np.array(im)#.reshape(1, 16384)
# im.show()
# print(image.shape)
classes = model.predict(image)
print(np.argmax(classes))'''
