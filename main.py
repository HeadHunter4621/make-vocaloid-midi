import random
from midiutil import MIDIFile

# Works in vocaloid 4 I think (haven't tested lol)

kanaReclist = "ka ki ku ke ko kya kyu kye kyo ga gi gu ge go gya gyu gye gyo sa si su se so sha shi shu she sho za zi zu ze zo ja ji ju je jo ta ti tu te to cha chi chu che cho tsa tsi tsu tse tso. da di du de do na ni nu ne no nya nyu nye nyo ha hi hu he ho hya hyu hye hyo fa fi fu fe fo ba bi bu be bo bya byu bye byo pa pi pu pe po pya pyu pye pyo ma mi mu me mo mya myu mye myo ya yu ye yo ra ri ru re ro rya ryu rye ryo wa wi we wo va vi vu ve vo a i u e o n br1 br2 br3 br4 br5 Sil -"
allKana = kanaReclist.split(" ")
vowels = ["a", "i", "u", "e", "o", "n", "Sil", "Sil", "-", "-", "X", "X"]

def genMIDI(minPitch, maxPitch, totalNotes):

    possibleDuration = [0.125, 0.25, 0.333, 0.5, 0.5, 0.75, 1, 1.5, 2, 3, 4]
    track = 0
    time = 0
    tempo = 60
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard

    midiFile = MIDIFile(1)
    midiFile.addTempo(track,time,tempo)

    for i in range(0, totalNotes):
        noteDuration = possibleDuration[random.randrange(0,10)]
        midiFile.addNote(track, channel, random.randrange(minPitch, maxPitch), time, noteDuration, volume)
        time += noteDuration

    with open("output.mid", "wb") as midi_output:
        midiFile.writeFile(midi_output)

def genLyrics(amount):
    kanaOutList = []
    for i in range(0, amount):
        number = random.randrange(1,10)
        if number <= 2:
            selectedKana = vowels[random.randrange(0,11)]
        else:
            selectedKana = allKana[random.randrange(0,142)]
        kanaOutList.append(selectedKana)
    kanaOutString = " ".join(kanaOutList)

    with open("lyrics.txt", "w") as lyric_output:
        lyric_output.write(kanaOutString)

def main(totalNotes):
    genMIDI(40,67,totalNotes)
    genLyrics(totalNotes)

main(3000)