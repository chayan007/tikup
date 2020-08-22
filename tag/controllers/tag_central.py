"""Handle all tag related functions."""
from tag.models import Hashtag, HashtagLink


class TagCentral:
    """Handle all tag functions."""

    def extract_tags(self, post_description):
        """Extract all tag."""
        return set(
            part[1:] for part in post_description.split() if part.startswith('#')
        )

    def store_all_tags(self, tag):
        """Store all tags present in post description."""
        Hashtag.objects.create(
            name=tag
        )

    def link_all_tags_to_post(self, tag, post):
        """Link one tag to a post."""
        HashtagLink.objects.create(
            post=post,
            hashtag__name=tag
        )

    def handle_tag_cycle(self, post):
        """Handle all tags."""
        try:
            tags = self.extract_tags(post.description)
            for tag in tags:
                self.store_all_tags(tag)
                self.link_all_tags_to_post(tag, post)
            return True
        except BaseException as e:
            return False
