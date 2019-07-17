import mido
from mido import MidiFile, Message, MidiTrack
import random
from intervals import second, third, fourth, fifth, sixth, seventh, octave, INTERVALS
from midi import print_midi, get_notes, beats_to_ticks, add_note, rm_note, batch_notes, parse_midi
import argparse
from pathlib import Path

track = MidiTrack()

def first_species(notes):
    # notes = get_notes(file)
    queue = [[[notes[i][0]], notes[i][1], ''] for i in range(len(notes))]

    # # Begin:        1, 5, or 8
    first = notes[0][0]
    rand = random.choice([fifth(first), octave(first)])
    # rand2 = random.choice([octave(first), 12 + third(first)])
    queue[0] = [[first, rand], notes[0][1], '']

    # # NO more than 12 (octave + 5th)
    # # No unisions in the middle
    # # No P5->P5
    # # No P5->P12 / P12->P5
    # # No P8->P8
    # # No more than 3 of the same imperfect consonance in a row
    prev = 'fifth'
    for i in range(1, len(notes)-2):
        # print("here")
        n = notes[i][0]
        # print(n)
        # interval = random.choice([third(n), fourth(n), fifth(n), sixth(n)])
        possible = ['third', 'fourth', 'fifth', 'sixth']
        while True:
            interval = random.choice(possible)

            if interval == 'fifth' and prev == 'fifth':
                continue
            elif interval == 'octave' and prev == 'fifth':
                continue
            elif interval == 'fifth' and prev == 'octave':
                continue
            elif interval == 'octave' and prev == 'octave':
                continue

            # any large leaps (fourth or larger) are followed by step in opposite direction
            # if prev == 'third' and interval == 'sixth':
            #     possible = ['fourth', 'fifth']
            #     continue
            # elif prev == 'octave' and (interval == 'fourth' or interval == 'fifth'):
            #     possible = ['third', 'sixth']

            # FIXME:
            # elif queue[i-1][0][1] > INTERVALS[interval](n) + 6:
            #     print("jump 1")
            #     continue
            # elif queue[i-1][0][1] < INTERVALS[interval](n) - 6:
            #     print("jump 2")
            #     continue

            if queue[i-2][2] == queue[i-1][2] and queue[i-1][2] == interval:
                continue
            


            break
                
        # if interval == 
        inter = str(interval)
        # print("Int: {}".format(inter))
        interval = INTERVALS[interval](n)

        queue[i] = [[n, interval], notes[i][1], inter]



    # # Penultimate:  3 or 6
    penultimate = notes[-2][0]
    rand = random.choice([third(penultimate)])
    queue[-2] = [[penultimate, rand], notes[-2][1], 'third']

    # # End:          1, or 8
    ultimate = notes[-1][0]
    # rand = random.choice([ultimate, octave(ultimate)])
    queue[-1] = [[ultimate], notes[-1][1], 'unison']


    # for i in range(len(queue)):
    #     print(queue[i])
    
    #     batch_notes(queue[i][0], queue[i][1], 0, 1)
    return queue



if __name__ == "__main__":
    # test = MidiFile('test1.mid')
    # print_midi(test)

    
    mid = MidiFile()
    # t = MidiTrack()
    
    

    # t.append(Message('program_change', program=12, time=0))
    # t.append(Message('note_on', note=59, velocity=64, time=0))
    # t.append(Message('note_off', note=59, velocity=64, time=beats_to_ticks(2)))
    track.append(Message('program_change', program=12, time=0))

    # test = MidiFile('test3.mid')
    # # notes = get_notes(test)
    # # fscp = first_species(notes)

    # # for i in range(len(fscp)):
    # #     print(fscp[i])
    
    # #     batch_notes(fscp[i][0], fscp[i][1], 0, 1)

    # # mid.save('new_song.mid')
    
    # test = MidiFile('new_song.mid')
    # notes = get_notes(test)
    # first_species(notes)
    # mid.save('new_song.mid')

    # test = MidiFile('test1.mid')
    # get_notes(test)


    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("file_path", type=Path)

        p = parser.parse_args()
        # print(p.file_path, type(p.file_path), p.file_path.exists())
        if not p.file_path.exists():
            raise Exception('FileNotFoundError')
        path = str(p.file_path)
    except:
        print("Failed to open file.\nUsing default file instead.")
        path = "test1.mid"

    midi_file = MidiFile(path)
    notes = get_notes(midi_file)
    fscp = first_species(notes)

    for i in range(len(fscp)):
        print(fscp[i])
    
        batch_notes(track, fscp[i][0], fscp[i][1], 0, 1)


    mid.tracks.append(track)
    mid.save('new_song.mid')

    test = MidiFile('new_song.mid')
    # print_midi(test)
    print(*parse_midi(test), sep = "\n")
    # print(get_notes(test))


