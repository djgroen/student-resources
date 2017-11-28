
### Q: Can a unit test have multiple assertions, or should it always have only one?

### A: It is a matter of taste, but it is certainly possible to do multiple assertions. 
However, make sure that:

A) the user is clearly informed when a test fails (and assume there will be other developers than you).

B) that the message documenting a test failure is very easy to implement, to prevent unit tests from being difficult to write.

One way to address B could be to write your own print test result function. This could take as an argument the output value of the test function (True or False), as well as a designated name for the test. Furthermore, you want the function to have a very short name, as you will write it many times.

So an example function signature in Python could be:
def pr_unittest(test_name, test_outcome_bool):

Another advantage of having a custom print function is that you can change the verbosity (level of output) in your tests simply by changing the behavior of that one function.

For example, you could have it only print if test_outcome_bool is False, hence not crowding the screen with test results that were correct.
"""
