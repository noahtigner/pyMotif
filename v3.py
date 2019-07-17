# from mido import MidiFile, Message, MidiTrack
import mido
import os
import intervals
from Utilities.utilities import print_error, print_warning, print_success


# def beats_to_ticks(seconds, bpm):
#     seconds_per_beat = 1 / (bpm / 60)   # 120bpm / 60s = 2bps = 1/2spb
#     ticks_per_beat = 480                # precision
#     tempo = mido.bpm2tempo(bpm)         # microseconds per beat
#     return mido.second2tick(seconds_per_beat, ticks_per_beat, tempo)

def beats_to_ticks(seconds, bpm):
    # FIXME: shit is broke2
    # 120 beats / min
    # 120 / 60 = 2 bps
    ticks_per_beat = 480                # precision
    # seconds_per_beat = 2 * seconds
    seconds_per_beat = 1 / (bpm / 60)   # 120bpm / 60s = 2bps = 1/2spb
    tempo = mido.bpm2tempo(bpm)         # microseconds per beat
    return mido.second2tick(seconds_per_beat, ticks_per_beat, tempo)

def ticks_to_beat(ticks, bpm):
    ticks_per_beat = 480                # precision
    tempo = mido.bpm2tempo(bpm)         # microseconds per beat
    ticks_to_seconds = mido.tick2second(ticks, ticks_per_beat, tempo)
    return   ticks_to_seconds * 2



# TODO: MIDIFile
class MIDIFile(mido.MidiFile):
    def __init__(self, file_name, file_type=1, overwrite=False):
        self.file_name = file_name

        if os.path.isfile(self.file_name) and not overwrite:
            self.obj = mido.MidiFile(file_name, type=file_type)
        else:
            self.obj = mido.MidiFile(type=file_type)

    def __getattr__(self, name):
        func = getattr(self.__dict__['obj'], name)
        if callable(func):
            def wrapper(*args, **kwargs):
                # print("entering")
                # ret = func(*args, **kwargs)
                # print("exiting")
                # return ret
                return func(*args, **kwargs)
            return wrapper
        else:
            return func

    def save(self):
        self.obj.save(self.file_name)

    def print_midi(self):
        for i, track in enumerate(self.tracks):
            print('{}: Track {}:'.format(self.file_name, i))
            # print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.type == 'note_on':
                    print("    + {}".format(msg))
                elif msg.type == 'note_off':
                    print("    - {}".format(msg))

    

    def parse_midi(self):
        """
        Returns a list of notes in a given file.
        """
        # FIXME: Durations
        # FIXME: Harmonies (stack notes)


        midi = []
        for i, track in enumerate(self.tracks):
            print('{}: Track {}:'.format(self.file_name, i))

            for j, msg in enumerate(track):
                if msg.type == 'note_on':

                    # Find Duration
                    duration = 0
                    for k in range(j, len(track)):
                        if track[k].type == 'note_off' and track[k].note == msg.note:
                            duration = track[k].time - msg.time
                            break
                    print("    Note: {} Velocity: {} Duration: {}".format(msg.note, msg.velocity, duration))



                    
                    





                # msg = str(msg)
                # print(msg)
                # if "note_on" in msg and "signature" not in msg:
                #     mess = msg.split(" ")
                #     note = int(mess[2][5:])
                #     velocity = int(mess[3][9:])
                #     midi.append((intervals.NOTEMAP[note], velocity))
                #     # print(intervals.NOTEMAP[note])
                #     # print("note: {}".format())
                
                
        return midi

    

# TODO: MIDITrack



# TODO: MIDINote ???

if __name__ == "__main__":
    # mid = mido.MidiFile(type=0)
    # track = mido.MidiTrack()
    # mid.tracks.append(track)

    # track.append(mido.Message('note_on', note=64, velocity=60, time=0))
    # track.append(mido.Message('note_off', note=64, velocity=60, time=0))

    # mid.save('a.mid')

    mid = MIDIFile('x.mid', overwrite=True)
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.Message('note_on', note=64, velocity=60, time=0))
    track.append(mido.Message('note_off', note=64, velocity=60, time=32))

    # print(mid.tracks)

    mid.save()
    mid.print_midi()
    print("\n")
    mid.parse_midi()

    # mid.print_midi()

    # m = MIDIFile('x.mid', overwrite=True)
    # m.print_midi()
    # print("\n")
    # m.parse_midi()
    # m.save()

    # print_error("yeet")
    print_warning(beats_to_ticks(1, 120))
    print_warning(ticks_to_beat(beats_to_ticks(1, 120), 120))

    print_warning(ticks_to_beat(beats_to_ticks(2, 120), 120))
    print(mid.ticks_per_beat)

    
