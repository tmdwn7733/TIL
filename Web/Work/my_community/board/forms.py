from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label='제목',
      error_messages={
        'required': '제목을 입력해 주세요'
      })

    contents = forms.CharField(label='내용',
      error_messages={
        'required': '내용을 입력해 주세요'
      })
    
    tags =  forms.CharField(
      required=False, # 반드시 입력할 필요는 없기 때문에 required=False
      label="태그")