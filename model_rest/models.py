from django.db import models

# Create your models here.
'''
OPId       | int(11)     | NO   | PRI | NULL    | auto_increment |
| DeviceId   | varchar(50) | YES  |     | NULL    |                |
| LocationId | int(11)     | YES  |     | NULL    |                |
| ShiftId    | int(11)     | YES  |     | NULL    |                |
| Temp       | double      | YES  |     | NULL    |                |
| Humidity   | double      | YES  |     | NULL    |                |
| TimeStamp  | timestamp   | YES  |     | NULL    |                |
| Extra1     | varchar(50) | YES  |     | NULL    |                |
| Extra2     | varchar(50) | YES  |     | NULL    |                |
| Extra3     | double      | YES  |     | NULL    |                |
| Extra4     | double      | YES  |     | NULL    |                |
| SensorId   | varchar(50) | YES  |     | NULL
'''

class operational_parameter(models.Model):
    OPId = models.IntegerField()
    DeviceId = models.CharField(max_length=60)
    LocationId = models.IntegerField()
    ShiftId = models.IntegerField()
    Temp = models.DecimalField(max_digits=10,decimal_places=2)
    Humidity = models.DecimalField(max_digits=10, decimal_places=2)
    TimeStamp = models.DateTimeField()
    SensorId = models.CharField(max_length=60)

    class Meta:
        db_table = 'operationalparameter'

