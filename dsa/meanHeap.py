class MinHeap:
    
    def __init__(self, capacity):
        self.storage = [0]* capacity
        self.capacity = capacity
        self.size = 0
        
    # helper method
    def get_parent_index(self, index):
        return (index-1)//2

    def get_left_child_index(self, index):
        return index*2 +1 

    def get_right_child_index(self, index):
        return index*2+2
    
    # Check Parent/Child 
    def hasParent(self, index):
        return self.get_parent_index(index)>=0

    def hasLeftChild(self, index):
        return self.get_left_child_index(index) < self.size 
    
    def hasRightChild(self, index):
        return self.get_right_child_index(index) < self.size

    
    # get the value
    def parent(self, index):
        return self.storage[self.get_parent_index(index)]
    def leftChild(self, index):
        return self.storage[self.get_left_child_index(index)]
    def rightChild(self, index):
        return self.storage[self.get_right_child_index(index)]
    
    def isFull(self):
        return self.size == self.capacity
    
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]


    def heapifyUp(self):
        index = self.size -1
        while(self.hasParent(index)) and \
        self.parent(index) > self.storage[index]:
            self.swap(index, self.get_parent_index(index))
            # to look back to parent  
            index = self.get_parent_index(index)



    # Insert 
    def insert(self, data):
        if self.isFull():
            raise("Heap is Full ")
        self.storage[self.size] = data 
        self.size +=1 
        self.heapifyUp()

    

# Test 
min_heap_test = MinHeap(7)
x = [10,12,1,4,6,7,9]
for item in x:
    min_heap_test.insert(item)
    print(min_heap_test.storage)