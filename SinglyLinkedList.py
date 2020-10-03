#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Node:  #Node class
    def __init__(self,data):  #Function to initialize the node object
        self.data = data  #assigning data
        self.next = None  #initialize next as null

#linked list class

class LinkedList:
# Function to initialize the Linked  
# List object  
  def __inti__(self):
        self.head = None
        
  def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
        
    
if __name__ == '__main__': #execution is starting from here
    
        llist = LinkedList()
        
        llist.head = Node(1) #1st node
        second = Node(2)     #2nd node
        third = Node(3)      #3rd node 
        
        llist.head.next = second;
        second.next = third;
        
        llist.printList()
        


# In[ ]:




