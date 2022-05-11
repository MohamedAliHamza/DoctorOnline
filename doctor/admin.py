from django.contrib import admin
from .models import Doctor, ClinicDuration
from user.models import User
from django import forms

 
admin.site.register(Doctor)
admin.site.register(ClinicDuration)

# class DoctorForm(forms.ModelForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = Doctor 
#         fields  = ['email', 'password1', 'password2', 'full_name', 'avatar','fees','phone', 'specialty', 'bio'] 


# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     form =  DoctorForm 

#     list_display = ['full_name', 'email']
#     list_per_page = 10
#     readonly_fields = ['created_at', 'updated_at']

#     raw_id_fields = ["specialty"]

#     def save_model(self, request, obj, form, change):
#         user = User.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
#         obj.user = user
#         super().save_model(request, obj, form, change)


# @admin.register(ClinicDuration)
# class DurationAdmin(admin.ModelAdmin):

#     list_display = ['get_doctor', 'day', 'start_at', 'end_at']
#     list_per_page = 10
#     # readonly_fields = ['created_at', 'updated_at']
