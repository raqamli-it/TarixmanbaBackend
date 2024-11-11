from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class Library_Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Library(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Library_Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.title


class News(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.title


class Sliders(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Connection(BaseModel):
    phone = models.IntegerField()
    phone_two = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    map = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class About(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Feedbacks(BaseModel):
    message = models.TextField()
    # user = models.ForiegnKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Comments(BaseModel):
    message = models.TextField()

    # user = models.ForiegnKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Connection_Category(models.Model):
    title= models.CharField(max_length=255)


class Connection_Value(models.Model):
    connection_category = models.ForeignKey(Connection_Category, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)