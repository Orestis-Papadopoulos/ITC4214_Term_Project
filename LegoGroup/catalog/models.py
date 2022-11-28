from django.db import models
import shortuuid

# define the category and subcategory first to reference them in later models as foreign keys directly

class Category(models.Model):
    """
    Defines a lego part category.
    """

    BRICK, TECHNIC, ELECTRIC = 'B', 'T', 'E'
    CATEGORY_CHOICES = [(BRICK, 'Brick'), (TECHNIC, 'Technic'), (ELECTRIC, 'Electric')]

    id = models.CharField(primary_key = True, max_length = 50, default = shortuuid.uuid(), editable = False)
    name = models.CharField(unique = True, max_length = 50, help_text = "Select category", choices = CATEGORY_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

class Subcategory(models.Model):
    """
    Defines a lego part subcategory.
    """

    # Brick subcategories
    DECORATED, MODIFIED, PROMOTIONAL, ROUND = 'D', 'M', 'P', 'R'
    BRICK_SUBCATEGORY_CHOICES = [(DECORATED, 'Decorated'), (MODIFIED, 'Modified'), (PROMOTIONAL, 'Promotional'), (ROUND, 'Round')]

    # Technic subcategories
    AXLE, BRICK, CONNECTOR, DISK, GEAR = 'A', 'B', 'C', 'D', 'G'
    TECHNIC_SUBCATEGORY_CHOICES = [(AXLE, 'Axle'), (BRICK, 'Brick'), (CONNECTOR, 'Connector'), (DISK, 'Disk'), (GEAR, 'Gear')]

    # Electric subcategories
    BATTERY_BOX, PROGRAMMABLE, LIGHTS, MOTOR, WIRE = 'B', 'P', 'L', 'M', 'W'
    ELECTRIC_SUBCATEGORY_CHOICES = [(BATTERY_BOX, 'Battery box'), (PROGRAMMABLE, 'Programmable'), (LIGHTS, 'Lights'), (MOTOR, 'Motor'), (WIRE, 'Wire')]

    id = models.CharField(primary_key = True, max_length = 50, default = shortuuid.uuid(), editable = False) # populate once the category has been chosen
    name = models.CharField(unique = True, max_length = 50, help_text = "Select subcategory")
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True)

    def __str__(self):
        return self.subcategory_name

    def get_subcategories_of(category):
        """
        Returns the list of subcategories of the passed category.

        Parameters
            category: str
                The category of which the subcategories are to be returned.

        Returns
            : list
                The list of subcategories corresponding to the passed category.
        """

        global BRICK_SUBCATEGORY_CHOICES
        global TECHNIC_SUBCATEGORY_CHOICES
        global ELECTRIC_SUBCATEGORY_CHOICES

        if category == 'Brick': return BRICK_SUBCATEGORY_CHOICES
        elif category == 'Technic': return TECHNIC_SUBCATEGORY_CHOICES
        elif category == 'Electric': return ELECTRIC_SUBCATEGORY_CHOICES

    def get_absolute_url(self):
        pass

class LegoPart(models.Model):
    """
    Defines attributes of a Lego part.
    """

    id = models.UUIDField(primary_key = True, max_length = 50, default = shortuuid.uuid(), editable = False)
    name = models.CharField(max_length = 50, help_text = "Type part name")
    description = models.TextField(max_length = 1000, help_text = "Type part description (up to 1000 characters)", blank = True)
    image = models.ImageField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True)
    subcategory = models.ForeignKey(Subcategory, on_delete = models.PROTECT, choices = Subcategory.get_subcategories_of(category.name), null = True)
    public_access = models.BooleanField(default = False)

    def __str__(self):
        return self.part_name

    def get_absolute_url(self):
        pass

class User(models.Model):
    """
    Defines attributes of a user.
    """

    username = models.CharField(primary_key = True, max_length = 30, help_text = "Type username here", default = 'username')
    password = models.CharField(max_length = 20, help_text = "Type password here", default = 'password')
    first_name = models.CharField(max_length = 50, help_text = "Type first name here", default = 'George')
    last_name = models.CharField(max_length = 50, help_text = "Type last name here", default = 'Boole')
    email = models.EmailField(max_length = 100, help_text = "Type email here", null = True)
    user_image = models.ImageField(null = True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        pass
