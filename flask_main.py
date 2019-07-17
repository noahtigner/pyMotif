import flask
from flask import Flask, redirect, url_for, request, render_template, flash, session, send_file, send_from_directory
import config
import logging

import mido
from mido import MidiFile, Message, MidiTrack
import random
from intervals import second, third, fourth, fifth, sixth, seventh, octave, INTERVALS
from midi import print_midi, get_notes, beats_to_ticks, add_note, rm_note, batch_notes, parse_midi
from counterpoint import first_species



app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

track = MidiTrack()

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    # flash("Flash")
    return flask.render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

# @app.route('/file-downloads/')
# def file_downloads():
# 	try:
# 		return render_template('downloads.html')
# 	except Exception as e:
# 		return str(e)

@app.route('/cp')
def cp():
    mid = MidiFile()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    path = "test1.mid"

    midi_file = MidiFile(path)
    notes = get_notes(midi_file)
    fscp = first_species(notes)

    for i in range(len(fscp)):
        print(fscp[i])
    
        batch_notes(fscp[i][0], fscp[i][1], 0, 1)

    mid.save('new_song.mid')

    return redirect(url_for("show"))

@app.route('/download')
def return_files():
    try:
        # FIXME: change download name
        return send_from_directory('new_song.mid', 'new_song.mid',  as_attachment=True)

    except Exception as e:
        return str(e)

@app.route('/show')
def show():
    midi = parse_midi(MidiFile('new_song.mid'))
    result = {
        'Midi: ': midi
    }
    return flask.jsonify(result=result)


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

    mid = MidiFile()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))

    print("Failed to open file.\nUsing default file instead.")
    path = "test1.mid"

    midi_file = MidiFile(path)
    notes = get_notes(midi_file)
    fscp = first_species(notes)

    for i in range(len(fscp)):
        print(fscp[i])
    
        batch_notes(fscp[i][0], fscp[i][1], 0, 1)

    mid.save('new_song.mid')
