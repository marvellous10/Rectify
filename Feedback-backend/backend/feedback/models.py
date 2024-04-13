from mongoengine import *

class Feedback(Document):
    FEATURE = 'FT'
    OTHER = 'OT'
    FEEDBACK_CHOICES = {
        FEATURE: 'Feature',
        OTHER: 'Other'
    }
    user_id = StringField()
    feedback_type = StringField(default=FEEDBACK_CHOICES.FEATURE)
