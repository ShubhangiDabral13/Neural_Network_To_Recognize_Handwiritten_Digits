
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
![1_UpqLxhXMqmN6ztphYNSFLA](https://user-images.githubusercontent.com/44902363/69443626-d179a880-0d74-11ea-841e-424d44339c7b.png)
where a is the neuron's output when the training input x=1 is used, and y=0 is the corresponding desired output. To write this more 
explicitly in terms of the weight and bias, recall that a=σ(z), where z=wx+b. Using the chain rule to differentiate with respect to the weight and bias we get
<!---enter quation with partial derivative with repect to w and b-->
<!---nter sigmoid graph-->
![sigmoid_and_derivative_plot](https://user-images.githubusercontent.com/44902363/69445295-089d8900-0d78-11ea-86e3-5f5bcb3a301a.jpg)
We can see from this graph that when the neuron's output is close to 1, the curve gets very flat, and so σ′(z) gets very small. 
hence ∂C/∂w and ∂C/∂b get very small. This is the origin of the learning slowdown.So to overcome this we will use cross-Entropy cost function.
## What is Cross-Entropy ?
Cross-Entropy is similar to the cost function cause it has property similar to cross function.
<!---enter the equation for the Cross-Entropy -->
![binary_crossentropy](https://user-images.githubusercontent.com/44902363/69445504-747ff180-0d78-11ea-9c77-653c832147de.png)

* 1:-First, it's non-negative, that is, C>0. To see this, notice the above equation that all the individual terms in the sum  are
negative, since both logarithms are of numbers in the range 0 to 1; and there is a minus sign out the front of the sum.

* 2:-Second, if the neuron's actual output is close to the desired output for all training inputs, x, then the cross-entropy will be close to Zero.

As we know that how in quadaratic cost function suffer from slow learning rate.Hence to overcome this we will use Cross-Entropy.
The ∂C/∂w and ∂C/∂b for Cross-Entropy is given below
<!---equation for the cross entropy-->
![maxresdefault](https://user-images.githubusercontent.com/44902363/69445589-a4c79000-0d78-11ea-8953-e6f9d76ad232.jpg)
in the above equation we can se that there is no σ′(z) term thus it does not suffer from the slow  learning rate. We know that 
w=w- ∂C/∂w hence for cross entropy we have (a-y) for ∂C/∂w hence *w=w-(a-y)*. therefore when there is lot of difference between predicted value and actual value then w will decrease with large amount. 
<!---cross-entropy graph for epoochs-->
This is how slow learning rate is overcome by the cross-entropy cross function.
Neural Network turn out to be  boon in todays era but...there are some things which the Neural Network faces a lot .One of them which is
most commun is **Overfitting** .below is a brife intro about what is overfitting and how we can remove it.
## Overfitting
To make the picture clear about the overfitting first we will analyis the probllem through graph
<!---enter the graph of cost on the training data vs epochs-->
![overfitting1](https://user-images.githubusercontent.com/44902363/69445922-5961b180-0d79-11ea-9e99-4d32e06b8f4d.png)
here we can see that the model is improving at every epochs cause the the cost function is decreasing .
<!---enter the graph for the test data accuracy vs epochs-->
![c03f5837ac919e7152bdb84b2891d5d0e2674dbf](https://user-images.githubusercontent.com/44902363/69446056-9a59c600-0d79-11ea-937d-d1188f4c6039.png)
In the above graph we can see that the accuracy increased but around 280 epochs it remained constant hence this show that there is no
futher improvement but for training data the cost went on decreasing this is all because of Overfitting of the model.
Overfitting is a common problem that all Neural Networks run into. This occurs when the model is fit too well to the training set but
does not perform as well on the test set. For Deep Learning, the issue of overfitting since the model is able to adapt freely to large
amount of complex data. 
We can deccrease the overfitting by various way.

* 1:- If we provide large amount of trianing data.

* 2:- If we decrease the hper parameter of the model.

But both of them have the their own drawback.To collect large amount of data is not that easily available to us and also decreasing the 
hyperparamter will not make the model that much complex thus decreasing the efficiency of the output.
Therefore we use regularization to overcome fitting .
<!---enter the equation for the regualrization-->
![reg_formulas](https://user-images.githubusercontent.com/44902363/69446589-bdd14080-0d7a-11ea-8c82-aec63a7e9ca0.png)
The first term is just the usual expression for the cross-entropy. But we've added a second term, namely the sum of the squares of all 
the weights in the network. This is scaled by a factor λ/2n, where λ>0 is known as the regularization parameter, and n is, as usual, the
size of our training set. It's also worth noting that the regularization term doesn't include the biases. 
Intuitively, the effect of regularization is to make it so the network prefers to learn small weights, all other things being equal. 
Large weights will only be allowed if they considerably improve the first part of the cost function. Put another way, regularization can 
be viewed as a way of compromising between finding small weights and minimizing the original cost function. The relative importance of 
the two elements of the compromise depends on the value of λ: when λ is small we prefer to minimize the original cost function, but when λ is large we prefer small weights.
<!---equation for the partical derivative of regualization-->
as w=w- ∂C/∂w so the equation will be
<!---insert the equation-->
Thus from the above equation we can see that if we increase λ then the weight will decrease hence making hyperparamter closer to the optimal thus overcoming the overfitting problem.
This is how regualrization deccrase the overfitting problem . The above regularization was of L1 .There are different type of regularization.

* L2 Reguarization:-

<!---equation for L2 regularizaiton-->
![reg_formulas](https://user-images.githubusercontent.com/44902363/69446589-bdd14080-0d7a-11ea-8c82-aec63a7e9ca0.png)
 In L1 regularization, the weights shrink by a constant amount toward 0. In L2 regularization, the weights shrink by an amount which is
 proportional to w. And so when a particular weight has a large magnitude, |w|, L1 regularization shrinks the weight much less than L2
 regularization does. By contrast, when |w| is small, L1 regularization shrinks the weight much more than L2 regularization. The net
 result is that L1 regularization tends to concentrate the weight of the network in a relatively small number of high-importance 
 connections, while the other weights are driven toward zero.

* Dropout :-

Simply put, dropout refers to ignoring units (i.e. neurons) during the training phase of certain set of neurons which is chosen at
random. By “ignoring”, mean these units are not considered during a particular forward or backward pass.Hence like this way we get a
large amount of different models.


