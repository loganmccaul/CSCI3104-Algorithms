#LastName:McCaul
#FirstName:Logan
#Email:logan.mccaul@colorado.edu
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        #assert(len(w) > 0)

        # YOUR CODE HERE
        # If you want to create helper/auxiliary functions, please do so.
        if len(w) == 0:
            return
        else:
            letter = w[:1]
            if letter in self.next:
                if len(w) == 1:
                    self.next[letter].count += 1
                self.next[letter].addWord(w[1:])
            else:
                self.next[letter] = MyTrieNode(False)
                print (letter)
                if len(w) == 1:
                    self.next[letter].isWordEnd = True
                    self.next[letter].count += 1
                self.next[letter].addWord(w[1:])
        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        letter = w[:1]
        if letter not in self.next:
            return 0
        elif len(w) == 1:
            return self.next[letter].count
        else:
            return self.next[letter].lookupWord(w[1:])
        
        # YOUR CODE HERE
        
        return self.next[letter].count # TODO: change this line, please
    

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
        found = []
        node = self.find(w)
        word = self.lookupWord(w)
        if (word > 0):
            found.append((w, word))
        if node == None:
            return []
        return self.search(w, node, found)

    
    def find(self, w):
        letter = w[:1]
        if letter not in self.next:
            return None
        if len(w) == 1:
            return self.next[letter]
        else:
            return self.next[letter].find(w[1:])
        return self.next[letter]

    def search(self, w, node, found):
        for x, y in node.next.items():
            if node.next[x].isWordEnd:
                found.append((w+x, node.next[x].count))
            self.search(w+x, node.next[x], found)
        return found

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
