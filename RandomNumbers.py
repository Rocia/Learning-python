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
        
def random_generator_decl():
    return random.SystemRandom()      
  
    
def pseudo_random(rand_gen):
    test = ["ravioli", "farfelle", "carbonara", "spaghetti", "lasagne"]
    print("Pseudo Random     \n", rand_gen.random(),"\n",rand_gen.random(),"\n",rand_gen.random(),"\n",rand_gen.random(),"\n",rand_gen.random(),"\n")
    print("Pseudo RandInt    \n", rand_gen.randint(1,10),"\n",rand_gen.randint(1,10),"\n",rand_gen.randint(1,10),"\n",rand_gen.randint(1,10),"\n",rand_gen.randint(1,10),"\n")
    print("Pseudo RandRange  \n", rand_gen.randrange(1,10),"\n",rand_gen.randrange(1,10),"\n",rand_gen.randrange(1,10),"\n",rand_gen.randrange(1,10),"\n",rand_gen.randrange(1,10),"\n")
    print("Pseudo RandFloat  \n", rand_gen.uniform(1,10),"\n",rand_gen.uniform(1,10),"\n",rand_gen.uniform(1,10),"\n",rand_gen.uniform(1,10),"\n",rand_gen.uniform(1,10),"\n")
    print("Pseudo RandChoice \n", rand_gen.choice(test),"\n",rand_gen.choice(test),"\n",rand_gen.choice(test),"\n",rand_gen.choice(test),"\n",rand_gen.choice(test),"\n")
    print("Pseudo RandSample \n", rand_gen.sample(test,3),"\n",rand_gen.sample(test,3),"\n",rand_gen.sample(test,3),"\n",rand_gen.sample(test,3),"\n",rand_gen.sample(test,3),"\n")
    print("Pseudo RandShuffle")
    for i in range (0,5):
        rand_gen.shuffle(test)
        print(test)    
    
   
if __name__ == "__main__":
    rand()
    rand_gen = random_generator_decl()
    pseudo_random(rand_gen)
    
    
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

Pseudo Random     
 0.4053336197238897 
 0.1215484263400548 
 0.7029225918337397 
 0.3380994114460928 
 0.20020357824013335 

Pseudo RandInt    
 5 
 10 
 8 
 2 
 7 

Pseudo RandRange  
 4 
 4 
 5 
 9 
 9 

Pseudo RandFloat  
 8.769135536343104 
 9.152618824107037 
 6.5110161402314795 
 2.7236291851803682 
 3.3697509371916885 

Pseudo RandChoice 
 carbonara 
 carbonara 
 carbonara 
 spaghetti 
 ravioli 

Pseudo RandSample 
 ['lasagne', 'farfelle', 'spaghetti'] 
 ['farfelle', 'spaghetti', 'lasagne'] 
 ['ravioli', 'spaghetti', 'farfelle'] 
 ['spaghetti', 'carbonara', 'lasagne'] 
 ['lasagne', 'spaghetti', 'farfelle'] 

Pseudo RandShuffle
['ravioli', 'carbonara', 'farfelle', 'lasagne', 'spaghetti']
['ravioli', 'carbonara', 'lasagne', 'spaghetti', 'farfelle']
['ravioli', 'carbonara', 'farfelle', 'lasagne', 'spaghetti']
['farfelle', 'lasagne', 'ravioli', 'spaghetti', 'carbonara']
['farfelle', 'spaghetti', 'lasagne', 'ravioli', 'carbonara']
'''