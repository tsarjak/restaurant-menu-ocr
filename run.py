from data_helper import Data
import neural_network
import network2

data = Data()
data.load_data()
train = data.wrap_train_data()
validation = data.wrap_validation_data()

net2 = network2.Network([784, 200, 62], cost=network2.CrossEntropyCost)
net2.SGD(train, 400, 10, 0.05, lmbda=3.0, evaluation_data=validation,
         monitor_evaluation_accuracy=True,
         monitor_evaluation_cost=False,
         monitor_training_accuracy=True,
         monitor_training_cost=False)
# net = neural_network.NeuralNetwork([784, 20, 62])
# net.stoch_grad_desc(train, 300, 10, 1, test_data=validation)
