class Fibonacci:
    def fibonacci(self, n, flag):
        """
        Tính số Fibonacci.

        Tham số:
        - n (int): chỉ số
        - flag (bool):
            + True  → có thể để trống hoặc return -1 (vì chỉ xử lý False ở impl2)
            + False → trả về danh sách các số Fibonacci từ 0 đến n (dùng vòng lặp for)

        Trả về:
        - Danh sách số Fibonacci nếu flag = False
        """
        if not flag:
            fib_sequence = []
            a, b = 0, 1
            for _ in range(n + 1):
                fib_sequence.append(a)
                a, b = b, a + b
            return fib_sequence
        else:
            return -1  # hoặc raise NotImplementedError("Chưa xử lý khi flag=True")
