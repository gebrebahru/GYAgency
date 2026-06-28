from django.db import models

class Asset(models.Model):
    CATEGORY_CHOICES = [
        ('house_sale', 'የቤት/መሬት ሽያጭ (ሻጭና ገዢ)'),
        ('house_rent', 'የቤት ኪራይ (አከራይና ተከራይ)'),
        ('car_sale', 'የመኪና ሽያጭ'),
        ('land_sale', 'የቦታ ሽያጭ'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="የንብረቱ ስም/ሞዴል")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name="የአገልግሎት አይነት")
    location = models.CharField(max_length=100, verbose_name="ቦታ/አድራሻ")
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="ዋጋ (በብር)")
    phone_number = models.CharField(max_length=20, verbose_name="ባለቤት/ሻጭ ስልክ ቁጥር")
    image = models.ImageField(upload_to='assets/', blank=True, null=True, verbose_name="የንብረቱ ምስል (ፎቶ)")
    description = models.TextField(blank=True, null=True, verbose_name="ዝርዝር መግለጫ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="የተለጠፈበት ቀን")
    is_paid = models.BooleanField(default=False, verbose_name="ክፍያ ተፈጽሟል?")
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")

    def __str__(self):
        return f"[{self.get_category_display()}] - {self.title}"
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")


class Worker(models.Model):
    WORKER_TYPE_CHOICES = [
        ('local', 'የሀገር ውስጥ ሰራተኛ (አሰሪና ሰራተኛ)'),
        ('foreign', 'የውጭ ሀገር ሰራተኛ (አሰሪና ሰራተኛ)'),
    ]
    SKILL_CHOICES = [
        ('domestic', 'የቤት ስራ / ምግብ አሰራር'),
        ('driver', 'ሹፌር'),
        ('caregiver', 'ህጻናት/አረጋውያን ተንካባካቢ'),
        ('guard', 'ዘበኛ/ጥበቃ'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="የሰራተኛው ሙሉ ስም")
    worker_type = models.CharField(max_length=20, choices=WORKER_TYPE_CHOICES, verbose_name="የስራ ሁኔታ")
    skill = models.CharField(max_length=20, choices=SKILL_CHOICES, verbose_name="የሙያ አይነት")
    age = models.IntegerField(verbose_name="እድሜ")
    passport_or_id = models.CharField(max_length=30, verbose_name="የፓስፖርት ወይም የመታወቂያ ቁጥር")
    price_or_salary = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="ደመወዝ / የኤጀንሲ ዋጋ")
    phone_number = models.CharField(max_length=20, verbose_name="የሰራተኛው ስልክ ቁጥር")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="የተለጠፈበት ቀን")
    is_paid = models.BooleanField(default=False, verbose_name="ክፍያ ተፈጽሟል?")
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")

    def __str__(self):
        return f"[{self.get_worker_type_display()}] - {self.name}"
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")


class EmployerRequirement(models.Model):
    JOB_TYPE_CHOICES = [
        ('local', 'የሀገር ውስጥ'),
        ('foreign', 'የውጭ ሀገር'),
    ]
    REQUIRED_SKILL_CHOICES = [
        ('domestic', 'የቤት ስራ / ምግብ አሰራር'),
        ('driver', 'ሹፌር'),
        ('caregiver', 'ህጻናት/አረጋውያን ተንካባካቢ'),
        ('guard', 'ዘበኛ/ጥበቃ'),
    ]
    
    employer_name = models.CharField(max_length=100, verbose_name="የቀጣሪው/አሰሪው ሙሉ ስም")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, verbose_name="የስራ ሁኔታ")
    required_skill = models.CharField(max_length=20, choices=REQUIRED_SKILL_CHOICES, verbose_name="የሚፈለገው ሙያ")
    gender_preference = models.CharField(max_length=20, choices=[('M', 'ወንድ'), ('F', 'ሴት'), ('any', 'አይለይም')], verbose_name="የፆታ ምርጫ") # <-- እዚህ ጋር ተስተካክሏል
    offered_salary = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="የሚከፍሉት ደመወዝ (ብር)")
    location = models.CharField(max_length=100, verbose_name="የስራ ቦታ/አድራሻ")
    phone_number = models.CharField(max_length=20, verbose_name="የአሰሪው ስልክ ቁጥር (ለአድሚን ብቻ)")
    other_requirements = models.TextField(blank=True, null=True, verbose_name="ተጨማሪ መስፈርቶች (ካሉ)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="የተመዘገበበት ቀን")
    is_paid = models.BooleanField(default=False, verbose_name="ክፍያ ተፈጽሟል?")
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")

    def __str__(self):
        return f"[ቀጣሪ] {self.employer_name} - {self.get_required_skill_display()}"
    views_count = models.PositiveIntegerField(default=0, verbose_name="የእይታ ብዛት")