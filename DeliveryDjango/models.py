from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model): 
    name = models.CharField(max_length=200) 
    def __str__(self): 
        return self.name

class Dish(models.Model): 
    title = models.CharField(max_length=200) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descr = models.TextField() 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='images/', max_length=200, null=True, blank=True)

class Restaurant(models.Model): 
    name = models.CharField(max_length=500) 
    address = models.CharField(max_length=1000) 
    menu = models.ManyToManyField(Dish, through='MenuItem')


    def __str__(self):
        return self.name



class MenuItem(models.Model): 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 



class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True) 
    items = models.ManyToManyField(Dish, through='CartItem') 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Person(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    lastname = models.CharField(max_length=200) 
    middlename = models.CharField(max_length=200) 
    phone = models.CharField(max_length=200) 
    email = models.EmailField(unique=True) 
    pin = models.CharField(max_length=4, unique=True)

class CartItem(models.Model): 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    item = models.ForeignKey(Dish, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=0)



class Order(models.Model): 
    CART_CHOICES = [ ('card', 'Карта'), ('cash', 'Наличные'), ]
    payment_method = models.CharField(max_length=20, choices=CART_CHOICES) 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    items = models.ManyToManyField(CartItem, through='OrderItem')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True) 
    have_review = models.BooleanField(default=False)
    
    def calculate_total_price(self): 
        order_items = CartItem.objects.filter(cart__id=self.payment_method.split('_')[1])
        self.total_price = sum(order_item.item.price * order_item.quantity for order_item in order_items) 
        self.save()
        
    def has_review_from_user(self, user): 
        return self.reviews.filter(user=user).exists()


    def __str__(self):
        return f"Order #{self.id}"

    def calculate_total_price(self):
        order_items = CartItem.objects.filter(cart__id=self.payment_method.split('_')[1])
        self.total_price = sum(order_item.item.price * order_item.quantity for order_item in order_items)
        self.save()

    def has_review_from_user(self, user):
        return self.reviews.filter(user=user).exists()


class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        unique_together = ('order', 'cart_item',)




class Review(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='reviews') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField() 
    delivery_speed_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    taste_intensity_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    product_quality_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    service_quality_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    

    def __str__(self):
        return f"{self.user.username}'s review for {self.order}"




