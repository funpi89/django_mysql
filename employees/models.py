# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    categoryid = models.IntegerField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=45)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'employees'


class EmployeesLog(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees_log'


class Orderdetails(models.Model):
    orderdetailid = models.IntegerField(db_column='OrderDetailID', primary_key=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    shipperid = models.IntegerField(db_column='ShipperID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    productid = models.IntegerField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.IntegerField(db_column='SupplierID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'


class Shippers(models.Model):
    shipperid = models.IntegerField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    shippername = models.CharField(db_column='ShipperName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippers'


class Suppliers(models.Model):
    supplierid = models.IntegerField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suppliers'
