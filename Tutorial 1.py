'''
Given two track which is an array of non-negative integers.
For each track, the variable trap need removing.

Problem 1.1
Remove all the traps and make sure the track remains connected (no empty cells)
i.e A[i] = trap are removed and shift all remaining elements left to fill the emptied cells.
'''
#Slower but interesting idea:
#Using the concept of mergesort (divide and conquer) but not directly solving yet only when there is a trap remove.
#O(nlgn) time and O(n) space.


#Naive solution:
#Do loop and create a new array and append those that are not loop.
#O(n) time and O(n) space

#Efficient solution:
#Use two pointers. If pointer 1 hit a trap, set pointer 2 to that index and continue to increase pointer 2 until a non trap and switch the value of A[pointer 2] = A[pointer 1].
# Then continue with pointer 1.
# O(n) time and O(1) space.
def Remove_Trap(track, trap):
    pointer_1 = 0
    while pointer_1 < len(track):
        if track[pointer_1] == trap:
            pointer_2 = pointer_1
            while track[pointer_2] == trap and pointer_2 <len(track)-1:
                pointer_2 +=1

            y = track[pointer_2]
            x = track[pointer_1]
            track[pointer_1] = y
            track[pointer_2] = x
        pointer_1 +=1

    for i in range(len(track)-1, 0, -1):
        if track[i] == trap:
            track.pop(i)

    return track
##Test:
print("Problem 1.1")
A = [2,1,3,2,0,1,2]
TrapA = 1
MyOwnSolution = Remove_Trap(A, TrapA)
print("A:",MyOwnSolution)
A_solution = [2,3,2,0,2]
if MyOwnSolution == A_solution:
    print("A is correct")
B = [1,2,1,2,0,0,3]
TrapB = 2
MyOwnSolution = Remove_Trap(B, TrapB)
print("B:",MyOwnSolution)
B_solution = [1,1,0,0,3]
if MyOwnSolution == B_solution:
    print("B is correct")


print()



"""Problem 1.2 We want to find out which track will allow you to get to the end of the array where the treasure is. 
Each cell in the track array lets you know the maximum you can advance to the right in ither words, at cell i, the furthest yolu can go to is A[i] + i. 
For example, A[0] = 2 so, you can take at most 2 steps to the right, and land at cell 2. Note that you can also take just 1 step if you wish.
Between tracks A and B above, only track A can let you land at the last index A[4].
Remember, the player that goes down the wrong track gets stuck, eaten by a python, and loses the game. 
How can we quickly discover which track is the right one? 
What is the time and space complexity of your method.
"""


#Observed, if we take the higher number, you will still get to the place that the previous number get.
#Take of it as fuel. At each step -1 the fuel. Take the fuel with the highest.
#O(n) time and O(1) space

def CheckReachTreasure(track):
    fuel = 0
    for i in range(len(track)):
        if fuel < track[i]:
            fuel = track[i]
        if fuel == 0: # unable to move
            return False
        if (i == len(track) -1):
            return True
        fuel -= 1



#Test
A = [2,3,2,0,2]
B = [1,1,0,0,3]
print("Problem 1.2")
print("A:", CheckReachTreasure(A))
print("B:", CheckReachTreasure(B))
