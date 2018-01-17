import random

    
def rand():
    test = ["ravioli", "farfelle", "carbonara", "spaghetti", "lasagne"]
    print("Random     \n", random.random(),"\n",random.random(),"\n",random.random(),"\n",random.random(),"\n",random.random(),"\n")
    print("RandInt    \n", random.randint(1,10),"\n",random.randint(1,10),"\n",random.randint(1,10),"\n",random.randint(1,10),"\n",random.randint(1,10),"\n")
    print("RandRange  \n", random.randrange(1,10),"\n",random.randrange(1,10),"\n",random.randrange(1,10),"\n",random.randrange(1,10),"\n",random.randrange(1,10),"\n")
    print("RandFloat  \n", random.uniform(1,10),"\n",random.uniform(1,10),"\n",random.uniform(1,10),"\n",random.uniform(1,10),"\n",random.uniform(1,10),"\n")
    print("RandChoice \n", random.choice(test),"\n",random.choice(test),"\n",random.choice(test),"\n",random.choice(test),"\n",random.choice(test),"\n")
    print("RandSample \n", random.sample(test,3),"\n",random.sample(test,3),"\n",random.sample(test,3),"\n",random.sample(test,3),"\n",random.sample(test,3),"\n")
    print("RandShuffle")
    for i in range (0,5):
        random.shuffle(test)
        print(test)
if __name__ == "__main__":
    rand()
    
    
'''
Random     
 0.6482500717119858 
 0.7321057336522246 
 0.5260377314918446 
 0.6431567145870853 
 0.472825483417066 

RandInt    
 2 
 8 
 7 
 10 
 2 

RandRange  
 1 
 3 
 4 
 2 
 8 

RandFloat  
 1.951873204236501 
 1.0897213916390422 
 1.6446245088964906 
 5.906078241206072 
 9.09279933417104 

RandChoice 
 farfelle 
 ravioli 
 farfelle 
 spaghetti 
 farfelle 

RandSample 
 ['carbonara', 'spaghetti', 'lasagne'] 
 ['ravioli', 'carbonara', 'spaghetti'] 
 ['lasagne', 'farfelle', 'carbonara'] 
 ['farfelle', 'lasagne', 'spaghetti'] 
 ['ravioli', 'lasagne', 'farfelle'] 

RandShuffle
['carbonara', 'lasagne', 'farfelle', 'ravioli', 'spaghetti']
['carbonara', 'lasagne', 'spaghetti', 'farfelle', 'ravioli']
['spaghetti', 'lasagne', 'farfelle', 'carbonara', 'ravioli']
['ravioli', 'carbonara', 'farfelle', 'lasagne', 'spaghetti']
['carbonara', 'ravioli', 'farfelle', 'lasagne', 'spaghetti']
'''