import random
import numpy as np
from midiutil import MIDIFile


romaji_list = "ka ki ku ke ko kya kyu kye kyo ga gi gu ge go gya gyu gye gyo sa si su se so sha shi shu she sho za zi zu ze zo ja ji ju je jo ta ti tu te to cha chi chu che cho tsa tsi tsu tse tso da di du de do na ni nu ne no nya nyu nye nyo ha hi hu he ho hya hyu hye hyo fa fi fu fe fo ba bi bu be bo bya byu bye byo pa pi pu pe po pya pyu pye pyo ma mi mu me mo mya myu mye myo ya yu ye yo ra ri ru re ro rya ryu rye ryo wa wi we wo a i u e o n -"
all_kana = romaji_list.split(" ")
vowels = ["a", "i", "u", "e", "o", "n", "-"]


def add_phonemes(vowel, phoneme):
    if vowel:
        vowels.append(phoneme)
    else :
        all_kana.append(phoneme)


def generate_note_list(minPitch, maxPitch, totalNotes):
    mean = round((maxPitch + minPitch) / 2)
    range = round(((maxPitch - mean) + (mean + minPitch)) / 4)
    amount = totalNotes

    dirty_list = np.array(np.random.normal(mean,range,amount))

    dirty_list[dirty_list > 127] = random.randrange(0,127) # Set to 127 if above 127
    dirty_list[dirty_list <   0] = random.randrange(0,127)   # Set to 0 if below 0

    note_list = [round(pitch) for pitch in dirty_list]

    return note_list


def generate_midi(note_array, total_notes):
    noteDurations = [0.25, 0.5, 0.75, 1, 2, 4, 8]
    restDurations = [0.25, 0.5, 0.75, 1, 2, 4   ]
    track   = 0
    time    = 0
    tempo   = 120
    channel = 0

    restChance = 0

    outputTrack = MIDIFile(1)
    outputTrack.addTempo(track, time, tempo)


    for i in range(0, total_notes): # every note

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


def generate_lyrics(total_notes):
    kana_out_list = []
    for i in range(0, total_notes):
        number = random.randrange(1, 10)
        if number <= 2:
            selected_syllable = vowels[random.randrange(0, len(vowels))]
        else:
            selected_syllable = all_kana[random.randrange(0, len(all_kana))]
        kana_out_list.append(selected_syllable)
    kana_out_string = " ".join(kana_out_list)

    return(kana_out_string)



def main(min_pitch, max_pitch, total_notes):
    print(generate_note_list(min_pitch, max_pitch, total_notes))
    print(generate_lyrics(total_notes))


# add_phonemes()
main(36, 8, 3600)

# 3600 Notes ~ 1 Hour of data

# EXTRA PHONEMES!
# V1: in (inhale)
# Other: N/A