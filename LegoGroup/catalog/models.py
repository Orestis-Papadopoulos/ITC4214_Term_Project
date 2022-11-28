from django.db import models
import uuid
#import smalluuid # need Internet to install this

# select-options correspond to dropdowns; e.g., category name (not id)

class LegoPart(models.Model):
    """
    Defines attributes of a Lego part.
    """

    part_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    part_name = models.CharField(max_length = 50, help_text = "Type part name")
    description = models.TextField(max_length = 1000, help_text = "Type part description (up to 1000 characters)", blank = True)
    part_image = models.ImageField()
    category_id = models.ForeignKey() # choices = CATEGORY_CHOICES
    subcategory_id = models.ForeignKey() # populate subcategories once category has been chosen ?
    public_access = models.BooleanField()

    def __str__(self):
        return self.part_name

    def get_absolute_url(self):
        pass

class User(models.Model):
    """
    Defines attributes of a user.
    """

    username = models.CharField(primary_key = True, max_length = 30, help_text = "Type username here")
    password = models.CharField(max_length = 20, help_text = "Type password here")
    first_name = models.CharField(max_length = 50, help_text = "Type first name here")
    last_name = models.CharField(max_length = 50, help_text = "Type last name here")
    email = models.EmailField(max_length = 100, help_text = "Type email here")
    user_image = models.ImageField()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass

class Category(models.Model):
    """
    Defines a lego part category.
    """

    BRICK = ''
    TECHNIC = ''
    ELECTRIC = ''

    CATEGORY_CHOICES = [
        (BRICK, 'Brick'),
        (TECHNIC, 'Technic'),
        (ELECTRIC, 'Electric'),
    ]

    category_id = models.CharField(max_length = 10, primary_key = True, choices = CATEGORY_CHOICES)
    category_name = models.CharField(unique = True, max_length = 50, help_text = "Type category name")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        pass

class Subcategory(models.Model):
    """
    Defines a lego part subcategory.
    """

    # Brick subcategories
    DECORATED = ''
    MODIFIED = ''
    PROMOTIONAL = ''
    ROUND = ''

    BRICK_SUBCATEGORY_CHOICES = [
        (DECORATED, 'Decorated'),
        (MODIFIED, 'Modified'),
        (PROMOTIONAL, 'Promotional'),
        (ROUND, 'Round'),
    ]

    # Technic subcategories
    AXLE = ''
    BRICK = ''
    CONNECTOR = ''
    DISK = ''
    GEAR = ''
    LIFTARM = ''
    LINK = ''
    PIN = ''
    PLATE = ''
    SHOCK_ABSORBER = ''

    TECHNIC_SUBCATEGORY_CHOICES = [
        (AXLE, 'Axle'),
        (BRICK, 'Brick'),
        (CONNECTOR, 'Connector'),
        (DISK, 'Disk'),
        (GEAR, 'Gear'),
        (LIFTARM, 'Liftarm'),
        (LINK, 'Link'),
        (PIN, 'Pin'),
        (PLATE, 'Plate'),
        (SHOCK_ABSORBER, 'Shock absorber'),
    ]

    # Electric subcategories
    BATTERY_BOX = ''
    PROGRAMMABLE = ''
    LIGHTS = ''
    MOTOR = ''
    WIRE = ''

    ELECTRIC_SUBCATEGORY_CHOICES = [
        (BATTERY_BOX, 'Battery box'),
        (PROGRAMMABLE, 'Programmable'),
        (LIGHTS, 'Lights'),
        (MOTOR, 'Motor'),
        (WIRE, 'Wire'),
    ]

    subcategory_id = models.CharField(max_length = 10, primary_key = True) # populate once the category has been chosen
    subcategory_name = models.CharField(unique = True, max_length = 50, help_text = "Type subcategory name")

    def __str__(self):
        return self.subcategory_name

    def get_absolute_url(self):
        pass
