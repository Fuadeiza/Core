from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to ='products/') 

    def __str__(self):
        return self.name


class Flavour(models.Model):
    parent = models.ForeignKey(Product,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to ='products/') 

    def __str__(self):
        return f'{self.name} : {self.parent.name}'


class Order(models.Model):
    name = models.CharField(max_length = 100,blank = True)
    email = models.EmailField(max_length = 100,blank = True)
    phone = models.CharField(max_length = 20,blank = True)

    area = models.CharField(max_length = 100,blank = True)
    country = models.CharField(max_length = 100,blank = True)
    shipping = models.PositiveIntegerField(default = 0)

    subtotal = models.PositiveIntegerField(default = 0)
    total = models.PositiveIntegerField(default = 0)

    street = models.CharField(max_length = 100,blank = True)
    house = models.CharField(max_length = 100,blank = True)
    specific_directions = models.CharField(max_length = 100,blank = True)

    confirmation_sent = models.BooleanField(default = False)
    order_id = models.CharField(max_length = 20,blank = True)
    status = models.CharField(max_length = 20,choices = (("On The Way","On The Way"),("In Progress","In Progress"),("Completed","Completed")),blank = True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    flavour_linked = models.ForeignKey(Flavour,on_delete = models.CASCADE)
    user_order = models.ForeignKey(Order,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.flavour_linked.name

