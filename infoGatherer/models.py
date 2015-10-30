from django.db import models
from django_countries.fields import CountryField
from django_languages.fields import LanguageField
from localflavor.us.models import USStateField, USSocialSecurityNumberField, PhoneNumberField
from django.utils import timezone
from audit_log.models.managers import AuditLog

GENDER_CHOICES = (('Female', 'Female'), ('Male', 'Male'), ('Undifferentiated', 'Undifferentiated'), ('Blank', ''))

RACE_CHOICES = (('American Indian or Alaska Native', 'American Indian or Alaska Native'), \
                ('Asian', 'Asian'), \
                ('Black or African American', 'Black or African American'), \
                ('Hispanic or Latino', 'Hispanic or Latino'), \
                ('Native Hawaiian or Other Pacific Islander','Native Hawaiian or Other Pacific Islander'), \
                ('White', 'White'),\
                ('PD', 'Patient Declined'), ('Blank', ''))

ETHNICITY_CHOICES = (('Hispanic or Latino', 'Hispanic or Latino'), \
                     ('Not Hispanic or Latino', 'Not Hispanic or Latino'), \
                     ('PD', 'Patient Declined'), ('Blank', ''))

EMP_STATUS_CHOICES = (('Employed','Employed'),('Unemployed','Unemployed'),\
                      ('Full-Time Student','Full-Time Student'), \
                      ('Part-Time Student','Part-Time Student'), \
                      ('Other','Other'),('Retired','Retired'),('Child','Child'),('Blank',''))

CALL_PREF_CHOICES = (('Home','Home Phone'),('Cell','Cell Phone'))

WRITTEN_PREF_CHOICES = (('Email','Email'),('Post','Postal Mail'))

ACCOUNT_TYPE_CHOICES = (('9','09: Self-pay'),
('10','10: Central Certification'),
('11','11: Other Non-Federal Programs'),
('12','12: Preferred Provider Org. (PPO)'),
('13','13: Point of Service (POS)'),
('14','14: Exclusive Provider Org. (EPO)'),
('15','15: Indemnity Insurance'),
('16','16: Health Maintenance Org. (HMO)'),
('AM','AM: Automobile Medical'),
('BL','BL: Blue Cross/Blue Shield'),
('CH','CH: Champus'),
('CI','CI: Commercial Insurance Co.'),
('DS','DS: Disability'),
('HM','HM: Health Maintenance Org.'),
('LI','LI: Liability'),
('LM','LM: Liability Medical'),
('MB','MB: Medicare Part B'),
('MC','MC: Medicaid'),
('OF','OF: Other'),
('TV','TV: Title V'),
('VA','VA: Veteran Administration Plan'),
('WC','WC: Workers Compensation'),
('Blank','')
)

ACCOUNT_STATUS_CHOICES = (('Current','Current'),('Archived','Archived'))

SIGN_CHOICES = (('Yes','Yes'),('No','No'))

INSURANCE_LEVEL_CHOICES = (('Primary','Primary'),('Secondary','Secondary'),('Tertiary','Tertiary'))

INSURANCE_STATUS_CHOICES = (('Active','Active'),('Inactive','Inactive'),('Invalid','Invalid'),('Not Found','Not Found')) 

PAYER_TYPE_CHOICE = (('M','Medicare'),('C','Commercial'))

RELATION_CHOICES = (('Self','Self'),('Other','Other'))
  
class Personal_Information(models.Model):
    first_name = models.CharField(max_length=128, default='')
    middle_name = models.CharField(max_length=128, default='', null=True, blank=True)
    last_name = models.CharField(max_length=128, default='')
    dob = models.DateField()
    sex = models.CharField(choices=GENDER_CHOICES, max_length=32, default='Blank')
    race = models.CharField(choices=RACE_CHOICES, max_length=64, default='Blank')
    ethnicity = models.CharField(choices=ETHNICITY_CHOICES, max_length=64, default='Blank')
    language = LanguageField(default='en')
    country = CountryField(blank_label='',default='US')
    ssn = USSocialSecurityNumberField(null=True, blank=True, help_text='XXX-XX-XXXX')
    address = models.CharField(max_length=128,default='')
    city = models.CharField(max_length=128,default='')   
    state = USStateField(default='')  
    zip = models.IntegerField(default='')
    home_phone = PhoneNumberField(help_text='XXX-XXX-XXXX')
    cell_phone = PhoneNumberField(null=True, blank=True, help_text='XXX-XXX-XXXX')
    email = models.EmailField(null=True, blank=True)
    call_pref = models.CharField(choices=CALL_PREF_CHOICES, max_length=10, default='Home')
    written_pref = models.CharField(choices=WRITTEN_PREF_CHOICES, max_length=12, default='Post')
    emp_status = models.CharField(choices=EMP_STATUS_CHOICES, max_length=64, default='Blank')    
     
    #Account Information
    chart_no = models.AutoField(primary_key=True)
    date_registered = models.DateField(default=timezone.now)
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES, max_length=64, default='Blank')
    account_status = models.CharField(choices=ACCOUNT_STATUS_CHOICES, max_length=64, default='Current')
    sign = models.CharField(choices=SIGN_CHOICES, max_length=3, default='Yes')
     
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.first_name+' '+self.last_name

class Guarantor_Information(models.Model):
    patient = models.ForeignKey(Personal_Information)
    relation = models.CharField(choices=RELATION_CHOICES,max_length=128)
    
    #If relation is self, auto fill rest of the details
    first_name = models.CharField(max_length=128, default='')
    middle_name = models.CharField(max_length=128, default='', null=True, blank=True)
    last_name = models.CharField(max_length=128, default='')
    dob = models.DateField()
    sex = models.CharField(choices=GENDER_CHOICES, max_length=32, default='Blank')
    race = models.CharField(choices=RACE_CHOICES, max_length=64, default='Blank')
    ethnicity = models.CharField(choices=ETHNICITY_CHOICES, max_length=64, default='Blank')
    language = LanguageField(default='en')
    country = CountryField(blank_label='',default='US')
    ssn = USSocialSecurityNumberField(null=True, blank=True, help_text='XXX-XX-XXXX')
    address = models.CharField(max_length=128,default='')
    city = models.CharField(max_length=128,default='')   
    state = USStateField(default='')  
    zip = models.IntegerField(default='')
    home_phone = PhoneNumberField(help_text='XXX-XXX-XXXX')
    
    def __unicode__(self):
        return self.patient+' '+self.relation
    
class Payer(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, default='')
    address = models.CharField(max_length=256, default='')
    city = models.CharField(max_length=128,default='')   
    state = USStateField(default='')  
    zip = models.IntegerField(default='')
    phone = PhoneNumberField(null=True, blank=True, help_text='XXX-XXX-XXXX')
    type = models.CharField(choices=PAYER_TYPE_CHOICE,max_length=1,default='C')
    
    def __unicode__(self):
        return self.name
    
class Insurance_Information(models.Model):
    level = models.CharField(choices=INSURANCE_LEVEL_CHOICES,max_length=10,default='Primary')
    status = models.CharField(choices=INSURANCE_STATUS_CHOICES,max_length=10,default='Active')
    payer = models.ForeignKey(Payer)
    patient = models.ForeignKey(Personal_Information)
    insurance_id = models.CharField(max_length=32,default='')
    
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.payer.name 
