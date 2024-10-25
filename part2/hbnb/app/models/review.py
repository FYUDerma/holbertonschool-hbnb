from app.models.base import BaseModel


class Review(BaseModel):
    """
    Class representing a review of a place.
    """

    def __init__(self, text, rating, place_id, user_id):
        """
        Initialize a review.
        """
        super().__init__()

        self.validate(text, rating, place, user)
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @staticmethod
    def validate(text, rating, place, user):
        """
        Validate review data.
        """
        if len(text) > 1024:
            raise ValueError('Text length exceeds 1024 characters')

        if rating is None or rating < 0 or rating > 5:
            raise ValueError('Rating must be between 0 and 5')

        if not place:
            raise ValueError('Place must be provided')

        if not user:
            raise ValueError('User must be provided')
