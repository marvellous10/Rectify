from datetime import datetime
import datetime as dt
from mongoengine import *

class Feedback(Document):
    FEEDBACK_CHOICES = (
        ('Feature', 'Feature'),
        ('Other', 'Other'),
    )
    user_id = StringField()
    feedback_type = StringField(choices=FEEDBACK_CHOICES, default=FEEDBACK_CHOICES.FEATURE)
    feedback_text = StringField(min_length=10, max_length=512)
    created = DateTimeField(default=datetime.now(dt.UTC), auto_now_add=True, null=False, blank=False)
    
    meta = {'collection': 'Feedback'}
