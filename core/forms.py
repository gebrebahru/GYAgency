from django import forms
from .models import Asset, Worker, EmployerRequirement  # <--- EmployerRequirement እዚህ ጋር መኖሩን ያረጋግጣል

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['title', 'category', 'location', 'price', 'phone_number', 'image', 'description']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'worker_type', 'skill', 'age', 'passport_or_id', 'price_or_salary', 'phone_number']

# አዲሱ የቀጣሪዎች ፎርም
class EmployerRequirementForm(forms.ModelForm):
    class Meta:
        model = EmployerRequirement
        fields = ['employer_name', 'job_type', 'required_skill', 'gender_preference', 'offered_salary', 'location', 'phone_number', 'other_requirements']