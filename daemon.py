import Pyro5.api
import logging
from multiprocessing import Process
from subprocess import Popen, PIPE

logging.basicConfig(level=logging.DEBUG)

from librespot.core import Session
from librespot.metadata import TrackId, PlaylistId
from librespot.audio.decoders import AudioQuality, VorbisOnlyAudioQuality
from librespot.audio import PlayableContentFeeder

class PulseDaemon():
    def __init__(self):
        self.session: Session = None
        self.stdin_keys: list = []


    def authenticate(self, username: str, password: str):
        self.session = Session.Builder().user_pass(username, password).create()
        self.session.connect()

    def play_song(self, track_id: TrackId):
        stream = (
            self.session.content_feeder()
            .load(
                track_id,
                VorbisOnlyAudioQuality(
                    AudioQuality.VERY_HIGH
                ),
                False
            )
        )
        # Create a new process to play the song, so we can return to the main loop
        # and keep listening for new commands
        def _stream(stream: PlayableContentFeeder.LoadedStream.input_stream):
            ffplay = Popen(
                ['ffplay', '-nodisp', '-autoexit', '-'],
                stdin=PIPE
            )
            while True:
                data = stream.input_stream.read(4096)
                if not data:
                    break
                ffplay.stdin.write(data)
            ffplay.stdin.close()
            ffplay.wait()
        Process(target=_stream).start()


    def pause(self):
        pass

    def stop(self):
        pass
