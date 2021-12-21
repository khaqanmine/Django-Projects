from django import forms

class groceryBill(forms.Form):
    product_oil = forms.IntegerField(label='Oil',widget=forms.TextInput(attrs={'class':'form-control'}))
    product_sugar = forms.IntegerField(label='Sugar',widget=forms.TextInput(attrs={'class':'form-control'}))
    product_flour = forms.IntegerField(label='Flour',widget=forms.TextInput(attrs={'class':'form-control'}))

class checkEvenOdd(forms.Form):
    number = forms.IntegerField(label='Enter Number:',widget=forms.TextInput(attrs={'class':'form-control'}))

class StudentData(forms.Form):
    student_name = forms.CharField(label='Student Name', required=True)
    student_roll_number = forms.CharField(label='Student Roll Number', required=True)
    student_gender = forms.CharField(label='Student Gender', required=True)
    student_fathername = forms.CharField(label='Student FatherName', required=True)

# class teacherd(forms.Form):
#     name = forms.CharField(label='Teacher Name', required=True)
#     phone = forms.CharField(label='Teacher Phone', required=True)
#     address = forms.CharField(label='Teacher Gender', required=True)
#     salary = forms.CharField(label='Salary', required=True)


