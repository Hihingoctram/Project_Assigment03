class Fibonacci:
    def fibonacci(self, n, flag):
        """
        Tính số Fibonacci.

        :param n: chỉ số (>=0)
        :param flag:
            True  -> trả về F(n) bằng đệ quy
            False -> in dãy từ 0..n (giữ nguyên logic cũ)
        """
        if flag:
            # ---- ĐỆ QUY ----
            if n < 2:
                return n
            return self.fibonacci(n - 1, True) + self.fibonacci(n - 2, True)
        else:
            a, b = 0, 1
            print(f"Dãy Fibonacci đến n = {n}:")
            for _ in range(n + 1):
                print(a, end=" ")
                a, b = b, a + b
            print()
            return None
