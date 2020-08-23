"""Handle all tag related functions."""
from tag.models import Hashtag, HashtagLink


class TagCentral:
    """Handle all tag functions."""

    @staticmethod
    def extract_tags(post_description):
        """Extract all tag."""
        return set(
            part[1:] for part in post_description.split() if part.startswith('#')
        )

    @staticmethod
    def store_tag(tag):
        """Store all tags present in post description."""
        try:
            Hashtag.objects.create(
                name=tag
            )
        except BaseException:
            return

    @staticmethod
    def link_all_tags_to_post(tag, post):
        """Link one tag to a post."""
        HashtagLink.objects.create(
            post=post,
            hashtag=Hashtag.objects.get(name=tag)
        )

    def handle_tag_cycle(self, post):
        """Handle all tags."""
        try:
            tags = self.extract_tags(post.description)
            for tag in tags:
                self.store_tag(tag)
                self.link_all_tags_to_post(tag, post)
            return True
        except BaseException as e:
            return False
