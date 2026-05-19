from django import forms
from .models import Projeto, UnidadeCurricular, TFC, Tecnologia, Docente, Licenciatura, Formacao, Competencia, MakingOf

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

    def clean_video_demo(self):
        video_demo = self.cleaned_data.get('video_demo')
        if video_demo and not video_demo.startswith(('http://', 'https://')):
            video_demo = 'https://' + video_demo
        return video_demo

    def clean_github(self):
        github = self.cleaned_data.get('github')
        if github and not github.startswith(('http://', 'https://')):
            github = 'https://' + github
        return github

class UnidadeCurricularForm(forms.ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = '__all__'

class TFCForm(forms.ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class MakingOfForm(forms.ModelForm):
    class Meta:
        model = MakingOf
        fields = '__all__'
