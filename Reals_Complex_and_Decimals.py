# Hello everybody, and welcome to yet another session on Python Programming.
# In the last one we had a quick look at the Boolean data type, and how we can
# do stuff with Boolean variables. We looked into declaring Boolean variables,
# assigning values, the different operations that can be performed on these
# variables, and how these variables react to Boolean specific and non-specific
# operators being used on them.

# We also had a look at how Boolean values interact with Integer values, Boolean
# being a sub-type of Integers, and how Booleans work in case of pure logical
# operations ('not', 'or', 'and').

# In this session, we're going to start by exploring another sub type of the Numbers data type
# in Python: Real Numbers, or simple Reals...

# Now, Real Numbers are also called Floating Point Numbers. Basically, for a
# layman's definition, Floating Point Numbers consist of decimal points, with
# one or more digits after the decimal point.

# For a more technical definition, I'm going to have you take a look at the following
# terms, online:

# 1) IEEE 754 double precision binary floating-point format
# 2) Single Precision numbers - These take up 32 bits of memory for each declaration
# 3) Double Precision numbers - These take up 64 bits of memory for each declaration

# Python makes use of double precision when it comes to real numbers, which means
# that each floating-point variable is allocated 64 bits of memory. Which simply means
# we can store 2 to the power 64 numbers with that amount of bits...

floatingPointLimit = 2 ** 64;
print('Largest Floating-Point Number: ' + str(floatingPointLimit) + '\n');

# Well, that's a whopping 18,446,744,073,709,551,616 numbers with that amount of bits.

# So, what's precision about? And why are talking about it?
# Well, precision is basically the number of significant digits required to represent a
# number. For example, 2.54432581 is better than simple 2.54. You see, the former provides
# more precision than the latter. 2.54432581 is closer to providing accuracy than simply 2.54.
# This is really important from a scientific standpoint, and since Python was built
# keeping the scientific community in mind, it only makes sense that Real Numbers would
# have better precision.

# Alrighty then! Let's get to exploring Real Numbers...

pi = 3.14159265;
radius = 6;
print('Radius of the Circle: ' + str(radius));
area = pi * (radius ** 2);
print('Area of the Circle: ' + str(area) + '\n');

# Basically, you can do all operations on Real Numbers what you did on Integers.
# Let's have a look at a few more:

a = 5;
b = 16;
print('A = ' + str(a));
print('B = ' + str(b));
c = a / b;
print('C = A / B = ' + str(c));
d = b * c;
print('D = B x C = ' + str(d) + '\n');

# And just like how Integers can be used along with Boolean values, you'll find there
# is no exception for Reals either...
e = True;
f = 3.14159265;
g = e + f;
print('E = True + 3.14159265 = ' + str(g) + '\n');     # The output of 'E = True + 3.14159265 = ' is 4.14159265.

# Before we end our exploration of Reals, I'd like to bring to light something called
# 'Approximation Issues'. To explain what approximation issues are, let's take a 
# quick look at some system information on Floating-Point Numbers:

import sys;     # This statement imports system parameters and variables from the 'sys' module in Python. 
print(str(sys.float_info) + '\n');      # Here, we print information related to floating-point numbers
                                        # and how they will behave in your system.
# Take a look at the 'max', and 'epsilon' values for floating-point numbers. You'll see
# that they are a lot larger than what can be accommodated by Python. We've already seen
# the limit for double precision numbers earlier. You'll see that there isn't enough
# space available for Reals can be approximated to the closest representation of
# these values.

# But does this issue only limit itself to smaller numbers? Let's have a look...
h = (6 * 0.1) - 0.6
print('(6 x 0.1) - 0.6 = ' + str(h) + '\n');   # On printing this statement, we get: (6 x 0.1) - 0.6 = 2.560000000000000053290705182007513940334320068359375
                                            
# What happened here? Wasn't the output expected to be a plain zero?
# So as we just saw, approximation issues also plague smaller double-precision numbers.
# This can be a serious problem when dealing with financial, or scientific data that
# might need to be approximated.

# Is there a work-around for this? Yes. Python provides us with the Decimal data type,
# another sub type of the Numbers data type. We're going to look at it next...

# Let's look at the Fraction and Decimal Type. Fractions are variables that hold
# a rational numerator and denimonator in their lowest forms. Let's look a few examples:
from fractions import Fraction;

