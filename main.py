import random
from midiutil import MIDIFile
import numpy as np

# Works in vocaloid 4 I think (haven't tested lol)

kanaReclist = "ka ki ku ke ko kya kyu kye kyo ga gi gu ge go gya gyu gye gyo sa si su se so sha shi shu she sho za zi zu ze zo ja ji ju je jo ta ti tu te to cha chi chu che cho tsa tsi tsu tse tso da di du de do na ni nu ne no nya nyu nye nyo ha hi hu he ho hya hyu hye hyo fa fi fu fe fo ba bi bu be bo bya byu bye byo pa pi pu pe po pya pyu pye pyo ma mi mu me mo mya myu mye myo ya yu ye yo ra ri ru re ro rya ryu rye ryo wa wi we wo a i u e o n -"
allKana = kanaReclist.split(" ")
vowels = ["a", "i", "u", "e", "o", "n", "-"]

def genNotes(minPitch, maxPitch, totalNotes):
    mean = round((maxPitch - minPitch) / 2)
    range = round(((maxPitch - mean) + (mean + minPitch)) / 2)
    amount = totalNotes


    dirty_array = np.array(np.random.normal(mean,range,amount))

    dirty_array[dirty_array > 127] = 127 # Set to 127 if above 127
    dirty_array[dirty_array <   0] = 0   # Set to 0 if below 0


    note_array = [round(pitch) for pitch in dirty_array]
    return note_array

def genMIDI(note_array, totalNotes):
    noteDurations = [0.25, 0.5, 0.75, 1, 2, 4, 8]
    restDurations = [      0.5, 0.75, 1, 2, 4   ]
    track   = 0
    time    = 0
    tempo   = 120
    channel = 0

    restChance = 0

    outputTrack = MIDIFile(1)
    outputTrack.addTempo(track, time, tempo)

    for i in range(0, totalNotes): # every note

        lorq = random.randrange(0,9)
        if lorq <= restChance:
            volume = 0
            duration = restDurations[random.randrange(0,len(restDurations))]
            restChance = 0
        else:
            volume = 100
            duration = noteDurations[random.randrange(0,len(noteDurations))]
            restChance += 1

        outputTrack.addNote(
            track,
            channel,
            note_array[i],
            time,
            duration,
            volume
        )
        time += duration

    with open("output.mid", "wb") as midi_output:
        outputTrack.writeFile(midi_output)


def genLyrics(amount):
    kanaOutList = []
    for i in range(0, amount):
        number = random.randrange(1, 10)
        if number <= 2:
            selectedKana = vowels[random.randrange(0, len(vowels))]
        else:
            selectedKana = allKana[random.randrange(0, len(allKana))]
        kanaOutList.append(selectedKana)
    kanaOutString = " ".join(kanaOutList)

    print(kanaOutString)


def main(minPitch, maxPitch, totalNotes):
    genNotes(minPitch, maxPitch, totalNotes)
    # print(genNotes(minPitch, maxPitch, totalNotes))
    #print(genLyrics(totalNotes))

main(36, 48, 1200)

# Pitch math
# Curve?
#   import numpy as np
#   random_numbers_array = np.random.normal(loc, scale, size)
#   mean = ((maxPitch + minPitch) / 2).round(0)
#   range = (maxPitch - minPitch)    # Deviation (keep average in range)
#   amount = totalNotes
# V1 Kaito:
#   Optimal range:
#     Low:   C2 (36)
#     Mean: F#2 (42)
#     High:  C3 (48)