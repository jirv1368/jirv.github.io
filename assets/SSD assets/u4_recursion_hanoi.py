# Towers of Hanoi Recursive Function

# This will output the disc moves to the pegs
def Hanoi(n , source, peg, auxiliary):
    if n==1:
        print ("Move disc 1 from peg",source,"to peg",peg)
        return
    Hanoi(n-1, source, auxiliary, peg)
    print ("Move disc",n,"from peg",source,"to peg",peg)
    Hanoi(n-1, auxiliary, peg, source)
         
# n is the number of discs in the tower and will determine the moves to solve it
# There should be a minimun of 3, this would solve it in 7 moves, more discs mean more moves are required
n = int(input("Enter number of discs: "))
# This will output the amount of moves
d =(2**n)-1
print("\nTotal Moves " + str(d))

# The pegs are numbered 1, 2, and 3
Hanoi(n,'1','2','3')

