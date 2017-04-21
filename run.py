from data_helper import Data
import neural_network

data = Data()
data.load_data()
train = data.wrap_train_data()
validation = data.wrap_validation_data()

net = neural_network.NeuralNetwork([784, 100, 62])
net.stoch_grad_desc(train, 30, 10, 3, test_data=validation)