numerator1 = 15;    # Have a look at this example here. 
denominator1 = 9;   # The lowest form of the fraction 15/9 = 5/3, and that is exactly what we get on printing the output.
fraction1 = Fraction(numerator1, denominator1);
print('Fraction 1 = 15 / 9 = ' + str(fraction1) + '\n');

numerator2 = 15;    # Here's a second example on how fractions work.
denominator2 = 6;
fraction2 = Fraction(numerator2, denominator2);
print('Fraction 2 = 15 / 6 = ' + str(fraction2) + '\n');

# Fractions can also be operated upon using regular Integer operands.
fraction3 = Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2);    # Here's an example of Fraction addition.
print('Fraction 3 = (15 / 9) + (15 / 6) = ' + str(fraction3) + '\n');

# Fraction Mulitiplication:
fraction4 = Fraction(3, 4) + Fraction(8, 19);
print('Fraction 4 = (3 / 4) + (8 / 19) = ' + str(fraction4) + '\n');

# Fractions also work along with Boolean values:
fraction5 = Fraction(3, 4) + True;
print('Fraction 5 = (3 / 4) + True = ' + str(fraction5) + '\n');

# Heck, they also work well with Reals, but only that the final output is in the form
# of a Real number, as Reals are given precedence over Fractions:
fraction6 = Fraction(8, 20) + 3.14159265;
print('Fraction 6 = (8 / 20) + 3.14159265 = ' + str(fraction6) + '\n');

# Fractions may be very useful in some applications, but you'll not find them being
# used often. This is simply because it is better to use the Decimals data type if
# you're looking for values that provide you with precision in scientific and financial
# calculations.

# Let's have a quick look at Decimals.
from decimal import Decimal as D;
decimal1 = D(2.57);
print('Decimal 1 = ' + str(decimal1) + '\n');   # This example is a great example demonstrating how Decimal values
                                                # also suffer from approximation issues when it is constructed from a
# foating-point number. What was initial constucted as '2.57' is printed as '2.569999999999999840127884453977458178997039794921875'.

# In order to avoid this approximation issue, it is best to contruct a Decimal variable
# using String. Consider the next example:
decimal2 = D('2.57');
print('Decimal 2 = ' + str(decimal2) + '\n');   # This time, the printed value is '2.57'. No approximation
                                                # issues to worry about. Using this, you can run successful operations
# on Decimal values.

# Decimal Addition:
decimal3 = D('3.14') + D('2.24');
print('Decimal 3 = 3.14 + 2.24 = ' + str(decimal3) + '\n');

# Decimal Division:
decimal4 = D('22') / D('7');
print('Decimal 4 = 22 / 7 = ' + str(decimal4) + '\n');

# Decimal addition with Booleans:
decimal5 = True + D('4.7639');
print('Decimal 5 = True + 4.7639 = ' + str(decimal5) + '\n');

# Decimal subtraction wih Booleans:
decimal6 = D('7.23462') - True;
print('Decimal 6 = 7.23462 - True = ' + str(decimal6) + '\n');

# Always use Decimals constructed using Strings when you need to work with precision.s

# Finally, let's have a quick look at Complex Numbers, another sub type of Numbers.
# If you're an engineer, you'll surely know what Complex Numbers are. Complex Numbers,
# unlike other numbers, consist of two parts: The Real part, and the 'Imaginary' part.
# Yeah, imaginary. This is how a complex number looks: 3 + 8j; sometimes also written
# as 3 + j8.

# Let's look at simple examples. Here's one of Complex addition:
a = 3 + 8j;
b = 11 + 4j;
c = a + b;
print('A: ' + str(a));
print('B: ' + str(b));
print('C = A + B = ' + str(c) + '\n');

# Complex mulitiplication:
d = a * b;
print('D = A x B = ' + str(d) + '\n');
d_verified = (3 * 11) + (3 * 4j) + (11 * 8j) + (4j * 8j);
print('D verified = (3 * 11) + (3 * 4j) + (11 * 8j) + (4j * 8j) = ' + str(d_verified) + '\n');

# Complex Numbers can also be split into their real and imaginary parts for processing:
A_real = a.real;
print('Real part of A = ' + str(A_real));
A_imaginary = a.imag * (0 + 1j);
print('Imaginary part of A = ' + str(A_imaginary));
print('A = ' + str(A_real) + ' + ' + str(A_imaginary) + '\n')
