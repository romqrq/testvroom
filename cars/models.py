from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    """Class for the car object"""

    CAR_CLASS_CHOICES = [
        ('Custom Classic', 'Custom Classic'),
        ('Luxury', 'Luxury'),
        ('Supersport', 'Supersport')
    ]
    YEAR_CHOICES = [(i, i) for i in range(1900, 2021)]
    TRACK_DAY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    ENGINE_TYPE_CHOICES = [
        ('Inline 3', 'Inline 3'),
        ('Inline 4', 'Inline 4'),
        ('Inline 6', 'Inline 6'),
        ('Boxer 4', 'Boxer 4'),
        ('Boxer 6', 'Boxer 6'),
        ('V6', 'V6'),
        ('V8', 'V8'),
        ('V10', 'V10'),
        ('V12', 'V12'),
        ('W10', 'W10'),
        ('W12', 'W12'),
        ('Other', 'Other')
    ]
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual')
    ]
    FUEL_CHOICES = [
        ('Diesel', 'Diesel'),
        ('Full Electric', 'Full Electric'),
        ('Hybrid', 'Hybrid'),
        ('Petrol', 'Petrol')
    ]
    PASSENGER_CHOICES = [(i, i) for i in range(1, 30)]
    DOORS_CHOICES = [(i, i) for i in range(1, 10)]
    ACCESSORIES_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Custom', 'Custom')
    ]
    CITY_CHOICES = [
        ('Dublin', 'Dublin'),
        ('Cork', 'Cork'),
        ('Galway', 'Galway')
    ]
    COUNTY_CHOICES = [
        ('Dublin', 'Dublin'),
        ('Cork', 'Cork'),
        ('Galway', 'Galway')
    ]
    COUNTRY_CHOICES = [('Ireland', 'Ireland')]

    car_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    car_class = models.CharField(max_length=40, choices=CAR_CLASS_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    year = models.DecimalField(max_digits=4,
                               decimal_places=0, choices=YEAR_CHOICES)
    track_day = models.CharField(max_length=40, choices=TRACK_DAY_CHOICES)
    engine_type = models.CharField(max_length=40,
                                   choices=ENGINE_TYPE_CHOICES)
    displacement = models.DecimalField(max_digits=4, decimal_places=1)
    transmission = models.CharField(max_length=20,
                                    choices=TRANSMISSION_CHOICES)
    fuel = models.CharField(max_length=50, choices=FUEL_CHOICES)
    passengers = models.DecimalField(max_digits=10,
                                     decimal_places=0,
                                     choices=PASSENGER_CHOICES)
    doors = models.DecimalField(max_digits=10,
                                decimal_places=0, choices=DOORS_CHOICES)
    accessories = models.CharField(max_length=20, choices=ACCESSORIES_CHOICES)
    city = models.CharField(max_length=30, choices=CITY_CHOICES)
    county = models.CharField(max_length=30,
                              choices=COUNTY_CHOICES,
                              blank=True)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    image1 = models.ImageField(upload_to='media/images')
    image2 = models.ImageField(upload_to='media/images', null=True)
    image3 = models.ImageField(upload_to='media/images', null=True)
    image4 = models.ImageField(upload_to='media/images', null=True)
    image5 = models.ImageField(upload_to='media/images', null=True)
    guidelines = models.TextField(max_length=500)

    def __str__(self):
        car_description = [str(self.year), str(self.brand), str(self.model)]
        return ' '.join(car_description)


class TrackDayAddon(models.Model):
    """Model to create instance of Track Day add on"""

    TRACK_CHOICES = [
        ('None', 'None'),
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Full Day', 'Full Day'),
    ]

    title = 'Track Day'
    coverage = models.CharField(max_length=40, choices=TRACK_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        track_day_description = [str(self.title), str(self.coverage)]
        return ' '.join(track_day_description)


class InsuranceAddon(models.Model):
    """Model to create instance of Insurance add on"""

    INSURANCE_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Full Coverage', 'Full Coverage'),
    ]

    title = 'Insurance'
    coverage = models.CharField(max_length=40, choices=INSURANCE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        insurance_description = [str(self.title), str(self.coverage)]
        return ' '.join(insurance_description)


class PrivateDriverAddon(models.Model):
    """Model to create instance of Private Driver add on"""

    PRIVATE_DRIVER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    title = 'Private Driver'
    coverage = models.CharField(max_length=40, choices=PRIVATE_DRIVER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        private_driver_description = [str(self.title), str(self.coverage)]
        return ' '.join(private_driver_description)
