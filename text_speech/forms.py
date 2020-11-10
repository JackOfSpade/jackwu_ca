import django.forms as forms
from django.core.exceptions import ValidationError

voices = (
    ("English", (
        ("Joanna", "     Joanna (US)"),
        ("Matthew", "     Matthew (US)"),
        ("Ivy", "     Ivy (US)"),
        ("Kendra", "     Kendra (US)"),
        ("Kimberly", "     Kimberly (US)"),
        ("Salli", "     Salli (US)"),
        ("Joey", "     Joey (US)"),
        ("Justin", "     Justin (US)"),
        ("Kevin", "     Kevin (US)"),
        ("Amy", "     Amy (British)"),
        ("Emma", "     Emma (British)"),
        ("Brian", "     Brian (British)"),
        ("Nicole", "     Nicole (Australian)"),
        ("Russell", "     Russell (Australian)"),
        ("Raveena", "     Raveena (Indian)"),
        ("Geraint", "     Geraint (Welsh)"),
    )),
    ("Arabic", (
        ("Zeina", "     Zeina"),
    )),
    ("Chinese", (
        ("Zhiyu", "     Zhiyu (Mandarin)"),
    )),
    ("Danish", (
        ("Naja", "     Naja"),
        ("Mads", "     Mads"),
    )),
    ("Dutch", (
        ("Lotte", "     Lotte"),
        ("Ruben", "     Ruben"),
    )),
    ("French", (
        ("Celine", "     Céline"),
        ("Lea", "     Léa"),
        ("Mathieu", "     Mathieu"),
        ("Chantal", "     Chantal (Canadian)"),
    )),
    ("German", (
        ("Marlene", "     Marlene"),
        ("Vicki", "     Vicki"),
        ("Hans", "     Hans"),
    )),
    ("Hindi + English", (
        ("Aditi", "     Aditi"),
    )),
    ("Icelandic", (
        ("Dora", "     Dóra"),
        ("Karl", "     Karl"),
    )),
    ("Italian", (
        ("Carla", "     Carla"),
        ("Bianca", "     Bianca"),
        ("Giorgio", "     Giorgio"),
    )),
    ("Japanese", (
        ("Mizuki", "     Mizuki"),
        ("Takumi", "     Takumi"),
    )),
    ("Korean", (
        ("Seoyeon", "     Seoyeon"),
    )),
    ("Norwegian", (
        ("Liv", "     Liv"),
    )),
    ("Polish", (
        ("Ewa", "     Ewa"),
        ("Maja", "     Maja"),
        ("Jacek", "     Jacek"),
        ("Jan", "     Jan"),
    )),
    ("Portuguese", (
        ("Camila", "     Camila (Brazilian)"),
        ("Vitoria", "     Vitória (Brazilian)"),
        ("Ricardo", "     Ricardo (Brazilian)"),
        ("Ines", "     Inês (European)"),
        ("Cristiano", "     Cristiano (European)"),
    )),
    ("Romanian", (
        ("Carmen", "     Carmen"),
    )),
    ("Russian", (
        ("Tatyana", "     Tatyana"),
        ("Maxim", "     Maxim"),
    )),
    ("Spanish", (
        ("Conchita", "     Conchita (European)"),
        ("Lucia", "     Lucia (European)"),
        ("Enrique", "     Enrique (European)"),
        ("Mia", "     Mia (Mexican)"),
        ("Lupe", "     Lupe (US)"),
        ("Penelope", "     Penélope (US)"),
        ("Miguel", "     Miguel (US)"),
    )),
    ("Swedish", (
        ("Astrid", "     Astrid"),
    )),
    ("Turkish", (
        ("Filiz", "     Filiz"),
    )),
    ("Welsh", (
        ("Gwyneth", "     Gwyneth"),
    )),
)

class input_form(forms.Form):
    # 3000 characters is the max for Amazon Polly API
    text = forms.CharField(label="Text", max_length=3000, widget=forms.Textarea)
    voice = forms.ChoiceField(label="Voice", choices=voices)