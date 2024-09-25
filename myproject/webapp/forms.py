from django import forms

class SubmissionForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Example validation: check if email domain is valid
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the domain 'example.com'")
        return email
