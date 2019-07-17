import mido
from mido import MidiFile, Message, MidiTrack
import intervals

# track = MidiTrack()

def print_midi(file_name):

    for i, track in enumerate(file_name.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)

def parse_midi(file_name):
    """
    Returns a list of notes in a given file.
    """
    # FIXME: Durations
    # FIXME: Harmonies (stack notes)


    midi = []
    for i, track in enumerate(file_name.tracks):
        for msg in track:
            # print(str(msg))
            msg = str(msg)
            print(msg)
            if "note_on" in msg and "signature" not in msg:
                mess = msg.split(" ")
                note = int(mess[2][5:])
                velocity = int(mess[3][9:])
                midi.append((intervals.NOTEMAP[note], velocity))
                # print(intervals.NOTEMAP[note])
                # print("note: {}".format())
    return midi

def get_notes(file_name):
    # FIXME: durations
    notes = []
    for i, track in enumerate(file_name.tracks):
        for msg in track:
            # print(str(msg))
            msg = str(msg)
            if "note_on" in msg and "signature" not in msg:
                mess = msg.split(" ")
                # for m in mess:
                #     print(m)
                # print(mess[2][5:])
                note = int(mess[2][5:])
                velocity = int(mess[3][9:])
                notes.append((note, velocity))
                # print("note: {}".format())
    return notes

def beats_to_ticks(seconds):
    # 120 beats / min
    # 120 / 60 = 2 bps
    beats = 2 * seconds
    return int(mido.second2tick(beats, 120, 500000))


def add_note(track, note, velocity, start):
    track.append(Message('note_on', note=note, velocity=velocity, time=beats_to_ticks(start)))

def rm_note(track, note, velocity, duration, batch_time=False):
    track.append(Message('note_off', note=note, velocity=velocity, time=beats_to_ticks(duration)))


def batch_notes(track, notes, velocity, start, duration):

    for note in notes:
        track.append(Message('note_on', note=note, velocity=velocity, time=beats_to_ticks(start)))
        if start > 0:
            start-=1

    # for note in notes:
    #     track.append(Message('note_off', note=note, velocity=velocity, time=beats_to_ticks(duration)))
    #     print(duration)
    #     if duration > 0:
    #         duration-=1

    # FIXME: notes might not be ending correctly
    for note in notes:
        track.append(Message('note_off', note=note, velocity=velocity, time=beats_to_ticks(duration)))
        print(duration)
        if duration > 0:
            duration-=1    

    