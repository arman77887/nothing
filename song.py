import time
import sys

def print_lyrics():
   lyrics = [
     "Haathon ko sambhale mere haathon meni",
     "kaise haathon ko sambhale mere haathon meni",
     "jab tak neend na aaya, inn lakeeron meni",
     "Baateni hon..........",
     "Haayee........"
   ]
delays =[1.0, 0.1, 1.22, 0.9, 0.8]
print("Arz kya hai?...........\n)
 time.sleel(1.4)

        for i, line in enumerate(lyrics):
           for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
print()
time.sleep(delays[i])

print_lyrics()
