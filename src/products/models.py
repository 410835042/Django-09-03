from django.db import models
from django.urls import reverse


# Create your models here.
# 引用Django內建的模型作為模型
# Text型態輸入、True需大寫、blank針對表格能否為空、null針對資料庫能否為空

class Product(models.Model):
    product_name = models.CharField(max_length=120)  # char型態輸入
    brand = models.ForeignKey('partners.Brand', on_delete=models.CASCADE, default=None, related_name='product')
    material_color = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(decimal_places=1, max_digits=7)  # decimal型態輸入
    picture = models.ImageField(upload_to='image/', blank=True, null=True)
    threeD_model = models.FileField(upload_to='gltf/', blank=True, null=True)

    def get_absolute_url(self):
        # return f"/products/{self.id}/" #依據產品編號提取資料
        return reverse("products:product-detail", kwargs={"p_id": self.id})  # 動態依據搜尋路徑名稱提取資料
