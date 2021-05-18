import markdown
from django.db import models

from mdeditor.fields import MDTextField
from model_utils import Choices


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='分类名', unique=True, db_index=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类管理'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题', unique=True, db_index=True)
    content_raw = MDTextField(verbose_name='原始内容')
    content_render = models.TextField(verbose_name='呈现内容', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='分类',
                                 db_index=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def save(self, *args, **kwargs):
        # 将Markdown格式 转为html，页面上显示
        self.content_render = markdown.markdown(self.content_raw, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章管理'

    def __str__(self):
        return self.title

class Mcallnote(models.Model):
   row_num = models.AutoField(db_column='row_num', primary_key=True)
   SAMPLEID = models.CharField(db_column='SAMPLEID', blank=True, null=True, verbose_name=u"MARCH ID",
                                  max_length=10)  # Field name made lowercase.
   call_date = models.DateField( db_column='call_date', blank=False,verbose_name=u"Date of Call Note" )  # Field name made lowercase.
   CALLNOTE = models.TextField(db_column='CALLNOTE', blank=True,verbose_name=u"Call Note",
                                 null=True)  # Field name made lowercase.
   type = models.CharField(max_length=25, db_column='type', blank=True, null=True)
   initial = models.CharField(max_length=10, db_column='initial', blank=True, null=True,verbose_name=u"Please enter your initial")

   class Meta:
        managed = True
        db_table = 'march_callnote'
        verbose_name_plural = 'MARCH Call Note'

class Mcontact(models.Model):
    row_num = models.AutoField(db_column='row_num', primary_key=True)
    responseid = models.CharField(db_column='ResponseID', blank=True, null=True,verbose_name=u"Qualtrics ID",max_length=30)  # Field name made lowercase.
    responseset = models.CharField(max_length=20,db_column='ResponseSet', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(max_length=20,db_column='IPAddress', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True,verbose_name=u"Survey Start date")  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True,verbose_name=u"Survey Start date")  # Field name made lowercase.
    recipientlastname = models.IntegerField(db_column='RecipientLastName', blank=True, null=True)  # Field name made lowercase.
    recipientfirstname = models.IntegerField(db_column='RecipientFirstName', blank=True, null=True)  # Field name made lowercase.
    recipientemail = models.IntegerField(db_column='RecipientEmail', blank=True, null=True)  # Field name made lowercase.
    externaldatareference = models.IntegerField(db_column='ExternalDataReference', blank=True, null=True)  # Field name made lowercase.
    finished = models.BigIntegerField(db_column='Finished', blank=True, null=True)  # Field name made lowercase.
    status = models.BigIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    q1 = models.BigIntegerField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2_1_text = models.CharField(max_length=20,blank=True, null=True,verbose_name=u"First Name")  # Field name made lowercase.
    q2_2_text = models.CharField(max_length=20,db_column='Q2_2_TEXT', blank=True, null=True,verbose_name=u"Middle Name")  # Field name made lowercase.
    q2_3_text = models.CharField(max_length=20,db_column='Q2_3_TEXT', blank=True, null=True,verbose_name=u"Last Name")  # Field name made lowercase.
    q47_1 = models.CharField(max_length=10,db_column='Q47_1', blank=True, null=True,verbose_name=u"Birth Month")  # Field name made lowercase.
    q47_2 = models.BigIntegerField(db_column='Q47_2', blank=True, null=True,verbose_name=u"Birth Day")  # Field name made lowercase.
    q47_3 = models.BigIntegerField(db_column='Q47_3', blank=True, null=True,verbose_name=u"Birth Year")  # Field name made lowercase.
    q49_1_text = models.CharField(max_length=20,db_column='Q49_1_TEXT', blank=True, null=True,verbose_name=u"Child First Name")  # Field name made lowercase.
    q49_2_text = models.CharField(max_length=20,db_column='Q49_2_TEXT', blank=True, null=True,verbose_name=u"Child Middle Name")  # Field name made lowercase.
    q49_3_text = models.CharField(max_length=20,db_column='Q49_3_TEXT', blank=True, null=True,verbose_name=u"Child Last Name")  # Field name made lowercase.
    q50_1 = models.TextField(db_column='Q50_1', blank=True, null=True, verbose_name=u"Child Birth Month")  # Field name made lowercase.
    q50_2 = models.BigIntegerField(db_column='Q50_2', blank=True, null=True,verbose_name=u"Child Birth Day")  # Field name made lowercase.
    q50_3 = models.BigIntegerField(db_column='Q50_3', blank=True, null=True,verbose_name=u"Child Birth Year")  # Field name made lowercase.
    q6 = models.TextField(db_column='Q6', blank=True, null=True,verbose_name=u"Best Phone Number to Reach")  # Field name made lowercase.
    q7 = models.TextField(db_column='Q7', blank=True, null=True,verbose_name=u"Do You Have Additional Home Phone or Work Phone")  # Field name made lowercase.
    q8 = models.TextField(db_column='Q8', blank=True, null=True,verbose_name=u"Additional Phone NUmber")  # Field name made lowercase.
    q9 = models.TextField(db_column='Q9', blank=True, null=True,verbose_name=u"Can we Text This Number")  # Field name made lowercase.
    q10 = models.TextField(db_column='Q10', blank=True, null=True,verbose_name=u"Can we Viocemail This Number")  # Field name made lowercase.
    q11_1 = models.TextField(db_column='Q11_1', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_2 = models.TextField(db_column='Q11_2', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_3 = models.TextField(db_column='Q11_3', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_4 = models.TextField(db_column='Q11_4', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_5 = models.TextField(db_column='Q11_5', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_6 = models.TextField(db_column='Q11_6', blank=True, null=True,verbose_name=u"Preferred Time")  # Field name made lowercase.
    q11_7 = models.TextField(db_column='Q11_7', blank=True, null=True,verbose_name=u"Other Preferred Time")  # Field name made lowercase.
    q11_7_text = models.TextField(db_column='Q11_7_TEXT', blank=True, null=True,verbose_name=u"Specify Other Preferred Time")  # Field name made lowercase.
    q51 = models.TextField(db_column='Q51', blank=True, null=True,verbose_name=u"Additional Phone Number to Provide")  # Field name made lowercase.
    q47 = models.TextField(db_column='Q47', blank=True, null=True,verbose_name=u"Additional Phone Number")  # Field name made lowercase.
    q48 = models.TextField(db_column='Q48', blank=True, null=True,verbose_name=u"Can we Text This Phone")  # Field name made lowercase.
    q49 = models.TextField(db_column='Q49', blank=True, null=True,verbose_name=u"Can we Viocemail This Number")  # Field name made lowercase.
    q12_1_text = models.TextField(db_column='Q12_1_TEXT', blank=True, null=True,verbose_name=u"Address Line 1")  # Field name made lowercase.
    q12_2_text = models.TextField(db_column='Q12_2_TEXT', blank=True, null=True,verbose_name=u"Address Line 2")  # Field name made lowercase.
    q12_3_text = models.TextField(db_column='Q12_3_TEXT', blank=True, null=True,verbose_name=u"City")  # Field name made lowercase.
    q12_4_text = models.TextField(db_column='Q12_4_TEXT', blank=True, null=True,verbose_name=u"State")  # Field name made lowercase.
    q12_5_text = models.TextField(db_column='Q12_5_TEXT', blank=True, null=True,verbose_name=u"Zip")  # Field name made lowercase.
    q13 = models.TextField(db_column='Q13', blank=True, null=True,verbose_name=u"Do you Plan to Move")  # Field name made lowercase.
    q14_1_text = models.DateField(db_column='Q14_1_TEXT', blank=True, null=True,verbose_name=u"Move Date")  # Field name made lowercase.
    q14_2_text = models.IntegerField(db_column='Q14_2_TEXT', blank=True, null=True,verbose_name=u"Address Line 1")  # Field name made lowercase.
    q14_3_text = models.IntegerField(db_column='Q14_3_TEXT', blank=True, null=True,verbose_name=u"Address Line 2")  # Field name made lowercase.
    q14_4_text = models.IntegerField(db_column='Q14_4_TEXT', blank=True, null=True,verbose_name=u"City")  # Field name made lowercase.
    q14_5_text = models.IntegerField(db_column='Q14_5_TEXT', blank=True, null=True,verbose_name=u"State")  # Field name made lowercase.
    q14_6_text = models.IntegerField(db_column='Q14_6_TEXT', blank=True, null=True,verbose_name=u"Zip")  # Field name made lowercase.
    q15 = models.TextField(db_column='Q15', blank=True, null=True)  # Field name made lowercase.
    q16 = models.TextField(db_column='Q16', blank=True, null=True)  # Field name made lowercase.
    q17 = models.TextField(db_column='Q17', blank=True, null=True)  # Field name made lowercase.
    q18 = models.BigIntegerField(db_column='Q18', blank=True, null=True)  # Field name made lowercase.
    q19_1_text = models.TextField(db_column='Q19_1_TEXT', blank=True, null=True)  # Field name made lowercase.
    q19_2_text = models.TextField(db_column='Q19_2_TEXT', blank=True, null=True)  # Field name made lowercase.
    q20 = models.TextField(db_column='Q20', blank=True, null=True)  # Field name made lowercase.
    q21 = models.TextField(db_column='Q21', blank=True, null=True)  # Field name made lowercase.
    q22 = models.TextField(db_column='Q22', blank=True, null=True)  # Field name made lowercase.
    q23_1_text = models.TextField(db_column='Q23_1_TEXT', blank=True, null=True)  # Field name made lowercase.
    q23_2_text = models.IntegerField(db_column='Q23_2_TEXT', blank=True, null=True)  # Field name made lowercase.
    q23_3_text = models.TextField(db_column='Q23_3_TEXT', blank=True, null=True)  # Field name made lowercase.
    q23_4_text = models.TextField(db_column='Q23_4_TEXT', blank=True, null=True)  # Field name made lowercase.
    q23_5_text = models.TextField(db_column='Q23_5_TEXT', blank=True, null=True)  # Field name made lowercase.
    q24 = models.TextField(db_column='Q24', blank=True, null=True)  # Field name made lowercase.
    q26_1_text = models.TextField(db_column='Q26_1_TEXT', blank=True, null=True)  # Field name made lowercase.
    q26_2_text = models.TextField(db_column='Q26_2_TEXT', blank=True, null=True)  # Field name made lowercase.
    q27 = models.TextField(db_column='Q27', blank=True, null=True)  # Field name made lowercase.
    q28 = models.TextField(db_column='Q28', blank=True, null=True)  # Field name made lowercase.
    q29 = models.TextField(db_column='Q29', blank=True, null=True)  # Field name made lowercase.
    q30_1_text = models.IntegerField(db_column='Q30_1_TEXT', blank=True, null=True)  # Field name made lowercase.
    q30_2_text = models.IntegerField(db_column='Q30_2_TEXT', blank=True, null=True)  # Field name made lowercase.
    q30_3_text = models.IntegerField(db_column='Q30_3_TEXT', blank=True, null=True)  # Field name made lowercase.
    q30_4_text = models.IntegerField(db_column='Q30_4_TEXT', blank=True, null=True)  # Field name made lowercase.
    q30_5_text = models.IntegerField(db_column='Q30_5_TEXT', blank=True, null=True)  # Field name made lowercase.
    q31 = models.TextField(db_column='Q31', blank=True, null=True)  # Field name made lowercase.
    q32_1_text = models.TextField(db_column='Q32_1_TEXT', blank=True, null=True)  # Field name made lowercase.
    q32_2_text = models.TextField(db_column='Q32_2_TEXT', blank=True, null=True)  # Field name made lowercase.
    q32_3_text = models.TextField(db_column='Q32_3_TEXT', blank=True, null=True)  # Field name made lowercase.
    q33 = models.TextField(db_column='Q33', blank=True, null=True)  # Field name made lowercase.
    q34 = models.BigIntegerField(db_column='Q34', blank=True, null=True)  # Field name made lowercase.
    q35 = models.IntegerField(db_column='Q35', blank=True, null=True)  # Field name made lowercase.
    q35_text = models.TextField(db_column='Q35_TEXT', blank=True, null=True)  # Field name made lowercase.
    q35_1 = models.TextField(db_column='Q35_1', blank=True, null=True)  # Field name made lowercase.
    q51_1 = models.TextField(db_column='Q51_1', blank=True, null=True)  # Field name made lowercase.
    q50_4_text = models.BigIntegerField(db_column='Q50_4_TEXT', blank=True, null=True)  # Field name made lowercase.
    q50_5_text = models.BigIntegerField(db_column='Q50_5_TEXT', blank=True, null=True)  # Field name made lowercase.
    q37_1 = models.TextField(db_column='Q37_1', blank=True, null=True)  # Field name made lowercase.
    q37_2 = models.TextField(db_column='Q37_2', blank=True, null=True)  # Field name made lowercase.
    q37_3 = models.TextField(db_column='Q37_3', blank=True, null=True)  # Field name made lowercase.
    q53 = models.TextField(db_column='Q53', blank=True, null=True)  # Field name made lowercase.
    q38 = models.TextField(db_column='Q38', blank=True, null=True)  # Field name made lowercase.
    q54 = models.TextField(db_column='Q54', blank=True, null=True)  # Field name made lowercase.
    q39 = models.TextField(db_column='Q39', blank=True, null=True)  # Field name made lowercase.
    q40 = models.TextField(db_column='Q40', blank=True, null=True)  # Field name made lowercase.
    q41_1 = models.TextField(db_column='Q41_1', blank=True, null=True)  # Field name made lowercase.
    q41_2 = models.TextField(db_column='Q41_2', blank=True, null=True)  # Field name made lowercase.
    q41_3 = models.TextField(db_column='Q41_3', blank=True, null=True)  # Field name made lowercase.
    q41_4 = models.TextField(db_column='Q41_4', blank=True, null=True)  # Field name made lowercase.
    q41_5 = models.TextField(db_column='Q41_5', blank=True, null=True)  # Field name made lowercase.
    q41_6 = models.TextField(db_column='Q41_6', blank=True, null=True)  # Field name made lowercase.
    q41_7 = models.TextField(db_column='Q41_7', blank=True, null=True)  # Field name made lowercase.
    q41_7_text = models.TextField(db_column='Q41_7_TEXT', blank=True, null=True)  # Field name made lowercase.
    q42 = models.TextField(db_column='Q42', blank=True, null=True)  # Field name made lowercase.
    q55 = models.TextField(db_column='Q55', blank=True, null=True)  # Field name made lowercase.
    q43 = models.TextField(db_column='Q43', blank=True, null=True)  # Field name made lowercase.
    locationlatitude = models.FloatField(db_column='LocationLatitude', blank=True, null=True)  # Field name made lowercase.
    locationlongitude = models.FloatField(db_column='LocationLongitude', blank=True, null=True)  # Field name made lowercase.
    locationaccuracy = models.BigIntegerField(db_column='LocationAccuracy', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.CharField(max_length=6,db_column='SAMPLEID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mcontact'
        verbose_name_plural = 'MARCH Contact Survey'

class Mcontactinfo(models.Model):
   row_num = models.AutoField(db_column='row_num', primary_key=True)
   SAMPLEID = models.CharField(max_length=10, db_column='SAMPLEID', blank=False, null=False,verbose_name=u"MARCH ID")
   currdate = models.DateField( db_column='currdate', blank=False,verbose_name=u"Date of contact information" )
   address = models.TextField( db_column='address', blank=True, null=True,verbose_name=u"Address" )
   choice_social =  Choices('Yes', 'No')
   move_home = models.CharField(db_column='move_home',choices=choice_social, max_length=10, blank=True, null=True,verbose_name=u"Plan to move home")
   move_home_address =models.TextField(db_column='move_home_address', blank=True, null=True,
                                          verbose_name=u"New address plan to move")
   move_home_date = models.DateField(db_column='move_home_date',blank=True, null=True, verbose_name=u"Date of moving to new home")
   phone_num = models.CharField(max_length=30, db_column='phone_num', blank=True, null=True,verbose_name=u"Primary Phone Number")
   text_permission=models.CharField(max_length=5, db_column='text_permission', blank=True, null=True,verbose_name=u"Permission to text this number")
   other_phone = models.CharField(max_length=30, db_column='other_phone', blank=True, null=True,verbose_name=u"Additional Phone Number")
   other_text_permission = models.CharField(max_length=5, db_column='other_text_permission', blank=True, null=True,verbose_name=u"Permission to text this number")
   email=models.TextField( db_column='email', blank=True, null=True,verbose_name=u"Email Address" )
   prefer_c = Choices('Text', 'Email', 'call', 'Any of the above')
   prefer_contact = models.CharField(db_column='prefer_contact',choices=prefer_c, max_length=20, blank=True, null=True,
                                     verbose_name=u"Preferred contact method")
   contact_a=models.TextField( db_column='contact_a', blank=True, null=True,verbose_name=u"Alternate contact name" )
   contact_aphone=models.CharField(max_length=30, db_column='contact_aphone', blank=True, null=True,verbose_name=u"Phone number of alternate contact")
   contact_b = models.TextField( db_column='contact_b', blank=True, null=True,verbose_name=u"Other alternate contact name" )
   contact_bphone = models.CharField(max_length=30, db_column='contact_bphone', blank=True, null=True,verbose_name=u"Phone number of alternate contact")
   social_media = models.CharField(db_column='social_media',choices=choice_social, max_length=10, blank=True, null=True,
                                     verbose_name=u"Follow social media")
   facebook = models.CharField(max_length=150, db_column='facebook', blank=True, null=True, verbose_name=u"Facebook")
   Instagram = models.CharField(max_length=150, db_column='Instagram', blank=True, null=True, verbose_name=u"Instagram")
   Twitter = models.CharField(max_length=150, db_column='Twitter', blank=True, null=True, verbose_name=u"Twitter")
   source= models.CharField(max_length=30, db_column='source', blank=True, null=True,verbose_name=u"Source of the contact information")
   checkbbb = Choices('Unknown','Yes', 'No')
   PCG = models.CharField(choices=checkbbb,default=checkbbb.Unknown, max_length=20,blank=True, null=True)
   initial = models.CharField(max_length=10, db_column='initial', blank=True, null=True,verbose_name=u"Please enter your initial")
   qualtrics_id = models.CharField(max_length=50, db_column='qualtrics_id', blank=True, null=True)

   class Meta:
        managed = True
        db_table = 'march_all_contact'
        verbose_name_plural='MARCH All Contact Information'