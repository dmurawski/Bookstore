from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)
    from_email = forms.EmailField(
        label="From email",
    )
