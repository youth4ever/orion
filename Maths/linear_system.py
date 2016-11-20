#-----------------------------------------------------------------------------

"""Routines to solve linear systems in the form Ax=b by factoring a row-
permuted matrix A into L and U and solving for x using forward and back
solves

USAGE:
    p = lu( A )
    x = solve( A, p, b )

AUTHOR:
    Jonathan Senning <jonathan.senning@gordon.edu>
    Gordon College
    October 2008 (Based on Octave code written in February 1999)
"""

import numpy as np

#-----------------------------------------------------------------------------

def lu( A ):
    """Factor A into LU by Gaussian elimination with scaled partial pivoting

    USAGE:
        p = lu( A )

    INPUT:
        A     - NumPy matrix to be factored.  This matrix should should
                have a floating point data type.
                ***** THIS MATRIX IS MODIFIED *****

    OUTPUT:
        p     - (integer list) contains the row permutation information

    NOTES:
        This function performs Gaussian elimination with scaled partial
        pivoting on a square matrix A.  It returns the LU factorization of a
        and a permutation vector that indicates the true position of the rows
        in the result.

        The companion function solve() can be used to solve Ax=b once A has
        been factored by this function.
    """

    n, m = np.shape( A )
    if n != m:
        print ("Error: input matrix is not square")
        return None

    # Generate initial index vector

    p = range( n )

    # Determine the largest (in magnitude) element in each row.  These
    # factors are used to scale the pivot elements for comparison purposes
    # when deciding which row to use as a pivot row.

    s = [0] * n
    for i in xrange( n ):
        smax = 0.0
        for j in xrange( n ):
            smax = max( smax, abs( A[i,j] ) )
        s[i] = smax

    # Begin Gaussian elimination.

    for k in xrange( n - 1 ):

        # Find the remaining row with the largest scaled pivot.

        rmax = 0.0
        for i in xrange( k, n ):
            r = abs( A[p[i],k] / s[p[i]] )
            if r > rmax:
                rmax = r
                j = i

        # Row j has the largest scaled pivot, so "swap" that row with the
        # current row (row k).  The swap is not actually done by copying rows,
        # but by swaping two entries in an index vector.

        p[j], p[k] = ( p[k], p[j] )

        # Now carry out the next elimination step as usual, except for the
        # added complication of the index vector.

        for i in xrange( k + 1, n ):
            xmult = A[p[i],k] / A[p[k],k]
            A[p[i],k] = xmult
            for j in xrange( k + 1, n ):
                A[p[i],j] = A[p[i],j] - xmult * A[p[k],j]

    # All done, return factored matrix A and permutation vector p

    return ( A, p )

#-----------------------------------------------------------------------------

def solve( A, p, b ):
    """Solves Ax = b given an LU factored matrix A and permuation vector p

    USAGE:
        x = solve( A, p, b )

    INPUT:
        A     - NumPy matrix that contains LU factored form of A
        p     - list or NumPy array of permuted row positions
        b     - NumPy matrix or array containing RHS vector

    OUTPUT:
        x     - (NumPy array) Solution vector

    NOTES:
        This function performs the backward and forward solves necessary to
        use the LU factorization of a square matrix A to solve Ax=b.  The LU
        factorization is assumed to have been generated by the function
        lu() and has an associated permutation vector that indicates the
        true row values in the factored matrix.
    """

    n, m = np.shape( A )
    if n != m:
        print ("Error: input matrix is not square")
        return None

    # Forward solve

    x = np.zeros( n )

    for k in xrange( n - 1 ):
        for i in xrange( k + 1, n ):
            b[p[i]] = b[p[i]] - A[p[i],k] * b[p[k]]

    # Backward solve

    for i in xrange( n - 1, -1, -1 ):
        sum = b[p[i]]
        for j in xrange( i + 1, n ):
            sum = sum - A[p[i],j] * x[j]
        x[i] = sum / A[p[i],i]

    # All done, return solution vector

    return x
