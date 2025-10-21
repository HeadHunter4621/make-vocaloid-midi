import random
from midiutil import MIDIFile

# Works in vocaloid 4 I think (haven't tested lol)

kanaReclist = "ka ki ku ke ko kya kyu kye kyo ga gi gu ge go gya gyu gye gyo sa si su se so sha shi shu she sho za zi zu ze zo ja ji ju je jo ta ti tu te to cha chi chu che cho tsa tsi tsu tse tso da di du de do na ni nu ne no nya nyu nye nyo ha hi hu he ho hya hyu hye hyo fa fi fu fe fo ba bi bu be bo bya byu bye byo pa pi pu pe po pya pyu pye pyo ma mi mu me mo mya myu mye myo ya yu ye yo ra ri ru re ro rya ryu rye ryo wa wi we wo a i u e o n -"
allKana = kanaReclist.split(" ")
vowels = ["a", "i", "u", "e", "o", "n", "-"]

def genMIDI(minPitch, maxPitch, totalNotes):
    noteDurations = [0.25, 0.5, 0.75, 1, 2, 4]
    restDurations = [0.25, 0.5, 0.75, 1, 2, 4, 6]
    track = 0
    time = 0
    tempo = 120
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
            random.randrange(minPitch, maxPitch),
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


def main(totalNotes):
    genMIDI(40, 67, totalNotes)
    genLyrics(totalNotes)


main(1200)

# Pitches!
# V1 Kaito              [?-?] []
# V1 Meiko              [?-?] []
# V2 Gakupo         *   [A1-C4] []
# V2 Len A2             [D3-C#5] []
# V2 Luka           *   [D3-D5] []
# V2 Piko               [C3-B4] []
# V2 Rin A2             [F#3-C#5] []
# V2 VY1                [F2-E4] []
# V3 Galaco Blue        [F2-G4] []
# V3 Galaco Red         [F2-G4] []
# V3 Lily               [D2-D4] []
# V3 vFlower            [F#2-F#4] []
# V3 VY2            *   [A1-G3] []
# V4 Fukase             [F2-A3] []
# V4 Kaai Yuki          [F2-C4] []
# V4 Megpoid            [F2-A4] []
# V4 Una Spicy          [D2-C5] []
# V4 Una Sugar          [D2-C5] []
# V4 SF-A2 Miki         [E2-G4] []
# V4X Miku              [A2-E4] []