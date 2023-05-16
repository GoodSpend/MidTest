from django.db import models

TYPE_CHOICES = [
    ('Pinjaman', 'Tagihan'),
]

class Data(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.TextField()
    description = models.TextField()