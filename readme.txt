Bard seeded TAS made by Shortcake Sweets.

 Please use this TAS when your run is guaranteed to NOT SUBMIT on leaderboards.
  - you can use mods (such as changing xml without making any seed-variences)
    for disabling leaderboard submits

 This runs on python. You should install "cv2, pyautogui, numpy, time" before running.

 input_1_1 to input_5_4 are sequences of each zone's inputs.
  - If the sequence has 't' at the end, it means the sequence will use trapdoors to exit the zone.
  - Some inputs are not complete because of shopkeeper (especially blood shop) rngs.
    These are handled in TAS() and shopkeeper_sequence().


About functions

brightness_sensor() checks your screen and "target.png" to check if loading is complete,
 thus handles TAS() to not mash buttons before your loading is complete.

shopkeeper_sequence() is a specialized code for bloodshop rngs.
 After you bomb the shopkeeper, it calculates shopkeeper's relative coordinate from bard
 and execute the hard-coded sequence in the code.

TAS() is the main function of this run. It executes the hard-coded sequences, and interactes with
 brightness_sensor() and shopkeeper_sequence().

 for stablized runs, TAS() uses trapdoor latency for 2 seconds and normal stair latency for 0.2 seconds.
 you will need these latency when your default_interval of inputs is small.

How to use this TAS()
 * This TAS runs on full-screen, screen multiplier x4, and 'show boss intro' option should be disabled.

 1. On the code, there is a User Input section. You should enter seed & inputs before running
 2. Select character Bard and go to seeded-allzones
 3. Do not enter the seed and leave it blank. Run the code and it will give you 5 seconds for you to refocus
    Necrodancer game in screen.

 After that TAS will enter seed and sequences automatically. good luck!