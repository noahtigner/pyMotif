import mido
from mido import MidiFile, Message, MidiTrack

# Create Midi Message
# ----------------------------------------------------------------
msg = mido.Message('note_on', note=60)
print(msg.type)
print(msg.note)


# Read Midi File
# ----------------------------------------------------------------
mid = MidiFile('test1.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)


# Midi Messages
# ----------------------------------------------------------------
"""
note_on channel=0 note=59 velocity=57 time=0

note_on / note_off
channel
note (59 = B)
velocity

The time attribute of each message is the number of seconds since 
the last message or the start of the file.
"""

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('new_song.mid')


# You can use tick2second() and second2tick() to convert 
# to and from seconds and ticks. Note that integer rounding 
# of the result might be necessary because MIDI files require ticks to be integers.

# You can use bpm2tempo() and tempo2bpm() to convert to and 
# from beats per minute. Note that tempo2bpm() may return a floating point number.
# The default tempo is 500000 microseconds per beat, which is 120 beats per minute. 
# The meta message ‘set_tempo’ can be used to change tempo during a song.

