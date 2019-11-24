# Working of Backpropogation algorithm

As we know neural network is a complex structure consisting of large number of weights and biases.To make accurate prediction these weights and biases need to have appropriate value and hence to adjust these weights and biases so that we get minimum cost function value we use **Backpropogation** algorithm .To get a better view about the working of these algorithm we will dive further into thetoic of Backpropogation algorithm.

## What is Backpropogation algorithm

Backpropagation is a popular method for training artificial neural networks, especially deep neural networks.
Backpropagation is needed to calculate the gradient, which we need to adapt the weights of the weight matrices. The weights of the neurons 
(ie nodes) of the neural network are adjusted by calculating the gradient of the loss function. For this purpose a gradient descent optimization algorithm is used. It is also called backward propagation of errors.

![030819_0937_BackPropaga1](https://user-images.githubusercontent.com/44902363/69477535-616b3100-0e0d-11ea-98b1-b44475390e95.png)

The above diagram show the basic neural network which consist of input layer with 3 neuron ,2 hidden layer and one outer layer with 2 neuron.The error is calculated from the last output layer and then that error is feed backward to pass it to other hidden layer.Through this we will find the error for each layer.
Backpropogation algorithm can be expalined by its bacis 4 equations. We will try to get the detailed overview of each of the equation and try to understand the working of each of these equation and how they are connected to each other.

## Equation of Baackpropgation algorithm.

To get the better understanding of the equation first lets us begin with the notation that we have used in our equation.
Let's begin with a notation which lets us refer to weights in the network in an unambiguous way. We'll use wljk to denote the weight for 
the connection from the kth neuron in the (l−1)th layer to the jth neuron in the lth layer. So, for example, the diagram below shows the 
weight on a connection from the fourth neuron in the second layer to the second neuron in the third layer of a network:

![Screenshot (18)](https://user-images.githubusercontent.com/44902363/69496665-86899d80-0efa-11ea-9f48-c95b6b2c3a51.png)

We use a similar notation for the network's biases and activations. Explicitly, we use blj for the bias of the jth neuron in the lth layer.
And we use alj for the activation of the jth neuron in the lth layer. The following diagram shows examples of these notations in use:

![Screenshot (20)](https://user-images.githubusercontent.com/44902363/69496723-00ba2200-0efb-11ea-9c83-cc42a96fde7a.png)

Backpropagation is about understanding how changing the weights and biases in a network changes the cost function. Ultimately, this
means computing the partial derivatives ∂C/∂wljk and ∂C/∂blj. But to compute those, we first introduce an intermediate quantity, δlj,
which we call the error in the jth neuron in the lth layer. Backpropagation will give us a procedure to compute the error δlj, and then
will relate δlj to ∂C/∂wljk and ∂C/∂blj.

Suupose by there is some demon at the jth neuron in layer l. As the input to the neuron comes in, that demon messes with the neuron's operation. It adds a little change Δzlj to the neuron's weighted input, so that instead of outputting σ(zlj), the neuron
instead outputs σ(zlj+Δzlj). This change propagates through later layers in the network, finally causing the overall cost to change by 
an amount ∂C∂zljΔzlj.we define the error δlj of neuron j in layer l by

![Screenshot (22)](https://user-images.githubusercontent.com/44902363/69496922-6c04f380-0efd-11ea-9980-87c761ea6363.png)

You might wonder why the demon is changing the weighted input zlj. Surely it'd be more natural to imagine the demon changing the output 
activation alj, with the result that we'd be using ∂C∂alj as our measure of error. In fact, if you do this things work out quite 
similarly to the discussion below. But it turns out to make the presentation of backpropagation a little more algebraically complicated.
So we'll stick with δlj=∂C∂zlj as our measure of error.

### **An equation for the error in the output layer, δL:**
The components of δL are given by



