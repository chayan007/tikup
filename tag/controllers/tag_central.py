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
    def increment_tag_count(tag_obj):
        """Increment count of tag."""
        tag_obj.views += 1
        tag_obj.save()

    @staticmethod
    def store_tag(tag):
        """Store all tags present in post description."""
        try:
            Hashtag.objects.create(
                name=tag
            )
        except BaseException:
            return

    def link_all_tags_to_post(self, tag, post):
        """Link one tag to a post."""
        tag_obj = Hashtag.objects.get(name=tag)
        HashtagLink.objects.create(
            post=post,
            hashtag=tag_obj
        )
        self.increment_tag_count(tag_obj)

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
