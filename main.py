
import cv2
import pyautogui
import numpy as np
import time
import keyboard

# Debug purpose
cv2.namedWindow("Threshold Debug")
cv2.moveWindow("Threshold Debug", -1000, 300)
pre_shopkeeper = True

################### User inputs #######################

seed = '641499'
default_interval : float = 0.05

# references
prepthrow = 's'
bomb = 'w'
item_1 = 'd'
item_2 = 'a'
spell_1 = 'q'
spell_2 = 'e'
left = 'j'
right = 'l'
up = 'i'
down = 'k'
manual_mode_exit = 'c'

# Screen resolution
x, y = 1920, 1080
input_1_1 = 'kllllllllkkkkllllkkkkkkjjjjkkkjjjjjjijjjjkjjjkkjjijkjjjjljljljjjjjiijjjj'
#input_1_1 = 'kllllllllkkkkllllkkkkkkjjjjkkkjjjjjjijjjjkjjjkkjjijkjjjjljljljjjjjjjjjii'
input_1_2 = 'kkjjwllkjjkliiiwjii' # because of shopkeeper this sequence is further noted in TAS()
input_1_3 = 'lllt'
input_1_4 = 'likkjliiiiissk' # because of DM this sequence is further noted in TAS()
input_2_1 = 'jjjiikkj'
input_2_2 = 'jjjjjkkkk'
input_2_3 = 'jjjkkkkjjjjkkjjskks'
input_2_4 = 'iiiiiii'
input_3_1 = 'iiiiililkliiil'
input_3_2 = 'ijiiijijjjiii' # rng
input_3_3 = 'klkkkjkk'
input_3_4 = 'iiiisisikksks' + 'jlsisssiisiilsji' #maybe rng
input_4_1 = 'lkkkllkklklkkllli' # can have bat rng
input_4_2 = 'kkjkkkllklllllll' + 'klljikij' # can have sarc rng. works except rider spawns I think
input_4_3 = 'jiijjjjiiiiijjijj' # can have sarc rng really bad
input_4_4 = 'iiiiiikkiikiilkiiisiis' # coral riff teleport rng
input_5_1 = 'jjjjjjjkjklkikkjjsjjs'
input_5_2 = 'iiijjjjiiiijjjjiiii'
input_5_3 = 'kkkkjjjjjjjjjjkiijjjjl'
input_5_4 = 'iiiiiiwlqilk' # KC rng

total_input = [input_1_1, input_1_2, input_1_3, input_1_4, input_2_1, input_2_2, input_2_3, input_2_4, input_3_1, input_3_2, input_3_3, input_3_4, input_4_1, input_4_2, input_4_3, input_4_4, input_5_1, input_5_2, input_5_3, input_5_4]
#######################################################

threshold = 400000000
target = cv2.imread('target.png', cv2.IMREAD_COLOR)
meth = 'cv2.TM_CCOEFF'
method = eval(meth)

# shopkeeper sequence values
threshold_shopkeeper = 85000000
shopkeeper = cv2.imread('shopkeeper.png', cv2.IMREAD_COLOR)
bard = cv2.imread('bard.png', cv2.IMREAD_COLOR)
h,w = shopkeeper.shape[:2]

# coral riff sequence values
threshold_coralriff = 65000000
coralriff = cv2.imread('coralriff.png', cv2.IMREAD_COLOR)


