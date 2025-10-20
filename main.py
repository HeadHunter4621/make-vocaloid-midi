import random
from midiutil import MIDIFile

# Works in vocaloid 4 I think (haven't tested lol)

kanaReclist = "か き く け こ きゃ きゅ きぇ きょ が ぎ ぐ げ ご ぎゃ ぎゅ ぎぇ ぎょ さ すぃ す せ そ しゃ し しゅ しぇ しょ ざ ずぃ ず ぜ ぞ じゃ じ じゅ じぇ じょ た てぃ とぅ て と ちゃ ち ちゅ ちぇ ちょ つぁ つぃ つ つぇ つぉ. だ でぃ どぅ で ど な に ぬ ね の にゃ にゅ にぇ にょ は ひ ほぅ へ ほ ひゃ ひゅ ひぇ ひょ ふぁ ふぃ ふ ふぇ ふぉ ば び ぶ べ ぼ びゃ びゅ びぇ びょ ぱ ぴ ぷ ぺ ぽ ぴゃ ぴゅ ぴぇ ぴょ ま み む め も みゃ みゅ みぇ みょ や ゆ いぇ よ ら り る れ ろ りゃ りゅ りぇ りょ わ うぃ うぇ を ヴぁ ヴぃ ヴ ヴぇ ヴぉ あ い う え お ん br1 br2 br3 br4 br5 Sil -"
allKana = kanaReclist.split(" ")
vowels = ["あ", "い", "う", "え", "お", "ん", "Sil", "Sil", "-", "-", "X", "X"] # X will be deleted notes I think


def genMIDI(minPitch, maxPitch, totalNotes):
    possibleDuration = [0.125, 0.25, 0.333, 0.5, 0.5, 0.75, 1, 1.5, 2, 3, 4]
    track = 0
    time = 0
    tempo = 60
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard

    midiFile = MIDIFile(1)
    midiFile.addTempo(track, time, tempo)

    for i in range(0, totalNotes):
        noteDuration = possibleDuration[random.randrange(0, 10)]
        midiFile.addNote(
            track,
            channel,
            random.randrange(minPitch, maxPitch),
            time,
            noteDuration,
            volume,
        )
        time += noteDuration

    with open("output.mid", "wb") as midi_output:
        midiFile.writeFile(midi_output)


def genLyrics(amount):
    kanaOutList = []
    for i in range(0, amount):
        number = random.randrange(1, 10)
        if number <= 2:
            selectedKana = vowels[random.randrange(0, 11)]
        else:
            selectedKana = allKana[random.randrange(0, 142)]
        kanaOutList.append(selectedKana)
    kanaOutString = " ".join(kanaOutList)

    with open("lyrics.txt", "w") as lyric_output:
        lyric_output.write(kanaOutString)


def main(totalNotes):
    genMIDI(40, 67, totalNotes)
    genLyrics(totalNotes)


main(3000)
