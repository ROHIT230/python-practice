import threading , time



def calculate(seconds):
    print(f"Executing in {seconds} seconds")
    time.sleep(seconds)


# start= time.perf_counter()
# calculate(4)
# calculate(3)
# calculate(2)

# end = time.perf_counter()




# print("noraml calling",end-start)

tstart= time.perf_counter()
t1=threading.Thread(target=calculate, args=[4])
t2=threading.Thread(target=calculate, args=[3])
t3=threading.Thread(target=calculate, args=[2])


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

thend = time.perf_counter()

print(thend-tstart)