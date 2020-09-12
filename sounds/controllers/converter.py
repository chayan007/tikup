"""Convert video to audio instance."""
import os
import pipes


class AudioConverter:
    """Convert to audio."""

    def __init__(self):
        """Declare all class variables."""
        self.file_name = ''

    @staticmethod
    def audio_extractor(file_name):
        try:
            file, file_extension = os.path.splitext(file_name)
            file = pipes.quote(file)
            video_to_wav = 'ffmpeg -i {}{} {}.wav'.format(
                file,
                file_extension,
                file
            )
            final_audio = 'lame {}.wav {}.mp3'.format(
                file,
                file
            )
            os.system(video_to_wav)
            os.system(final_audio)
            # file=pipes.quote(file)
            # os.remove(file + '.wav')
        except OSError as err:
            print(str(err))
