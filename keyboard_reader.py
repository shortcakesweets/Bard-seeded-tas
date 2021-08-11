
import keyboard
import time

sequence = ''
key_split = 'm'
key_terminate = 'n'

print(" Auto keyboard listener will start in 3 seconds ")
time.sleep(3)
print(" Started. ")


while True:
    sequence += keyboard.read_key()

    last = len(sequence) - 1

    if sequence[last] == key_split :
        print( sequence[0:last] )
        sequence = ''
    elif sequence[last] == key_terminate :
        print( sequence[0:last] )
        break

    time.sleep(0.1)