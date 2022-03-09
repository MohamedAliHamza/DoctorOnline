# from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core.exceptions import ValidationError

# from .models import User


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'bio', 'avatar')

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         user.is_doctor=True
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('email', 'password', 'full_name', 'bio', 'avatar', 'is_active', )


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     list_display = ('email', 'full_name',)
#     list_filter = ()
#     fieldsets = (
#         (None, {
#             'fields': ('email', 'password', 'full_name', 'bio', 'avatar', 'created_at',)
#         }),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'full_name', 'bio', 'avatar', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ()
#     ordering = ('-created_at',)


# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
