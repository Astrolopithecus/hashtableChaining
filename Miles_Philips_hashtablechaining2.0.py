# Miles Philips
# Prog 260
# 8-5-19
# Implementation of a hash table where keys are strings treated case-insensitive. This class uses
# chaining collision resolution scheme.
class Node:
    ''' Node class that holds a (key,value) pair to be used in the 
    LinkedList class
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    '''
    LinkedList class that holds a linked list of Node class objects 
    holding (key, value) pairs. Keys are strings which are case-insensitive.
    '''
    def __init__(self):
        self.head = None

    def add(self, key, value):
        ''' Method to add data to the end of the list
        '''
        # Create a node with given key/value pair
        node = Node(key, value) 
        # If list is empty, set the node to be the head
        if self.head == None:
            self.head = node
        # Otherwise add the new node at the head    
        else:
            node.next = self.head
            # Set new node's next pointer to self.head
            node.next = self.head
            # Update the head to be the new node
            self.head = node
    
    def search(self, key):
        '''Searches the list sequentially to find a node that matches the 
        given key & returns it
        '''
        if self.head == None:
            return None
        else:
            current = self.head
            while current:
                if (current.key == key):
                    return current
                current = current.next
            return None


    def __len__(self):
        '''Returns the number of nodes in the list
        '''
        if self.head == None:
            return 0
        else:
            length = 0
            current = self.head
            while (current):
                length += 1
                current = current.next
            return length

class HashTableChaining:
    ''' Class to represent a Hash table where keys are strings treated
    case-insensitive. This class uses Chaining collision resolution scheme.
    '''
    def __init__(self, size):
        '''constructor that takes one parameter for the size of the hash table
        '''
        #size of table
        self.size = size
        #a list of given size of empty LinkedList objects.
        self.hashTable =[LinkedList()] * self.size
         
    def hashFunction(self, key, size):
        '''hash function which accepts keys that are of string type 
        calculates the hash value using the ordinal value of the first 
        two letters of the key. It adds the ordinal value of the first 
        two letters with weights of 1 and 2 respectively. It then applies 
        the "remainder".
        '''
        return (ord(key[0]) + 2 * ord(key[1])) % size

    def put(self, key, value):
        '''This method adds a new (key, value) pair to the LinkedList at
         the correct slot of the hash table.
        '''
        hashvalue = self.hashFunction(key,self.size)

        if self.hashTable[hashvalue] == None:
            self.hashTable[hashvalue] = key
            self.hashTable[hashvalue] = value

        else:
            if self.hashTable[hashvalue] == key:
                self.hashTable[hashvalue] = value  #replace
            else:
                nextslot = (hashvalue+1) % self.size
                while self.hashTable[nextslot] != None and self.hashTable[nextslot] != key:
                    nextslot = (hashvalue+1) % self.size

                if self.hashTable[nextslot] == None:
                    self.hashTable[nextslot] = key
                    self.hashTable[nextslot] = value
                else:
                    self.hashTable[nextslot] = value #replace

    def get(self, key):
        '''method returns the value corresponding to the given key from the 
        hash table if the key is present in the hash table otherwise returns 
        None.
        '''
        startslot = self.hashFunction(key, self.size)
        data = None
        stop = False
        found = False
        position = startslot
        while self.hashTable[position] != None and not found and not stop:
            if self.hashTable[position] == key:
                found = True
                data = self.hashTable[position]
            else:
                position = self.hashFunction(position + 1, self.size)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, value):
        return self.put(key, value)            

def main():
    print("Welcome to Student Score Hash table\n")
    studentTable = HashTableChaining(11)
    names = ["Albert", "Sandra", "Sally","Mike", "Alison", "George", "sally", "Gayle", "mike"]
    scores = [10,20,30,40,50,60,70,80,100]

    print("Printing hash values: ")
    print([(k, studentTable.hashFunction(k,11)) for k in names])
    
    print()
    #Setting the student scores in the hashtable
    for k in range(len(names)):
        studentTable[names[k]] = scores[k]

    #Checking lengths of different slots in the hashtable
    print("Printing lengths of slots of the hash table: ")
    totalNodes = 0
    for k in range(len(studentTable.hashTable)):
        l = len(studentTable.hashTable[k])
        totalNodes += l
        print(f"({k}, {l})",end=" ")    
    print("\nNumber of total Nodes:", totalNodes)
    
    print()
    #Retrieving the scores using name as the key
    print("Printing scores: ")
    for k in range(len(names)):
        print(f"Checking {names[k]}'s score: {studentTable[names[k]]}")

   
if __name__ == "__main__":
    main()
