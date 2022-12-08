from django.db import models
#import shortuuid # replace all 'default = uuid.uuid4' with 'default = shortuuid.uuid()'
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# define the category and subcategory first to reference them in later models as foreign keys directly

CATEGORY_CHOICES = [('Brick', 'Brick'), ('Technic', 'Technic'), ('Electric', 'Electric')]

class Category(models.Model):
    """
    Defines a lego part category.
    """

    id = models.CharField(primary_key = True, max_length = 50, default = uuid.uuid4, editable = False)
    name = models.CharField(unique = True, max_length = 50, help_text = "Select category", choices = CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_category_of(subcategory):
        if subcategory in ['Decorated', 'Modified', 'Promotional', 'Round']: return 'Brick'
        elif subcategory in ['Axle', 'Brick', 'Connector', 'Disk', 'Gear']: return 'Technic'
        elif subcategory in ['Battery box', 'Programmable', 'Lights', 'Motor', 'Wire']: return 'Electric'

class Subcategory(models.Model):
    """
    Defines a lego part subcategory.
    """

    BRICK_SUBCATEGORY_CHOICES = [('Decorated', 'Decorated'), ('Modified', 'Modified'), ('Promotional', 'Promotional'), ('Round', 'Round')]
    TECHNIC_SUBCATEGORY_CHOICES = [('Axle', 'Axle'), ('Brick', 'Brick'), ('Connector', 'Connector'), ('Disk', 'Disk'), ('Gear', 'Gear')]
    ELECTRIC_SUBCATEGORY_CHOICES = [('Battery box', 'Battery box'), ('Programmable', 'Programmable'), ('Lights', 'Lights'), ('Motor', 'Motor'), ('Wire', 'Wire')]

    id = models.CharField(primary_key = True, max_length = 50, default = uuid.uuid4, editable = False) # populate once the category has been chosen
    name = models.CharField(unique = True, max_length = 50, help_text = "Select subcategory", choices = BRICK_SUBCATEGORY_CHOICES + TECHNIC_SUBCATEGORY_CHOICES + ELECTRIC_SUBCATEGORY_CHOICES)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True)

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

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

        global BRICK_SUBCATEGORY_CHOICES, TECHNIC_SUBCATEGORY_CHOICES, ELECTRIC_SUBCATEGORY_CHOICES

        if category == 'Brick': return BRICK_SUBCATEGORY_CHOICES
        elif category == 'Technic': return TECHNIC_SUBCATEGORY_CHOICES
        elif category == 'Electric': return ELECTRIC_SUBCATEGORY_CHOICES

    def get_absolute_url(self):
        pass

class LegoPart(models.Model):
    """
    Defines attributes of a Lego part.
    """

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = True)
    name = models.CharField(max_length = 50, help_text = "Type part name")
    description = models.TextField(max_length = 1000, help_text = "Type part description (up to 1000 characters)", blank = True)
    image = models.ImageField(blank = True, upload_to = 'images/')
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True)
    subcategory = models.ForeignKey(Subcategory, on_delete = models.PROTECT, null = True)
    public_access = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass   

# see: https://www.youtube.com/watch?v=mWNeTTDB3zQ&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=12
class UserProfile(models.Model):
    """
    Defines attributes of a user.
    """

    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 0)
    username = models.CharField(primary_key = True, max_length = 30, help_text = "Type username here", default = '')
    password = models.CharField(max_length = 20, help_text = "Type password here", default = '')
    first_name = models.CharField(max_length = 50, help_text = "Type first name here", default = '')
    last_name = models.CharField(max_length = 50, help_text = "Type last name here", default = '')
    email = models.EmailField(max_length = 100, help_text = "Type email here", default = '', blank = True)
    image = models.ImageField(blank = True, upload_to = 'images/')

    def __str__(self):
        return self.username

# overrides the default User model in admin; see: https://www.youtube.com/watch?v=lxSZevvkcc4&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=12
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)
