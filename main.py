import unittest

class Coin: 
    def __init__(self) -> None: 
        self.weight: int = 2

    def __call__(self) -> int: 
        return self.weight

    def assign_weight(self, weight: int) -> None:
        self.weight: int = weight

class Answer: 
    def __init__(self, coin: int, weight: int) -> None: 
        self.coin: int = coin
        self.weight: int = weight

class Coins: 
    def __init__(self) -> None: 
        self.coins: list = [Coin() for _ in range(13)]

    def get_coins(self, *args: list) -> list:
        return [self.coins[i] for i in args]
   
class Balance: 
    def weigh(self, left: list, right: list) -> int: 
        left_weight: int = sum(coin() for coin in left)
        right_weight: int = sum(coin() for coin in right)
        
        if left_weight > right_weight: 
            return -1 
        elif left_weight < right_weight: 
            return 1
        else: 
            return 0

class Solution: 
    def __init__(self, counterfeit_coin: int, counterfeit_weight: int) -> None: 
        self.counterfeit_coin: int = counterfeit_coin
        self.counterfeit_weight: int = counterfeit_weight
        self.coins: Coins = self.setup()
        self.balance: object = Balance()

    def setup(self) -> Coins:
        coins: object = Coins()

        coins.coins[self.counterfeit_coin].assign_weight(self.counterfeit_weight)

        return coins
    
    def find_counterfeit(self) -> list:
        weigh_one = self.balance.weigh(self.coins.get_coins(0, 1, 2, 3), self.coins.get_coins(4, 5, 6, 7))

        if weigh_one == 0: 
            weigh_two = self.balance.weigh(self.coins.get_coins(0, 1, 2), self.coins.get_coins(8, 9, 10))

            if weigh_two == 0: 
                weigh_three = self.balance.weigh(self.coins.get_coins(0), self.coins.get_coins(11))

                if weigh_three == -1: 
                    answer = Answer(11, 1)
                elif weigh_three == 1: 
                    answer = Answer(11, 3)

            elif weigh_two == -1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(8), self.coins.get_coins(9))

                if weigh_three == 0: 
                    answer = Answer(10, 1)
                elif weigh_three == -1: 
                    answer = Answer(9, 1)
                elif weigh_three == 1: 
                    answer = Answer(8, 1)

            elif weigh_two == 1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(8), self.coins.get_coins(9))

                if weigh_three == 0: 
                    answer = Answer(10, 3)
                elif weigh_three == -1: 
                    answer = Answer(8, 3)
                elif weigh_three == 1:
                    answer = Answer(9, 3)

        elif weigh_one == -1: 
            weigh_two = self.balance.weigh(self.coins.get_coins(0, 1, 4, 5), self.coins.get_coins(6, 8, 9, 10))

            if weigh_two == 0:
                weigh_three = self.balance.weigh(self.coins.get_coins(2), self.coins.get_coins(3))

                if weigh_three == 0: 
                    answer = Answer(7, 1)

                elif weigh_three == -1: 
                    answer = Answer(2, 3)

                elif weigh_three == 1: 
                    answer = Answer(3, 3)

            elif weigh_two == -1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(0), self.coins.get_coins(1))

                if weigh_three == 0: 
                    answer = Answer(6, 1)

                elif weigh_three == -1: 
                    answer = Answer(0, 3)

                elif weigh_three == 1: 
                    answer = Answer(1, 3)

            elif weigh_two == 1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(4), self.coins.get_coins(5))

                if weigh_three == -1: 
                    answer = Answer(5, 1)

                elif weigh_three == 1: 
                    answer = Answer(4, 1)

        elif weigh_one == 1: 
            weigh_two = self.balance.weigh(self.coins.get_coins(0, 1, 4, 5), self.coins.get_coins(6, 8, 9, 10))

            if weigh_two == 0: 
                weigh_three = self.balance.weigh(self.coins.get_coins(2), self.coins.get_coins(3))

                if weigh_three == 0: 
                    answer = Answer(7, 3)

                elif weigh_three == -1: 
                    answer = Answer(3, 1)

                elif weigh_three == 1: 
                    answer = Answer(2, 1)

            elif weigh_two == -1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(4), self.coins.get_coins(5))

                if weigh_three == -1: 
                    answer = Answer(4, 3)

                elif weigh_three == 1: 
                    answer = Answer(5, 3)

            elif weigh_two == 1: 
                weigh_three = self.balance.weigh(self.coins.get_coins(0), self.coins.get_coins(1))

                if weigh_three == 0: 
                    answer = Answer(6, 3)

                elif weigh_three == -1: 
                    answer = Answer(1, 1)

                elif weigh_three == 1:
                    answer = Answer(0, 1)
                
        return [answer.coin, answer.weight]
    
class Tests(unittest.TestCase):
    pass

def create_test_case(n, m):
    def test(self):
        solution = Solution(n, m)
        self.assertEqual(solution.find_counterfeit(), [n, m])

    return test

if __name__ == '__main__':
    test_params = [(n, m) for n in range(12) for m in [1, 3]]

    for i, (n, m) in enumerate(test_params):
        test_method = create_test_case(n, m)
        test_name = f'test_{i + 1}'
        setattr(Tests, test_name, test_method)

    unittest.main()
