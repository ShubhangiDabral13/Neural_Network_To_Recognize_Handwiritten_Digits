# Working of Backpropogation algorithm

As we know neural network is a complex structure consisting of large number of weights and biases.To make accurate prediction these weights and biases need to have appropriate value and hence to adjust these weights and biases so that we get minimum cost function value we use **Backpropogation** algorithm .To get a better view about the working of these algorithm we will dive further into thetoic of Backpropogation algorithm.

## What is Backpropogation algorithm

Backpropagation is a popular method for training artificial neural networks, especially deep neural networks.
Backpropagation is needed to calculate the gradient, which we need to adapt the weights of the weight matrices. The weights of the neurons 
(ie nodes) of the neural network are adjusted by calculating the gradient of the loss function. For this purpose a gradient descent optimization algorithm is used. It is also called backward propagation of errors.

![030819_0937_BackPropaga1](https://user-images.githubusercontent.com/44902363/69477535-616b3100-0e0d-11ea-98b1-b44475390e95.png)

The above diagram show the basic neural network which consist of input layer with 3 neuron ,2 hidden layer and one outer layer with 2 neuron.The error is calculated from the last output layer and then that error is feed backward to pass it to other hidden layer.Through this we will find the error for each layer
