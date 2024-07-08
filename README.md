# TutoDjango

Tutoriel de Django

## Initialisation

### Pour initier la machine virtuelle

> Dans "TutoDjango"

`pipenv shell`

### Pour lancer le serveur local

> Dans "TutoDjango"

`python manage.py runserver`

### Pour créer une application prête à l'emploie

> Dans "TutoDjango"

`python manage.py startapp polls`

## Principales fonctions

### include()

> La fonction include() permet de référencer d’autres configurations d’URL. Quand Django rencontre un include(), il tronque le bout d’URL qui correspondait jusque là et passe la chaîne de caractères restante à la configuration d’URL incluse pour continuer le traitement.

```
from django.urls import include, path

urlpatterns = [
    path("lien/", include("liens.clé"))
]
```
