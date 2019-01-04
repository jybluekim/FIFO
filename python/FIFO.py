
class FIFO: 

    DEBUG = True

    # allocate variables and memory then call reset()
    def __init__(self, length):
      
        if self.DEBUG: print ("In init function")
        self.overflow = False
        self.underflow = False
        self.length = length 

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

    def read(self):
        item = self.mem[self.rd_ptr]

        if self.rd_ptr != self.wr_ptr:
            self.rd_ptr += 1
            if self.rd_ptr >= self.length:
                self.rd_ptr = 0
        else:
            self.underflow = True
            item = None

        return item


    def reset_underflow(self):
        self.underflow = False

    def reset_overflow(self):
        self.overflow = False


    def count(self):
        ret = self.wr_ptr - self.rd_ptr
        if ret < 0:
            ret = self.length + ret

        return ret

    def dump(self):
        print ("=============")
        print (self.mem)
        print ("wr_ptr: ", self.wr_ptr)
        print ("rd_ptr: ", self.rd_ptr)
        print ("overflow: ", self.overflow)
        print ("underflow: ", self.underflow)        
        print ("=============")


if __name__ == "__main__":

    import random 


    f = FIFO(8)
    

    for i in range (20):
        r_w = random.randint(1,3)
        if r_w == 1: # read
            r = f.read()
            if r == None and f.underflow:
                print ("Reading.. Underflow occured!!")
                f.reset_underflow()
            else:
                print ("Reading...", r)
    
        else:
            wv = random.randint(1,100)
            f.write(wv)
            if f.overflow:
                print ("Writing...", wv, ".. Overflow occurred!!")
                f.reset_overflow()
            else:
                print ("Writing...", wv)

        print ("Current number of items in the FIFO: ", f.count())
        f.dump()


 