def brightness_sensor() -> int :
    count = 0

    while 1:
        # Get a screenshot and convert color.
        #  - screenshots only 3rd quarter for performance
        pic = pyautogui.screenshot(region=(0, y/2, x/2, y))
        img_frame = np.array(pic)
        img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)

        # Find "SEEDED" with cv2.matchTemplate
        res = cv2.matchTemplate(target, img_frame, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > threshold or count == 0:
            # Debug purpose
            count = count + 1
            cropped_frame = img_frame[0:540].copy()
            cv2.imshow("Threshold Debug", cropped_frame)
            print(max_val)

            if count != 1 :
                break

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

    return 0

# Designed for blood shop kills because of tons of rng.
#  - works only on specific seed '641499'. modify when needed.ji
#  - works only on specific resolution (1920x1080) and screen multiplier x4 with full-screen mode.
def shopkeeper_sequence() :
    time.sleep(0.02) # 1 frame later for consistency
    while 1:
        pic = pyautogui.screenshot(region=(x/4,y/4,x,y)) # image detecter couldn't tell the difference of shopkeeper and coins lol
        img_frame = np.array(pic)
        img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("Threshold Debug", img_frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

        # Find bard
        #res = cv2.matchTemplate(bard, img_frame, method)
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #top_left = max_loc
        # Debug purpose
        #print("bard : ", top_left)
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(img_frame, top_left, bottom_right, (0, 255, 0), 2)
        #cv2.imshow("Threshold Debug", img_frame)
        #

        # Finding bard had issues when the health bar of the shopkeeper was above bard.
        bard_pos = (420,257)

        # Find shopkeeper
        res = cv2.matchTemplate(shopkeeper, img_frame, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        if max_val > threshold_shopkeeper :
            # Debug purpose
            #cv2.rectangle(img_frame, top_left, bottom_right, (0,255,0), 2)
            #cv2.imshow("Threshold Debug", img_frame)
            #print(top_left)
            #

            # convert max_loc to Necrodancer block coordinates (bard position : 0,0)
            converted_coord = [ top_left[0] - bard_pos[0], top_left[1] - bard_pos[1] ]
            print("converted top left : ", converted_coord)

            for i in [0,1] :
                if converted_coord[i] % 100 < 50 :
                    converted_coord[i] = converted_coord[i] // 100
                else :
                    converted_coord[i] = converted_coord[i] // 100 + 1

            print("converted coordinates : ", converted_coord)

            # Hard-coded movement sequence. After this sequence bard will end up above the travel rune outside.
            sequence = ''
            failsafe = 3

            #if converted_coord == [2,1] or converted_coord == [4,1]:
            #    time.sleep(60)

            while ( converted_coord[0] * converted_coord[1] != 0 and converted_coord != [3,4] and converted_coord != [1,1] ) :
                if failsafe == 0:
                    print("Failsafe detected!")
                    break
                sequence += 'i' # Press up for missedbeat
                converted_coord[0] = converted_coord[0] - 1
                converted_coord[1] = converted_coord[1] - 1
                failsafe -= 1
            if converted_coord == [0,5] :
                sequence += 'i'
                converted_coord[1] = converted_coord[1] - 1

            if converted_coord == [1,0] :
                sequence += 'kisllkkk'
            elif converted_coord == [2,0] :
                sequence += 'lslkkkkk'
            elif converted_coord == [3,0] :
                sequence += 'lksikk'
            elif converted_coord == [0,1] :
                sequence += 'ljksikk'
            elif converted_coord == [0,2] :
                sequence += 'ksllkkkk'
            elif converted_coord == [0,3] :
                sequence += 'ksllkkk'
            elif converted_coord == [0,4] :
                sequence += 'kslljkkl'
            elif converted_coord == [1,1] :
                sequence += 'ljksjikk'
            elif converted_coord == [3,4] :
                sequence += 'lksjjkkk'
            else :
                print("There is no matching converted coord. current converted coord : ", converted_coord)
                continue # attempt one more time

            print("shopkeeper sequence : ", sequence)
            pyautogui.write(sequence, interval=default_interval)
            break

# Designed for coral riff rngs
#  - wip
def coralriff_sequence():
    time.sleep(0.02)  # 1 frame later for consistency
    while 1:
        pic = pyautogui.screenshot(region=(0,y/2,x/2,y))
        img_frame = np.array(pic)
        img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)
        # cv2.imshow("Threshold Debug", img_frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

        # Find coral riff
        res = cv2.matchTemplate(coralriff, img_frame, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        if max_val > threshold_coralriff:
            # Debug purpose
            cv2.rectangle(img_frame, top_left, bottom_right, (0,255,0), 2)
            cv2.imshow("Threshold Debug", img_frame)
            print(max_val, top_left)
            #

            # Hard-coded movement sequence. After this sequence bard will end up above the travel rune outside.
            sequence = ''

            #print("coral riff sequence : ", sequence)
            # pyautogui.write(sequence, interval=default_interval)
            # break

# Designed for rngs
#  - Human will manually kill deathmetal after their first hit.
#  - should de-activate when bard is next to black chest
def manual_mode() :
    while 1:
        if keyboard.is_pressed(manual_mode_exit) :
            break


def TAS():
    current_zone = 1
    z5_latency = 0

    print(" Do not input the seed prior. TAS will start in 5 seconds. ")
    time.sleep(5)

    # Seed input sequence. Default input for seed is 0.2 seconds
    pyautogui.write(seed, interval=0.2)
    pyautogui.press('enter')

    for input_sequence in total_input :
        # Debug purpose - if any empty sequences exist, break
        if len(input_sequence) == 0 :
            break

        # Wait loading
        brightness_sensor()

        # TAS-ing
        print(input_sequence)
        pyautogui.write(input_sequence, interval = default_interval + z5_latency)

        # shopkeeper sequence
        if current_zone == 2 :
            shopkeeper_sequence()
            post_shopkeeper_sequence = 'isllllkkkkjkkjkjkjjjkiiljiksjs'
            print(post_shopkeeper_sequence)
            pyautogui.write(post_shopkeeper_sequence, interval = default_interval)

        # deathmetal rng
        if current_zone == 4 :
            manual_mode()
            post_deathmetal_sequence = 'jjksjkks'
            print(post_deathmetal_sequence)
            pyautogui.write(post_deathmetal_sequence, interval = default_interval)

        # 2-2 bat rng
        if current_zone == 6 :
            manual_mode()

        #if current_zone == 9 :
            #threshold = 350000000

        # 3-2 bat rng
        if current_zone == 10 :
            manual_mode()

        # coral riff sequencejjl
        #if current_zone == 12 :
        #   coralriff_sequence()

        #if current_zone == 13 :
            #threshold = 400000000

        if current_zone == 13 :
            z5_latency = 0.03

        if current_zone == 14 :
            z5_latency = 0

        if current_zone == 15 :
            manual_mode()

        if current_zone == 16 :
            z5_latency = 0.03

        # Wait trapdoors (2.1 seconds)
        if input_sequence[ len(input_sequence) - 1 ] == 't' :
            time.sleep(2)
        else :
            time.sleep(0.1)

        current_zone += 1

    print(" TAS ended. ")

# Main

TAS()