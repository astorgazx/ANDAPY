from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.



class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos')
    stock = models.IntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    numero = models.IntegerField(auto_created=True)
    fecha = models.DateField()
    total = models.IntegerField()
    entregado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
    
class DetallePedido(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    rfc = models.CharField(max_length=50)
    immex = models.CharField(max_length=50)
    repae= models.CharField(max_length=50)
    taxID = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener una dirección de correo electrónico')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    def __str__(self):
        return self.nombre
    
    
class Factura(models.Model):
    numero = models.IntegerField(auto_created=True)
    fecha = models.DateField()
    total = models.IntegerField()
    entregado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
    
class DetalleFactura(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    metodo_pago = models.enums('PayPal,MercadoPago')

    def __str__(self):
        return self.cantidad