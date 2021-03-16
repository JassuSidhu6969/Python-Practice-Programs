from time import time

start = time()
userinput = input("Type any sentence to start: ")
end= time()
total = round(end-start, 2)
w = len(userinput.split())
print("Total time taken by user = %s Seconds" % (total) )
total = int(total)/60
print("Average speed of the user: %s WPM" % str(w/total))
