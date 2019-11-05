#importing mnist_loader
import mnist_loader
#importing network
import network

# calling the load_data_wrapper function from mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

#creating the net object while intializing the network class
net=network.Network([784,30,10])
#It consist of 784 nodes in input layer cause input is an image of pixel value 28*28
#It consist of 30 hidden layers
#Consist of 10 nodes in output num_layers

#calling the SGD function of Network class in network
net.SGD(training_data,30,10,3.0,test_data=test_data)
#epochs which is 30
#mini_batch_size is 10
#eta of learning rate is 3.0
