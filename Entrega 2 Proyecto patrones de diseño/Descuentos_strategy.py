class DescuentoStrategy:
    def aplicar(self, total):
        return total

class Normal(DescuentoStrategy):
    pass

class Premium(DescuentoStrategy):
    def aplicar(self, total):
        return total * 0.9

class VIP(DescuentoStrategy):
    def aplicar(self, total):
        return total * 0.8