
# Improving The Way Neural Networks Work
In this we will get a detailed view about what is crosss-entropy cost function and also what is overfitting and how we can improve it.
So let us walk down the road to understand and absorve all the detail regarding the cross-entropy cost function.
## Why we use cross-Entropy ?
lets take a perceptron which give 1 when 0 is given and 0 when 1 is given.Consider 2 cases
* case1:- pick the initial weight to be 0.6 and the initial bias to be 0.9.The initial output from the neuron is 0.82, so quite a bit of
learning will be needed before our neuron gets near the desired output, 0.0. The learning rate is η=0.15.But after this when we train our
model, the neuron rapidly learns a weight and bias that drives down the cost, and gives an output from the neuron of about 0.09. That's
not quite the desired output, 0.0, but it is pretty good.

* case2:-Suppose, however, that we instead choose both the starting weight and the starting bias to be 2.0.The initial output from the
neuron is 0.98, so quite a bit of learning will be needed before our neuron gets near the desired output, 0.0. Although this example uses 
the same learning rate (η=0.15), but learning starts out much more slowly. Indeed, for the first 150 or so learning epochs, the weights
and biases don't change much at all. Then the learning kicks in and, much as in our first example, the neuron's output rapidly moves 
closer to 0.0. 

conculsion:-**But we've just seen that our artificial neuron has a lot of difficulty learning when it's badly wrong - far more difficulty
than when it's just a little wrong.**

To understand the origin of the problem, consider that our neuron learns by changing the weight and bias at a rate determined by the 
partial derivatives of the cost function, ∂C/∂w and ∂C/∂b. So saying "learning is slow" is really the same as saying that those partial 
derivatives are small. The challenge is to understand why they are small. To understand that, let's compute the partial derivatives. 
<!---enter the cost function equation-->
where a is the neuron's output when the training input x=1 is used, and y=0 is the corresponding desired output. To write this more 
explicitly in terms of the weight and bias, recall that a=σ(z), where z=wx+b. Using the chain rule to differentiate with respect to the weight and bias we get
<!---enter quation with partial derivative with repect to w and b-->
<!---nter sigmoid graph-->
We can see from this graph that when the neuron's output is close to 1, the curve gets very flat, and so σ′(z) gets very small. 
hence ∂C/∂w and ∂C/∂b get very small. This is the origin of the learning slowdown.So to overcome this we will use cross-Entropy cost function.
## What is Cross-Entropy ?
