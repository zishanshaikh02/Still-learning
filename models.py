from django.db import models
from django.contrib.auth.models import User





# class UserModel(models.Model):
#     user = models.OneToOneField(User,on_delete = models.CASCADE)

#     name = models.CharField(max_length=255)
#     email = models.EmailField(null=False)
#     password = models.CharField(max_length=255,null=False)
#     is_verified = models.BooleanField(default=False)


#     def __str__(self) -> str:
#         return self.name
    
    


# Create your models here.
class Category(models.Model):

    cat_name = models.CharField(max_length=255)
    cat_ima = models.ImageField(upload_to="images")
    sub_category =  models.CharField(max_length=255,choices=[("Featured", "FEATURED"),("normal","NORMAL"),("trending","TRENDING")],default="NORMAL")


    def __str__(self) -> str:
        return self.cat_name
    






# class SubCatergory(models.Model):

#     Category_name = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name="sub_category")
#     sub_category_name = models.CharField(max_length=255,primary_key=True,default="mens",blank=True)


#     def __str__(self) -> str:
#         return self.sub_category_name

class Product(models.Model):

    category  = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name="cat_pro")
    # sub_cate_name = models.ForeignKey(SubCatergory,on_delete=models.CASCADE,related_name="sub_cat",null=True)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to="product",default=False,null=True)
    product_image_2 = models.ImageField(upload_to="product",default=False,null=True)
    product_price =  models.IntegerField(null=True)
    is_new = models.BooleanField(default=False)
    type =  models.CharField(max_length=255,choices=[("Featured", "FEATURED"),("normal","NORMAL"),("trending","TRENDING")],default="NORMAL")
    countInStock = models.IntegerField(null=True ,default=False)
    description = models.CharField(max_length=255,default=False)





    def __str__(self):
        return self.product_name
    
class UserCustomer(models.Model):

    customer_name = models.CharField(max_length=255)
    customer_password = models.CharField(max_length=255)
    customer_email =  models.CharField(max_length=355)
    is_verified = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.customer_email
    

class UserModelsCustomer(models.Model):
    customer_name =  models.OneToOneField(User,on_delete = models.CASCADE)
    customer_password = models.CharField(max_length=255)
    customer_email =  models.CharField(max_length=355)
    is_verified = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.customer_email


