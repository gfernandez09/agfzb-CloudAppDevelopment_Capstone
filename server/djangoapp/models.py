from django.db import models
from django.utils.timezone import now


# Car Make model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car')
   
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MINIVAN = 'Minivan'
    CUV = 'CUV'
    HATCHBACK = 'Hatchback'
    LIMOUSINE = 'Limousine'
    GETAWAYCAR = 'Getawaycar'
    FORMULA1 = 'Formula1'
    BATMOBILE = 'Batmobile'
    MACH5 = 'Mach5'
    SPORTS_CAR = 'Sports Car'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MINIVAN, 'Minivan'),
        (CUV, 'CUV'),
        (HATCHBACK, 'Hatchback'),
        (LIMOUSINE, 'Limousine'),
        (GETAWAYCAR, 'Getawaycar'),
        (FORMULA1, 'Formula1'),
        (BATMOBILE, 'Batmobile'),
        (MACH5, 'Mach5'),
        (SPORTS_CAR, 'Sports car')
    ]

    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data