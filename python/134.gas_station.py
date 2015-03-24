# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    # 4:56
    def canCompleteCircuit(self, gas, cost):
        if not gas or not cost:
            return -1

        total, curSum, start = 0, 0, 0
        for i in range(len(gas)):
            curCost = gas[i] - cost[i]
            curSum += curCost
            total += curCost

            if curSum < 0:
                curSum, start = 0, i + 1

        if total < 0:
            return -1
        else:
            return start % len(gas)
