from pympler import summary, muppy


class MyObject(object):
    def __init__(self):
        self.memory = str(id(self)) * 2**10
            
def memory_summary(): 
    mem_summary = summary.summarize(muppy.get_objects())
    rows = summary.format_(mem_summary)
    return '\n'.join(rows)

if __name__ == "__main__":
    string = 'abc' * 2**26
    my_objs = [MyObject() for _ in range(2**16)]
    
    print(memory_summary())

'''
                       types |   # objects |   total size
============================ | =========== | ============
                 <class 'str |      122865 |    274.50 MB
                <class 'dict |       19297 |      9.02 MB
                <class 'code |       36790 |      5.08 MB
                <class 'type |        4578 |      4.65 MB
   <class '__main__.MyObject |       65536 |      3.50 MB
                <class 'list |       10792 |      1.82 MB
               <class 'tuple |       16592 |      1.07 MB
                 <class 'set |        2634 |      1.07 MB
             <class 'weakref |        7442 |    581.41 KB
         function (__init__) |        2542 |    337.61 KB
   <class 'getset_descriptor |        4596 |    323.16 KB
                 <class 'int |        9460 |    287.49 KB
         <class 'abc.ABCMeta |         265 |    268.62 KB
                <class 'cell |        5622 |    263.53 KB
  <class 'wrapper_descriptor |        2902 |    226.72 KB
'''