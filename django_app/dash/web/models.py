from django.db import models

# Create your models here.
class FamilyTree(models.Model):

    MALE = 1
    FEMALE = 2

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=MALE)
    parent = models.ForeignKey('FamilyTree', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        name = "-" if not self.name else self.name
        return "{}".format(name)
    
    class Meta:
        db_table = "family_tree"
