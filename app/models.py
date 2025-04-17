from django.db import models


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=70, blank=False, unique=True)

    def __str__(self):
        return self.username


# Профиль (OneToOne с User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"Profile of {self.user.username}"


# Заказ (OneToMany с User, ManyToMany с Product)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Один ко многим
    products = models.ManyToManyField('Product')  # Много ко многим
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# Товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
