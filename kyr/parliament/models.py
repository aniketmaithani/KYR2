from django.db import models
from versatileimagefield.fields import VersatileImageField
from uuid_upload_path import upload_to
from uuidfield import UUIDField


class MemberOfParliament(models.Model):
    name_of_the_mp = models.CharField(blank=False, null=False, max_length=256)
    state = models.CharField(blank=False, null=False, max_length=100, help_text='State to which MP Belongs')
    photo_of_the_mp = VersatileImageField(
        blank=True, null=True, upload_to=upload_to)
    constituency = models.CharField(blank=False, null=False, max_length=100, help_text='constituency of the mp')
    attendance_percent = models.DecimalField(max_digits=8, decimal_places=2)
    debates_total = models.IntegerField()
    no_of_questions_asked = models.IntegerField()
    private_member_bill_asked = models.IntegerField()
    unique_id = UUIDField(auto=True)

    def __str__(self):
        return self.name_of_the_mp

    class Meta:
        verbose_name = "MP"
        verbose_name_plural = "MPs"
        ordering = ['-name_of_the_mp']
