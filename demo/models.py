from django.db import models

# Create your models here.
from django.urls import reverse
from model_utils import Choices


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='部门名', help_text='一个部门的名字应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门管理"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=128, verbose_name='职务', null=True, blank=True)

    class Meta:
        verbose_name = '职务'
        verbose_name_plural = '职务管理'

    def get_absolute_url(self):
        return reverse('title-detail-view', args=(self.name,))

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(verbose_name='图片')
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片管理'

    def __str__(self):
        return self.image.path


class Employe(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text='员工的名字', null=False, blank=False,
                            db_index=True)

    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )

    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    idCard = models.CharField(max_length=18, verbose_name='身份证号', help_text='18位的身份证号码', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号')

    birthday = models.DateField(verbose_name='生日')
    time = models.TimeField(verbose_name='时间', auto_now=True)

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='部门',
                                   db_index=True)

    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='职务',
                              db_index=True)

    enable = models.BooleanField(verbose_name='状态', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工管理"

    def __str__(self):
        return self.name


class Acallnote(models.Model):
    row_num = models.AutoField(db_column='row_num', primary_key=True)
    family_ID = models.BigIntegerField(db_column='family_ID', blank=True, null=True)
    ARCH_ID = models.CharField(db_column='ARCH_ID', blank=True, null=True, verbose_name=u"ARCH ID",
                               max_length=10)  # Field name made lowercase.
    call_date = models.DateField( db_column='call_date', blank=False,verbose_name=u"Date of Call Note" )  # Field name made lowercase.
    call_note = models.TextField(db_column='call_note', blank=True,verbose_name=u"Call Note",
                                 null=True)  # Field name made lowercase.
    type = models.TextField( db_column='type', blank=True, null=True)
    initial = models.CharField(max_length=10, db_column='initial', blank=True, null=True,verbose_name=u"Please enter your initial")

    class Meta:
        # managed = True
        db_table = 'arch_callnote'
        # verbose_name = 'arch_callnote'
        verbose_name_plural='ARCH Call Note'

    def __str__(self):
        return self.ARCH_ID

class archtrack(models.Model):
    row_num = models.AutoField(db_column='row_num', primary_key=True)
    child_id = models.BigIntegerField(db_column='Child_ID', blank=True, null=True,
                                 verbose_name=u"Child ID")  # Field name made lowercase.
    arch_id = models.BigIntegerField(db_column='ARCH_ID', blank=True, null=True,
                                verbose_name=u"ARCH ID")  # Field name made lowercase.
    echo_id = models.CharField(db_column='echo_id', max_length=20, blank=True, null=True,verbose_name=u"ECHO ID")  # Field name made lowercase.
    echo_pin = models.CharField(db_column='echo_pin', max_length=10, blank=True, null=True,verbose_name=u"ECHO pin")  # Field name made lowercase.
    method_contact = Choices('Unknown', 'TEXT', 'Email','Call','Any')
    contactprefer_method = models.CharField(db_column='contactprefer_method',choices=method_contact, max_length=10, blank=True, null=True,verbose_name=u"preferred contact option")  # Field name made lowercase.
    gift_card = Choices('Unknown', 'Meijer', 'Walmart')
    giftcard=models.CharField(db_column='giftcard',choices=gift_card, max_length=10, blank=True, null=True,verbose_name=u"Gift card")  # Field name made lowercase.
    giftcard_date = models.DateField(db_column='giftcard_date', blank=True, null=True,
                                     verbose_name=u"Most recent gift card sent")
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateField(blank=True, null=True, verbose_name=u"Due date")
    age = models.BigIntegerField(blank=True, null=True, verbose_name=u"Child age")
    es_age = models.BigIntegerField(db_column='ES_age', blank=True, null=True,
                               verbose_name=u"Child age estimated from due date")  # Field name made lowercase.
    checkess = Choices('Unknown', 'YES', 'NO')
    echoreconsent = models.CharField(db_column='ECHOreconsent',choices=checkess, max_length=10, blank=True,
                                     null=True, verbose_name=u"ECHO Reconsent")  # Field name made lowercase.
    new_reconsent_date = models.DateField(db_column='new_reconsent_date',blank=True, null=True, verbose_name=u"ECHO Reconsent Date")
    reconsent_version = models.CharField(db_column='reconsent_version',blank=True, null=True, max_length=5,
                                         verbose_name=u"Most Recent Consent Version")
    fnpa_survey = models.DateField(db_column='FNPA_survey', blank=True, null=True, verbose_name=u"FNPA survey")  # Field name made lowercase.
    meal_survey = models.DateField(db_column='meal_survey', blank=True, null=True, verbose_name=u"Meal survey")
    age_consented_until = models.BigIntegerField(db_column='Age_consented_until', blank=True,
                                            null=True)  # Field name made lowercase.
    teeth_perm = models.CharField(db_column='Teeth_perm', max_length=5, blank=True,
                                  null=True, verbose_name=u"Consent to teeth")  # Field name made lowercase.
    inperson_perm = models.CharField(db_column='InPerson_perm', max_length=5, blank=True,
                                     null=True, verbose_name=u"Consent to in-person visit")  # Field name made lowercase.
    survey_outcome = Choices('Complete Interview', 'CHARM Q Only Complete', 'REDCap Only Complete', 'Partial Complete',
                             'NI, Reason Not Recorded', 'NS, Deceased Child', 'Refused Study Participation, Respondent',
                             'Final Refusal, Respondent', 'NI, Other Reason', 'NI, Locating Exhausted',
                             'NI, Deceased (Mom), Unable to Identify PCG','Unknown')
    one_month = models.TextField(db_column='one_month',blank=True, choices=survey_outcome,null=True,verbose_name=u"One-month survey outcome")
    onem_date = models.DateField(db_column='OneM_date', blank=True, null=True)  # Field name made lowercase.
    one_year = models.TextField(db_column='one_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"One-year survey outcome")
    oney_date = models.DateField(db_column='oneY_date', blank=True, null=True)  # Field name made lowercase.
    two_year = models.TextField(db_column='two_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"two-year survey outcome")
    twoy_date = models.DateField(db_column='twoY_date', blank=True, null=True)  # Field name made lowercase.
    three_year = models.TextField(db_column='three_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"three-year survey outcome")
    three_date = models.DateField(db_column='three_date', blank=True, null=True)
    three_giftdate = models.DateField(db_column='three_giftdate', blank=True, null=True,
                                      verbose_name=u"Three-year gift card date")
    four_year = models.TextField(db_column='four_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"four-year survey outcome")
    four_date = models.DateField(db_column='four_date', blank=True, null=True)
    four_giftdate = models.DateField(db_column='four_giftdate', blank=True, null=True,
                                     verbose_name=u"Four-year gift card date")
    five_year = models.TextField(db_column='five_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"five-year survey outcome")
    five_date = models.DateField(db_column='five_date', blank=True, null=True)
    five_giftdate = models.DateField(db_column='five_giftdate', blank=True, null=True,
                                     verbose_name=u"Five-year gift card date")
    six_year = models.TextField(db_column='six_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"six-year survey outcome")
    six_date = models.DateField(db_column='six_date', blank=True, null=True)
    six_giftdate = models.DateField(db_column='six_giftdate', blank=True, null=True,
                                    verbose_name=u"Six-year gift card date")
    seven_year = models.TextField(db_column='seven_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"seven-year survey outcome")
    seven_date = models.DateField(db_column='seven_date', blank=True, null=True)
    seven_giftdate = models.DateField(db_column='seven_giftdate', blank=True, null=True,
                                      verbose_name=u"Seven-year gift card date")
    eight_year = models.TextField(db_column='eight_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"eight-year survey outcome")
    eight_date = models.DateField(db_column='eight_date', blank=True, null=True)
    eight_giftdate = models.DateField(db_column='eight_giftdate', blank=True, null=True,
                                      verbose_name=u"Eight-year gift card date")
    nine_year = models.TextField(db_column='nine_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"nine-year survey outcome")
    nine_date = models.DateField(db_column='nine_date', blank=True, null=True)
    nine_giftdate = models.DateField(db_column='nine_giftdate', blank=True, null=True,
                                     verbose_name=u"Nine-year gift card date")
    ten_year = models.TextField(db_column='ten_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"ten-year survey outcome")
    ten_date = models.DateField(db_column='ten_date', blank=True, null=True)
    ten_giftdate = models.DateField(db_column='ten_giftdate', blank=True, null=True,
                                    verbose_name=u"Ten-year gift card date")
    eleven_year = models.TextField(db_column='eleven_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"eleven-year survey outcome")
    eleven_date = models.DateField(db_column='eleven_date', blank=True, null=True)
    eleven_giftdate = models.DateField(db_column='eleven_giftdate', blank=True, null=True,
                                       verbose_name=u"Eleven-year gift card date")
    twelve_year = models.TextField(db_column='twelve_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"twelve-year survey outcome")
    twelve_date = models.DateField(db_column='twelve_date', blank=True, null=True)
    twelve_giftdate = models.DateField(db_column='twelve_giftdate', blank=True, null=True,
                                       verbose_name=u"Twelve-year gift card date")
    thirteen_year = models.TextField(db_column='thirteen_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"thirteen-year survey outcome")
    thirteen_date = models.DateField(db_column='thirteen_date', blank=True, null=True)
    thirteen_giftdate = models.DateField(db_column='thirteen_giftdate', blank=True, null=True,
                                         verbose_name=u"Thirteen-year gift card date")
    fourteen_year = models.TextField(db_column='fourteen_year',blank=True, choices=survey_outcome,null=True,verbose_name=u"fourteen-year survey outcome")
    fourteen_date = models.DateField(db_column='fourteen_date', blank=True, null=True)
    fourteen_giftdate = models.DateField(db_column='fourteen_giftdate', blank=True, null=True,
                                         verbose_name=u"Fourteen-year gift card date")
    ipc_outcome1 = Choices('Complete Interview', 'Final Refusal, Respondent','Refused Study Participation, Respondent','NI, Locating Exhausted','NI, Other Reason')
    ipc_outcome2 = Choices('Sent', 'Complete Interview','Partial Complete','Final Refusal, Respondent','Refused Study Participation, Respondent','NI, Locating Exhausted','NI, Other Reason')
    ipc_outcome3 = Choices('Sent', 'Complete Interview','Final Refusal, Respondent','Refused Study Participation, Respondent','NI, Locating Exhausted','NI, Other Reason','Sent, Final Refusal, Respondent')

    #ipc_first = models.TextField(blank=True, choices=ipc_outcome,null=True,verbose_name=u"In-person visit outcome (4-6 years old")
    #ipc_4_6 = models.DateField(db_column='IPC_4_6', blank=True, null=True)  # Field name made lowercase.
    #ipa_4_6_surveysonly = models.DateField(db_column='IPA_4_6_surveysonly', blank=True,
     #                                      null=True)  # Field name made lowercase.
    #ipa1_giftdate = models.DateField(db_column='ipa1_giftdate', blank=True, null=True,
     #                                verbose_name=u"4-6 In-person visit gift card date")
    #ipc_second = models.TextField(blank=True, choices=ipc_outcome,null=True,verbose_name=u"In-person visit outcome (10-12 years old")
    #ipc_10_12 = models.DateField(db_column='IPC_10_12', blank=True, null=True)  # Field name made lowercase.
    #ipa_10_12_surveysonly = models.DateField(db_column='IPA_10_12_surveysonly', blank=True,
    #                                         null=True)  # Field name made lowercase.
    #ipa2_giftdate = models.DateField(db_column='ipa2_giftdate', blank=True, null=True,
    #                                 verbose_name=u"10-12 In-person visit gift card date")
    ec_ipa_out = models.TextField(blank=True, choices=ipc_outcome1, null=True,
                                  verbose_name=u"EC IPA Outcome")
    ec_ipa_date = models.DateField( blank=True, null=True,verbose_name=u"EC IPA Date")
    ec_ipa_date_gc = models.DateField( blank=True, null=True,verbose_name=u"EC IPA GC Date")
    ec_ipa_survey_out = models.TextField(blank=True, choices=ipc_outcome2, null=True,
                                  verbose_name=u"EC IPA survey Outcome")
    ec_ipa_survey_date = models.DateField( blank=True, null=True,verbose_name=u"EC IPA survey Date")
    ec_ipa_survey_gc_date = models.DateField( blank=True, null=True,verbose_name=u"EC IPA survey GC Date")
    ec_vib_out = models.TextField(blank=True, choices=ipc_outcome3, null=True,
                                         verbose_name=u"EC VIB Outcome")
    ec_vib_date = models.DateField( blank=True, null=True,verbose_name=u"EC VIB Date")
    ec_vib_gc_date = models.DateField( blank=True, null=True,verbose_name=u"EC VIB GC Date")

    MC_ipa_out = models.TextField(blank=True, choices=ipc_outcome1, null=True,
                                  verbose_name=u"MC IPA Outcome")
    MC_ipa_date = models.DateField(blank=True, null=True, verbose_name=u"MC IPA Date")
    MC_ipa_date_gc = models.DateField(blank=True, null=True, verbose_name=u"MC IPA GC Date")
    MC_ipa_survey_out = models.TextField(blank=True, choices=ipc_outcome2, null=True,
                                         verbose_name=u"MC IPA survey Outcome")
    MC_ipa_survey_date = models.DateField(blank=True, null=True, verbose_name=u"MC IPA survey Date")
    MC_ipa_survey_gc_date = models.DateField(blank=True, null=True, verbose_name=u"MC IPA survey GC Date")
    MC_vib_out = models.TextField(blank=True, choices=ipc_outcome3, null=True,
                                  verbose_name=u"MC VIB Outcome")
    MC_vib_date = models.DateField(blank=True, null=True, verbose_name=u"MC VIB Date")
    MC_vib_gc_date = models.DateField(blank=True, null=True, verbose_name=u"MC VIB GC Date")
    tooth_1 = models.DateField(blank=True, null=True)
    tooth_1_kit = models.DateField(blank=True, null=True)
    tooth_1_giftdate = models.DateField(db_column='tooth_1_giftdate', blank=True, null=True,
                                        verbose_name=u"First tooth gift card date")
    tooth_2 = models.DateField(blank=True, null=True)
    tooth_2_kit = models.DateField(blank=True, null=True)
    tooth_2_giftdate = models.DateField(db_column='tooth_2_giftdate', blank=True, null=True,
                                        verbose_name=u"Second tooth gift card date")
    tooth_3 = models.DateField(blank=True, null=True)
    tooth_3_kit = models.DateField(blank=True, null=True)
    tooth_3_giftdate = models.DateField(db_column='tooth_3_giftdate', blank=True, null=True,
                                        verbose_name=u"Third tooth gift card date")
    tooth_4 = models.DateField(blank=True, null=True)
    tooth_4_kit = models.DateField(blank=True, null=True)
    tooth_4_giftdate = models.DateField(db_column='tooth_4_giftdate', blank=True, null=True,
                                        verbose_name=u"Fourth tooth gift card date")
    tooth_5 = models.DateField(blank=True, null=True)
    tooth_5_kit = models.DateField(blank=True, null=True)
    tooth_5_giftdate = models.DateField(db_column='tooth_5_giftdate', blank=True, null=True,
                                        verbose_name=u"Fifth tooth gift card date")
    echo_contact_survey = models.DateField(blank=True, null=True)
    #followup_category = models.TextField(blank=True, null=True)
    date_recent = models.DateField(db_column='date_recent',blank=True, null=True,verbose_name=u"Most recent contact date")
    #survey_recent = models.CharField(max_length=255, blank=True, null=True)
    #contact_attempt = models.TextField(blank=True, null=True)
    #call_prefer_choice = Choices('Text', 'Email', 'Call', 'Any')
    #call_prefer = models.CharField(db_column='call_prefer', choices=call_prefer_choice, max_length=80, blank=True,
                     #              null=True, verbose_name=u"Preferred contact method")
    comment = models.TextField(db_column='Comment', max_length=255, blank=True, null=True,verbose_name=u"Comment")
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True,verbose_name=u"Participant category")  # Field name made lowercase.
    mom_firstname = models.CharField(db_column='Mom_FirstName', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    mom_lastname = models.CharField(db_column='Mom_LastName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    babysex = models.CharField(db_column='BabySex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childfirstname = models.CharField(db_column='ChildFirstName', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    childlastname = models.CharField(db_column='ChildLastName', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
   # facebook = models.CharField(db_column='Facebook', max_length=255, blank=True,
                          #      null=True)  # Field name made lowercase.
   # facebook_name = models.CharField(db_column='Facebook_name', max_length=255, blank=True,
                                   #  null=True)  # Field name made lowercase.
    #socialmedia_other_names = models.CharField(db_column='Socialmedia_other_names', max_length=255, blank=True,
           #                                    null=True)  # Field name made lowercase.
    #texting = models.CharField(db_column='Texting', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #texting_number = models.CharField(db_column='Texting_number', max_length=255, blank=True,
                    #                  null=True)  # Field name made lowercase.
    #alt_contact_b_name = models.CharField(db_column='Alt_contact_B_name', max_length=255, blank=True,
           #                               null=True)  # Field name made lowercase.
   # alt_contact_b_number = models.CharField(db_column='Alt_contact_B_number', max_length=255, blank=True,
               #                             null=True)  # Field name made lowercase.
    other_child_in_arch = models.CharField(db_column='Other_Child_in_ARCH', max_length=255, blank=True,
                                           null=True)  # Field name made lowercase.
    #primaryphonenumber = models.CharField(db_column='PrimaryPhoneNumber', max_length=255, blank=True,
                                 #         null=True)  # Field name made lowercase.
    #emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True,
                                 #   null=True)  # Field name made lowercase.
    #mailingaddress = models.CharField(db_column='MailingAddress', max_length=255, blank=True,
                                    #  null=True)  # Field name made lowercase.
    #city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #zipcode = models.CharField(db_column='ZipCode', max_length=25,blank=True, null=True)  # Field name made lowercase.
   # alternatecontact = models.CharField(db_column='AlternateContact', max_length=255, blank=True,
      #                                  null=True)  # Field name made lowercase.
    #alternatephone = models.CharField(db_column='AlternatePhone', max_length=255, blank=True,
                                   #   null=True)  # Field name made lowercase.
   # pcg_spe = models.CharField(db_column='pcg_spe', max_length=60, blank=True,null=True,verbose_name=u"If PCG, please specify")
    checkbbb = Choices('Unknown', 'Yes', 'No','PCG')
    active = models.CharField(choices=checkbbb, default=checkbbb.Unknown, max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'arch_survey_track'
        verbose_name_plural = 'ARCH Survey Track'


class archallcontact(models.Model):
   row_num = models.AutoField(db_column='row_num', primary_key=True)
   ARCHID = models.CharField(max_length=10, db_column='ARCHID', blank=False, null=False,verbose_name=u"ARCH ID")
   currdate = models.DateField( db_column='currdate', blank=False,verbose_name=u"Date of contact information" )
   address = models.TextField( db_column='address', blank=True, null=True,verbose_name=u"Address" )
   choice_social = Choices('Yes', 'No')
   move_home = models.CharField(db_column='move_home',choices=choice_social, max_length=10, blank=True, null=True,
                                verbose_name=u"Plan to move home")
   move_home_address = models.TextField(db_column='move_home_address',blank=True, null=True, verbose_name=u"New address plan to move")
   move_home_date = models.DateField(db_column='move_home_date',blank=True, null=True, verbose_name=u"Date of moving to new home")
   phone_num = models.CharField(max_length=200, db_column='phone_num', blank=True, null=True,verbose_name=u"Primary Phone Number")
   text_permission=models.CharField(max_length=5, db_column='text_permission', blank=True, null=True,verbose_name=u"Permission to text this number")
   text_num = models.CharField(max_length=200, db_column='text_num', blank=True, null=True,verbose_name=u"Phone Number for texting")
   other_phone = models.CharField(max_length=200, db_column='other_phone', blank=True, null=True,verbose_name=u"Additional Phone Number")
   other_text_permission = models.CharField(max_length=5, db_column='other_text_permission', blank=True, null=True,verbose_name=u"Permission to text this number")
   email=models.CharField( max_length=150,db_column='email', blank=True, null=True,verbose_name=u"Email Address" )
   ad_email=models.CharField( max_length=150,db_column='ad_email', blank=True, null=True,verbose_name=u"Additional email Address" )
   prefer_c = Choices('Text', 'Email', 'call', 'Any of the above!')
   prefer_contact = models.CharField(db_column='prefer_contact',choices=prefer_c, max_length=20, blank=True, null=True,
                                     verbose_name=u"Preferred contact method")
   social_media = models.CharField(db_column='social_media',choices=choice_social, max_length=10, blank=True, null=True,
                                   verbose_name=u"Follow social media")
   facebook=models.CharField( max_length=150,db_column='facebook', blank=True, null=True,verbose_name=u"Facebook" )
   Instagram=models.CharField( max_length=150,db_column='Instagram', blank=True, null=True,verbose_name=u"Instagram" )
   Twitter=models.CharField( max_length=150,db_column='Twitter', blank=True, null=True,verbose_name=u"Twitter" )
   contact_a=models.TextField( db_column='contact_a', blank=True, null=True,verbose_name=u"Alternate contact name" )
   contact_aphone=models.CharField(max_length=200, db_column='contact_aphone', blank=True, null=True,verbose_name=u"Phone number of alternate contact")
   contact_aemail=models.CharField(max_length=80, db_column='contact_aemail', blank=True, null=True,verbose_name=u"Email of alternate contact")
   contact_aaddress=models.CharField(max_length=200, db_column='contact_aaddress', blank=True, null=True,verbose_name=u"Mailing address of alternate contact")
   contact_b = models.TextField( db_column='contact_b', blank=True, null=True,verbose_name=u"Other alternate contact name" )
   contact_bphone = models.CharField(max_length=200, db_column='contact_bphone', blank=True, null=True,verbose_name=u"Phone number of other alternate contact")
   source= models.CharField(max_length=30, db_column='source', blank=True, null=True,verbose_name=u"Source of the contact information")
   initial = models.CharField(max_length=10, db_column='initial', blank=True, null=True,verbose_name=u"Please enter your initial")
   qualtrics_id = models.CharField(max_length=50, db_column='qualtrics_id', blank=True, null=True)

   class Meta:
        managed = True
        db_table = 'arch_all_contact'
        verbose_name_plural='ARCH All Contact Information'