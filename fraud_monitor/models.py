from django.db import models

class FraudMonitor(models.Model):
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    class Meta:
        ordering = ["-my_field_name"]

    def __str__(self):
        return self.my_field_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])
