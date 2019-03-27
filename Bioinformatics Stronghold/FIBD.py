n = 95
m = 20

#initialize the storage
rabbit_recorder = [0]*m

rabbit_recorder[0] = 1
#first generation from 0 month: has a rabbit
#rabbit will give birth after 1 month, and died after m months
#the sum of all the values in the vector rabbit_recorder is the total number of rabbits at month n


for i in range(1, n):
    #print rabbit_recorder
    #<1 month rabbits were not sexually matured
    new_borns = sum(rabbit_recorder[1:m])
    #rabbits that are older than m month will be extinguished
    rabbit_recorder = [new_borns] + rabbit_recorder[0:m-1]
    
print sum(rabbit_recorder)