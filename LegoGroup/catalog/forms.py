from django import forms

class SearchForm(forms.Form):
    search_by = forms.ChoiceField(choices = (('1', 'Name'), ('2', 'Category'), ('3', 'Subcategory')), required = False)
    search_string = forms.CharField(label = 'Search string', max_length = 100, required = False, help_text = 'Type here')
