import heapq

class StockHeap:
    def __init__(self, products):
        self.heap = products[:]
        heapq.heapify(self.heap)

    def get_low_stock(self, k):
        return heapq.nsmallest(k, self.heap)
