time = int(input("time :"))
acceleration = int(input("acceleration :"))
distance = int(input("distance :"))
for i in range (0, time+1):
    finish = acceleration *i*i/2
    finish = finish / 10
    finish = int(finish)
    print("Duration: ",i,"distance:","*" * finish)

finish = acceleration*i*i/2

if((acceleration*i)>60):
    print ("Over the speed limit. (Max speed was ",acceleration*i," m/s)")
else :
    print ("didn't go over the speed limit.(Max speed was ",acceleration*i,"m/s)")
if (finish >= distance):
    print("reach the destination. (Reached ",finish," m)")
else :
    print ("didn't reach the destination.(Reached ",finish,"m)")
