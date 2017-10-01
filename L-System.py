import matplotlib.pyplot as plt
import numpy as np

"""
Non Stochastic Context free L-system implementation for python 3.x
Conformaly to the description given in 'The Algorithmic Beauty of Plants' by Lindenmayer (algorithmicbotany.org/papers/abop/abop.pdf)
i.e : the angles are in degrees and grow clockwise
	  supports edge and node rewriting
	  supports branching
all lower cases : forward line
all upper cases : ignored in the drawing prosses
_               : forward without drawing
[ , ]           : respectively saving and popping a state
h               : initial heading, for manual correction of the orientation of the figure (in degrees)

Displayed using matplotlib (quicker and smoother than turtle)

"""

def L_system( axiom, rule , angle, iterations=2, h=0 ):
	d, h, axiom_ = angle*np.pi/180, h*np.pi/180, axiom
	R = { '-': [ [np.cos( d), -np.sin( d)],[np.sin( d), np.cos( d)] ] ,
		  '+': [ [np.cos(-d), -np.sin(-d)],[np.sin(-d), np.cos(-d)] ] }

	for i in range(iterations):
		sequence =''
		for i in axiom_ :
			try :
				sequence += rule[i]
			except :
				sequence +=  i
		axiom_ = sequence
	print(axiom_)

	a, k = (0,0), []
	r    = [ [np.cos(h), -np.sin(h)],[np.sin(h), np.cos(h)] ]
	
	for i in axiom_ :
		if  i.islower() :
			b = np.transpose(np.add(a, np.matmul(r, np.transpose([0,1]) )))
			plt.plot([ a[0],b[0] ], [ a[1],b[1] ], color='g')
			a = b
		elif i in R:
			r = np.transpose(np.matmul(R[i], np.transpose(r) ))
		elif i=='_':
			a = np.transpose(np.add(a, np.matmul(r, np.transpose([0,1]) )))
		elif i=='[':
			k.extend([a,r])
		elif i==']':
			r, a = k.pop(), k.pop()

	plt.suptitle("n=%s, angle=%s°, axiom=%s" %(iterations, angle, axiom))
	plt.title(str(rule).replace("'",""))

#exemple (d) page 25
axiom      = 'X'
rule       = { 'f':'ff' , 'X':'f[+X]f[-X]+X' }
angle      = 20
iterations = 7

L_system(axiom, rule, angle, iterations)

plt.axis('off')
plt.axis('equal')
plt.savefig( '%s_%s' %(axiom,iterations) )
plt.show()