from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            nickname = self.cleaned_data['nickname'],
            )
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('mismatched')
        return answer

    '''
    answer = forms.CharField(label = '이제우는 구데기?(Y/N)')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer',None)

        if answer != 'Y':
            raise forms.ValidationError('구데기 맞습니다')

        return answer
        '''