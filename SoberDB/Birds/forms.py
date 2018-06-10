# from django import forms
# from .models import Finch


class FinchEditForm(forms.Form):
    pLocation = forms.CharField(label = 'Location',max_length = 30)
    Procedure = forms.ChoiceField(label = 'Procedure')
    Experimenter = forms.ChoiceField(label = 'Experimenter')
    Notes = forms.CharField(label = 'Notes')
    Procedures = forms.ChoiceField(label = 'Procedures')



	# finch = forms.CharField()
	# class Meta:
	# 	model = Finch
	# 	fields = ('Location','Procedure','Notes','Experimenter',)


	# d(label='locaton?', max_length=100, widget=forms.Textarea())
	# def clean(self):
	# 	cleaned_data=super(FinchForm, self).clean()
	# 	name=cleaned_data.get('new_location')
	# 	if not name:
	# 		raise forms.ValidationError('You have blah')



	# class Meta:
	# 	model = Finch
	# 	fields = ('Location,Procedure,Notes,Alive,Experimenter')
