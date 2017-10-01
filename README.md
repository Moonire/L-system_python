# L-system_python
L-system implementation for python 3.x

Non Stochastic Context free L-system implementation for python 3.x
Conformaly to the description given in 'The Algorithmic Beauty of Plants' by Lindenmayer (algorithmicbotany.org/papers/abop/abop.pdf) i.e :

the angles are in degrees and grow clockwise
supports edge and node rewriting
supports branching

all lower cases : forward line
all upper cases : ignored in the drawing prosses (as well as all other special characters or numbers)
_               : forward without drawing
[ , ]           : respectively saving and popping a state

Displayed using matplotlib (quicker and smoother than turtle)
