class Movie:
    """Movie detail information and representation class."""

    def __init__(self, title, poster_image_url, trailer_youtube_url, storyline):
        """Initialize Movie class.

        Args:
            title: The movie title.
            poster_image_url: URL to the poster image.
            trailer_youtube_url: URL to trailer on the youtube.com.
            storyline: Short plot description.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
