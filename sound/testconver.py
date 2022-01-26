song reverse
from pydub.playback import play
from pydub import AudioSegment
song = AudioSegment.from_wav("tbz3.wav")
backwards = song.reverse()
play(backwards)
