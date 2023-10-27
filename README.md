# Twelve Coin Problem 

## Problem 
Given 12 coins, one of which is counterfeit and either heavier or lighter than the other equal-weighing coins, find the counterfeit coin and its weight in a maximum of three balance weighings. 

## Solution 
This solution involves splitting the coins into groups, initially: A1, A2, A3, A4; B1, B2, B3, B4; C1, C2, C3, C4. 
* First weigh all A coins against all B coins. 
* If equal, weigh the first three A coins against the first three C coins. If equal again weigh any coin against C4 to find whether it is heavier or lighter. If not, weigh two of the first three C coins against each other.
* If not equal, weigh A1, A2, B1, B2 against B4, C1, C2, C3.
* If equal, the counterfeit coin is among A3, A4, B3 and any of these can be weighed against each other.
* If the same side is heavier as before, the counterfeit coin is among A1, A2, B4 and any of these can be weighed against each other. If the opposite side is heavier than the counterfeit coin is among B1 or B2 and either can be weighed against any of the genuine coins. 
