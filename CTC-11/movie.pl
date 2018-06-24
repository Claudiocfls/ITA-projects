%% base de conhecimento
filme(amnesia,suspense,nolan,2000,113).
filme(babel,drama,inarritu,2006,142).
filme(capote,drama,miller,2005,98).
filme(casablanca,romance,curtiz,1942,102).
filme(matrix,ficcao,wachowsk,1999,136).
filme(rebecca,suspense,hitchcock,1940,130).
filme(shrek,aventura,adamson,2001,90).
filme(sinais,ficcao,symalan,2002,106).
filme(spartacus,acao,kubrik,1960,184).
filme(superman,aventura,donner,1978,143).
filme(titanic,romance,cameron,1997,194).
filme(tubarao,suspense,spielberg,1975,124).
filme(volver,drama,almodovar,2006,121).

%% regras
diretor(X,Y) :- filme(X,_,Y,_,_).
genero(X,Y) :- filme(Y,X,_,_,_).
dirigido(X,Y) :- filme(Y,_,X,_,_).
lancadoem(X,Y) :- filme(X,_,_,Y,_).
duracaomenor(X,Y) :- filme(Y,_,_,_,A), A<X.
lancadoentre(X,Y,F) :- filme(F,_,_,A,_), A>=X, A=<Y.
classico(X) :- lancadoentre(0,1980,X).
