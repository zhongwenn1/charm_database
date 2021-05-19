from django.db import models

# Create your models here.
class covid(models.Model):
   row_num = models.AutoField(db_column='row_num', primary_key=True)
   ResponseID = models.CharField(max_length=25, db_column='ResponseID', blank=True, null=True,verbose_name=u"Qualtrics ID",unique=True)
   startdate = models.DateField(db_column='startdate', blank=True, null=True, verbose_name=u"Survey start date")
   enddate = models.DateField(db_column='enddate', blank=True, null=True, verbose_name=u"Survey end date")
   first_name = models.CharField(max_length=30, db_column='first_name', blank=True, null=True,verbose_name=u"First name")
   last_name = models.CharField(max_length=30, db_column='last_name', blank=True, null=True,verbose_name=u"Last name")
   birthday = models.DateField(db_column='birthday', blank=False,verbose_name=u"Birthday" )
   address=models.TextField(db_column='address', blank=True, null=True,verbose_name=u"Address for gift card")
   primary_phone = models.CharField(max_length=30, db_column='primary_phone', blank=True, null=True,verbose_name=u"Primary Phone Number")
   secondary_phone = models.CharField(max_length=30, db_column='secondary_phone', blank=True, null=True,verbose_name=u"Secondary Phone Number")
   email= models.TextField(db_column='email', blank=True, null=True,verbose_name=u"Email Address")
   type= models.CharField(max_length=30, db_column='type', blank=True, null=True,verbose_name=u"Type of the COVID19 Survey")
   first_childname= models.CharField(max_length=30, db_column='first_childname', blank=True, null=True,verbose_name=u"Child one first name")
   second_childname= models.CharField(max_length=30, db_column='second_childname', blank=True, null=True,verbose_name=u"Child two first name")
   child_lastname= models.CharField(max_length=30, db_column='child_lastname', blank=True, null=True,verbose_name=u"Child last name")
   child_dob = models.DateField(db_column='child_dob', blank=True,null=True,verbose_name=u"Child Birthday")
   cohort_id = models.CharField(max_length=10, db_column='cohort_id', blank=True, null=True,verbose_name=u"Cohort ID")

   class Meta:
        managed = True
        db_table = 'charm_covid'
        verbose_name_plural='COVID19 Survey'