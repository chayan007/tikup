"""Convert video to audio instance."""
import os
import pipes
import random
import time

from django.core.files import File

from posts.models import Post

from sounds.models import Sound


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
            output_file = '{}_{}'.format(
                file,
                random.randint(0, 999999)
            )
            video_to_wav = 'ffmpeg -i {}{} {}.wav'.format(
                file,
                file_extension,
                output_file
            )
            final_audio = 'lame {}.wav {}.mp3'.format(
                output_file,
                output_file
            )
            os.system(video_to_wav)
            os.system(final_audio)
            return '{}.mp3'.format(output_file)
        except OSError as err:
            print(str(err))

    def _add_to_sound(self, file_name, post):
        """Store audio to Sound model."""
        with open(file_name, 'rb') as fi:
            sound = Sound.objects.create(
                profile=post.profile,
                sound_file=File(fi, name=os.path.basename(fi.name)),
                is_extracted_audio=True
            )
            post.sound = sound
            post.save()

    def extract(self, post_uuid):
        """Extract audio from one post."""
        post = Post.objects.get(uuid=post_uuid)
        file_name = post.video_file.path
        audio_file_path = self.audio_extractor(file_name)
        time.sleep(1 * 60)
        self._add_to_sound(
            audio_file_path,
            post
        )
