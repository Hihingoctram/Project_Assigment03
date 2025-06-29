class Fibonacci:
    def fibonacci(self, n, flag):
        """
        Hàm tính số Fibonacci.

        Tham số:
        - n (int): vị trí số Fibonacci (>= 0)
        - flag (bool): 
            + True  → trả về số Fibonacci thứ n
            + False → in dãy Fibonacci từ 0 đến n

        Trả về:
        - Số Fibonacci thứ n nếu flag = True
        - None nếu flag = False
        """
        if flag:
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        else:
            a, b = 0, 1
            print(f"Dãy Fibonacci đến n = {n}:")
            for _ in range(n + 1):
                print(a, end=' ')
                a, b = b, a + b
            print()
            return None
