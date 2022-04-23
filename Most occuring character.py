from collections import Counter
   def find(input_):
   # dictionary
   wc = Counter(input_)
   # Finding maximum occurrence
   s = max(wc.values())
   i = wc.values().index(s)
   print (wc.items()[i])
# Driver program
if __name__ == "__main__":
   input_ = 'sandeep'
   find(input_)