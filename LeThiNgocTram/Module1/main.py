class Fibonacci:
    def fibonacci(self, n, flag):
        """
        Tính số Fibonacci.

        Tham số:
        - n (int): chỉ số
        - flag (bool):
            + True  → trả về F(n) bằng đệ quy
            + False → trả về danh sách các số Fibonacci từ 0 đến n (dùng vòng lặp for)

        Trả về:
        - Số Fibonacci thứ n nếu flag = True
        - Danh sách số Fibonacci nếu flag = False
        """
        if flag:
            # Đệ quy
            if n < 2:
                return n
            return self.fibonacci(n - 1, True) + self.fibonacci(n - 2, True)
        else:
            # Vòng lặp for
            fib_sequence = []
            a, b = 0, 1
            for _ in range(n + 1):
                fib_sequence.append(a)
                a, b = b, a + b
            return fib_sequence
