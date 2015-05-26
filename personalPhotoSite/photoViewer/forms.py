from django import forms

class PhotoUploadForm (forms.Form):
    photo_img  = forms.ImageField(label="Select a Profile Image")
    photo_title = forms.CharField(max_length=20)
    date_taken = forms.DateField(label='date taken')