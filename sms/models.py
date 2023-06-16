from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class NoteSharing(models.Model):
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE)
    share_by = models.OneToOneField(User, on_delete=models.CASCADE,related_name="by")
    share_to = models.OneToOneField(User, on_delete=models.CASCADE,related_name="to")


