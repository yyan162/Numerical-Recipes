from   numpy import matrix 
import numpy as     np


class Linear:
    'Class to evaluate y = mx + c for a given instance defined by m and c'

    # Here a matrix of type matrix([m, c.]).T is used to initalise.  If no matrix is passed
    # a default behaviour is implemented, setting m=0, c=1.

    def __init__(self, i = matrix([0., 1.]).T):
        self.m     = i[0,0]
        self.c     = i[1,0]

    # This method assigns m and c for a given instance. 

    def set_elements(self, j):
        if (j.shape != (2, 1)):
            print 'Invalid column vector, must be a (2,1) matrix for assignment.'

        self.m = float(j[0,0])
        self.c = float(j[1,0])

    # This is the evaluate method for a single data point.     
    def eval(self, x):
        return self.m*x + self.c

    # Here we vectorize a function.  Having defined a function eval which acts on a scalar
    # (i.e number) and returns a scalar, vecfn = vectorize(eval) gives us a function vecfn which 
    # will act on np.arrays or matrices and returns a np.array or matrix in which "out_array[i]"
    # is "eval(in_array[i])" **(pseudocode)**.

    def veval(self, j):
        vecfn  = np.vectorize(self.eval) 
        return vecfn(j)
        

class ChiSq:
    'Class to provide a method to calculate chisq'

    # This is the constructor which sets up the vectors (data x and y) and matrices (inverse error matrix)     
    
    def __init__(self, xin=matrix([]).T, yin=matrix([]).T, ein=matrix([]).T):
        self.xdata  = xin
        self.ydata  = yin
        self.edata  = ein
        self.linear = Linear()

        # Do some checks                                                                                                   
        if(xin.shape == yin.shape == ein.shape and xin.shape[1] == 1 and xin.shape[0] != 0):
            # This bit constructs the error matrix and takes its inverse                                           
            self.cov    = matrix(np.diag(np.diag(self.edata*self.edata.T)))
            self.Icov   = self.cov.I

            ## Notes ##                                                                                                         
            # The numpy matrix class, with instance A, has methods to transpose: A.T, and inverse: A.I                     
            # self.edata*self.edata.T is a matrix, np.diag(self.edata*self.edata.T) returns a vector of the                
            # diagonal elements of this matrix.                                                                            
            # Finally np.diag(np.diag(self.edata*self.edata.T)) forms a diagonal matrix of solely these components         

        else:
            print("input x-y-e dimension error")
     
    # To pass in a new set of parsmeters, in this case m & c                                                               
    def setparams(self, params):
        self.linear.set_elements(params)  

    # Evaluate the chisq                                                                                                                                                      
    def evaluate(self):
        # Create a vector of theoretical points                                                                            
        yth = self.linear.veval(self.xdata)                                                                                                                                  
        # Take the difference                                                                                              
        diff = self.ydata - yth
                
        # Finally form the chisq                                                                                           
        chiSq  = diff.T*self.Icov*diff            
        
        return chiSq[0,0] 


class ChiSqII:
    def __init__(self):
        print 'Evaluating a chisq'
        data = np.loadtxt("decayTimes.txt")
        
        self.data = data 
        
        # Create Chisq object                                                                                              
        self.instance = ChiSq(matrix(data[:, 0]).T, matrix(data[:, 1]).T, matrix(data[:, 2]).T)

        # Finally form the chisq                                                                                           
        result = self.instance.evaluate()
    
        print result

