mdc(X,Y,G) :- X=Y, G=X.
mdc(X,Y,G) :- X<Y, Y1 is Y-X, mdc(X,Y1,G).
mdc(X,Y,G) :- X>Y ,mdc(Y,X,G).

common_divisor(X,Y) :- Y=1.
common_divisor(X,Y) :- Y>1, mdc(X,Y,1), Y1 is Y-1, common_divisor(X,Y1). 
is_prime(X) :- X>0, X1 is X-1, common_divisor(X,X1). 