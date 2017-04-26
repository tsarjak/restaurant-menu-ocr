from data_helper import Data
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

data = Data()
data.load_data()

training_data = data.training_input
training_labels = data.training_labels
test_data = data.test_input
test_labels = data.test_labels

model = Sequential()

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.add(Dense(30, activation='sigmoid', input_shape=(784,)))
model.add(Dense(62, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer=sgd)

print('Starting to train...')

history = model.fit(training_data, training_labels, epochs=20, batch_size=10)
score = model.evaluate(test_data, test_labels, batch_size=32)

print('Test accuracy: ', score)
