# Using Network nets to recognize handwritten digits.
|---|
Neural network is a part of deep learning and to implement the *Digit Recognition* we will use *Deep Learning*.Let us start with what is 
deep learning and then dive further into the topic to explore more about it.
## What is Deep Learning.
Deep learning is an artificial intelligence function that imitates the workings of the human brain in processing data and creating patterns
for use in decision making.
Deep learning is a subset of machine learning in artificial intelligence (AI) that has networks capable of learning unsupervised from data
that is unstructured or unlabeled. Also known as deep neural learning or deep neural network.
**_Deep_** parts refers of creating deep neural network. This refers to neural network with large amount of layers with the addition *weights*
and *biases*.
### Key points about deep learning:-
..*Deep Learning refers to Deep Neural Network(DNN).
..*DNN find association between a set of inputs and outputs.
..*Backpropogation is something that is used to update the parameters(weights and biases) of neural networks.
The above explanation about DNN might be foggy to you if you are new to this topic but don't worry i will make things crytsal clear to you.
The next question which might pop in your brain are What is neural network ,what are those layer and how actually neural network in Digit
Recognition.
## What is Neural Network.
<!---pic of neural network-->
The above fig is of Neural Network. It help to find the association between a set of inputs and outputs.
..* All the above layer are composed of nodes.\
..*Input layer takes in the numerical representation of data.
..*Output layer output the predictions.
--*While hidden layers are correlated with most of the computation.
<!--- pic of a nodes with weight and biases-->
The parameter weights and Bias are essential to the actual *Learning* process of deep learning algorithm.
After the neural network passes its input all theto its output, the network evaluates how good its perdiction was through something called 
**Mean Squared Error**:-
<!---The pic of the cost function-->
## Working of neural network to Recognize hand written digits.
Neural network to recoginze hand written digit in a different way.The idea is to take number of handwritten digits known as training examples.
Neural Network uses the example to automatically infer rules for recognizing hand written digits.By increasing the number of training examples
the network can learn more about handwriting and also improve the accuracy.
<!---image of perceptron-->
### Perceptrons:-
it takes several binary inputs x1,x2,.... and produce one output.weights are the real number expressing the importance of the respective input
to the output.
<!---image of those output and threshold-->
We change summation of wj*xj threshold which is cumbersome in two things:-
..1.By moving to otherside of inequality and to replace it by what's known as perceptron'sbias =-Threshold.
..2.write summation ofwjxj as dot product of w.x where w and x are vectors whose components are weight and input respectively.
<!---image of output with bias-->
Bias is a measure of how esay it is to get perceptron to output a 1.Perceptron with really big bias ,its extremely easy for perceptron to 
output a 1.
### What Sigmoid Neurons are used.
suupose the input to the network might be the pixel data from a scanned, handwritten image of digit and we would like the network to learn
weight and biases so that output from the network correctly classify the digit.For that we want that any small change in weights and biases
an cause a small corresponding change in the output from the network.But this does not work.Infact a small change in weights or biases 
of any single perceptron somewhat completely flip the output say from 1 to 0 or vise versa.
Therefore we can overcome this by using Sigmoid Neurons.
#### How Sigmod Neurons works.
They are similar to neuron but modified so that small changes in their weights and biases can cause only small change in their output.
<!---image of equation of sigmoid neuron-->
Where Z=wx+b   where w=weights and b=biases.
To understand the similarity to the perceptron model,suppose z=wx+b is large positive number .Then e^(-z)= 0 and sigmoid function of z =1.
In other words ,when z=wx+b is large and positive the Output for sigmoid neuron is apporximately 1, just as it would have been for the percetron.
Similarly for very negative it will give 1.The behavior of neuron also closely approximate a perceptron.
<!---graph of sigmoid and step  function-->
if segmoid had been a step function ,then sigmoid neuron would be a perceptron since the output would be 1 or 0 depending on whether wx+b
was + or -.But Sigmoid function has a smooth curve .the smoothness means that small changes in weight and bias will produce small change 
in the output from the neuron.
### Architecture of neural network:-
perceptron which have multiple layers hidden layer are called multilayer perceptron.The design of the input and output layers in a 
network is often straightforward. For example, suppose we're trying to determine whether a handwritten image depicts a "9" or not. A 
natural way to design the network is to encode the intensities of the image pixels into the input neurons. If the image is a 64 by 64 
greyscale image, then we'd have 4,096=64×64 input neurons, with the intensities scaled appropriately between 0 and 1. The output layer will
contain just a single neuron, with output values of less than 0.5 indicating "input image is not a 9", and values greater than 0.5 indicating
"input image is a 9 ".
#### A simple network to classify handwritten digits.
We split the problem of recognizing handwritten digit into 2 sub-problem
..1)We would like to break the image containing many digit into a sequence of seperating images,each containing single digit.
..2)second problem to classifying individual digits.
<!---neuron network for digit recognition-->
In output layer we have total 10 neuron if 0th neuron fire means the digit was zero and so on.
### Gradient Descent.
This is an iterative optimization algorithm for finding the minimum of a function. The algorithm takes steps proportional to the negative
gradient of the function at the current point. In deep learning neural networks are trained by defining a loss function and optimizing the
parameters of the network to obtain the minimum of the function. the optimization is dne using the gradient descent algorithm which operates
in these two steps:
..1.Compute the slope (gradient) that is first order derivative of the function at the current point
..1.Move in the opposite direction of the slope increase from the current point by the computed amount
<!---image of equation of gradient decent-->
#### Stochastic Gradient Descent
In this method one training sample (example) is passed through the neural network at a time and the parameters (weights) of each layer are
updated with the computed gradient. So, at a time a single training sample is passed through the network and its corresponding loss is computed
The parameters of all the layers of the network are updated after every training sample. For example, if the training set contains 100 samples
then the parameters are updated 100 times that is one time after every individual example is passed through the network. Following is the
gradient descent equation and for stochastic gradient descent it is iterated over ’n’ times for ’n’ training samples in the training set.
<!---Image of the equation for SGD-->
#### Batch Gradient Descent
The concept of carrying out gradient descent is the same as stochastic gradient descent. The difference is that instead of updating the
parameters of the network after computing the loss of every training sample in the training set, the parameters are updated once that is
after all the training examples have been passed through the network. For example, if the training dataset contains 100 training examples
then the parameters of the neural network are updated once.
#### Mini Batch Gradient Descent
This is a mixture of both stochastic and batch gradient descent. The training set is divided into multiple groups called batches. 
Each batch has a number of training samples in it. At a time a single batch is passed through the network which computes the loss of every 
sample in the batch and uses their average to update the parameters of the neural network. For example, say the training set has 100 training
examples which is divided into 5 batches with each batch containing 20 training examples. This means that the equation in figure2 will be
iterated over 5 times (number of batches).


