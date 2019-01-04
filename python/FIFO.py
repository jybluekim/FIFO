
class FIFO: 

    DEBUG = True

    # allocate variables and memory then call reset()
    def __init__(self, length):
      
        if self.DEBUG: print ("In init function")
        self.overflow = False
        self.underflow = False
        self.length = 1 << length # for input 5, we have 1 << 5 = 2^5 = 32

        self.mem = [ None for i in range (self.length) ]
        self.reset()

    # reset everything 
    def reset(self):
        if self.DEBUG: print ("In reset function")

        self.overflow = False
        self.underflow = False
        self.rd_ptr = 0
        self.wr_ptr = 0


    def write(self, item):
        next = self.wr_ptr + 1 
        if next >= self.length:
            next = 0
        if next != self.rd_ptr:
            self.mem[self.wr_ptr] = item
            self.wr_ptr = next
        else:
            self.overflow = True


    def dump(self):
        print (self.mem)




if __name__ == "__main__":

    import random 

    f = FIFO(4)
    
    for i in range(5):
        x = random.randint(1,100)
        f.write(x)

    f.dump()
