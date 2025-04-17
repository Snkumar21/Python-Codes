# Example of bubble sorting using class in python...
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def display(self):
        print("Sorted array:", self.arr)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble = BubbleSort(arr)
bubble.sort()
bubble.display()