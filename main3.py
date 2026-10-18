def fib_series(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # uptade values
        n1 = n2
        n2 = nth
        count += 1 

nterms = int (input("How many terms"))

 if nterms <= 0:
   print("Please enter a positive interger")
 elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   fib_series(nterms)
 else:
   print("Fibinacci secquence:")
   fib_series(nterms)