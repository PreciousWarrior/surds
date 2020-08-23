# surds
Simplifies surds, or expands simplified ones to their full form

to_simple_form function in an instance of the surd simplifier class takes in an a positive integer. This is the unsimplified surd (for example, the square root of 50),
and will output a tuple that has the surd multiplier in the first value, and the surd in the second. For example, if we input 50, the function will return
a tuple (5, 2) or 5√2, which is the simplified form.

The to_full_form (outside of the surd simplifier class), takes in two integers as input (the surd multiplier and the surd), for example 5√3, and returns the full
form as an integer,75 or √75 mathematically.

In the constructor of the surdsimplifier class, the class reads a file named "perfects.txt" to get the first 100,000 square numbers to be able to simplify surds.

PS-:
I am new to GitHub and this is my first repository, please inform me if I did something wrong, or there is something I need to do.
