# TutoDjango

Tutoriel de Django

## Initialisation

### Pour initier la machine virtuelle

`pipenv shell`

### Pour lancer le serveur local

`python manage.py runserver`

### Pour créer une application prête à l'emploie

`python manage.py startapp polls`

### Pour créer les tables de la base de donnée // Pour appliquer les changements de models.py

> Définies dans project>settings.py>INSTALLED_APPS

`python manage.py migrate`

### Pour appliquer les changements des modèles

`python manage.py makemigrations polls`

### Shell intéractif python

> Permet d'éviter de taper 'python' devant la ligne de commande et de lancer un environnement où l'on peut ajouter/modifer des entrées dans la DB

`python manage.py shell`

### Créer un superuser

`python manage.py createsuperuser`

## Principales fonctions

### include()

La fonction include() permet de référencer d’autres configurations d’URL. Quand Django rencontre un include(), il tronque le bout d’URL qui correspondait jusque là et passe la chaîne de caractères restante à la configuration d’URL incluse pour continuer le traitement.
Il faut toujours utiliser include() lorsque l’on veut inclure d’autres motifs d’URL. admin.site.urls est la seule exception à cette règle.

```
from django.urls import include, path

urlpatterns = [
    path("lien/", include("liens.clé"))
]
```

### path()

La fonction path() reçoit quatre paramètres, dont deux sont obligatoires : route et view, et deux facultatifs : kwargs et name. À ce stade, il est intéressant d’examiner le rôle de chacun de ces paramètres.

> Paramètre de path() : route¶

route est une chaîne contenant un motif d’URL. Lorsqu’il traite une requête, Django commence par le premier motif dans urlpatterns puis continue de parcourir la liste en comparant l’URL reçue avec chaque motif jusqu’à ce qu’il en trouve un qui correspond.

Les motifs ne cherchent pas dans les paramètres GET et POST, ni dans le nom de domaine. Par exemple, dans une requête vers https://www.example.com/myapp/, l’URLconf va chercher myapp/. Dans une requête vers https://www.example.com/myapp/?page=3, l’URLconf va aussi chercher myapp/.

Paramètre de path() : view¶

Lorsque Django trouve un motif correspondant, il appelle la fonction de vue spécifiée, avec un objet HttpRequest comme premier paramètre et toutes les valeurs « capturées » par la route sous forme de paramètres nommés. Nous montrerons cela par un exemple un peu plus loin.

Paramètre de path() : kwargs¶

Des paramètres nommés arbitraires peuvent être transmis dans un dictionnaire vers la vue cible.

Paramètre de path() : name¶

Le nommage des URL permet de les référencer de manière non ambiguë depuis d’autres portions de code Django, en particulier depuis les gabarits. Cette fonctionnalité puissante permet d’effectuer des changements globaux dans les modèles d’URL de votre projet en ne modifiant qu’un seul fichier.

### Modifications de modèles

Modifiez les modèles (dans models.py).

Exécutez `python manage.py makemigrations` pour créer des migrations correspondant à ces changements.

Exécutez `python manage.py migrate` pour appliquer ces modifications à la base de données`

### Ajout de questions dans la DB

Se placer sur l'environnement virtuel :
`python manage.py shell`

Importer les objets :
`from polls.models import Choice, Question`

Importer le temps :
`from django.utils import timezone`

Créer un nouvel objet et y ajouter l'heure de publication :
`q = Question(question_text="What's new?", pub_date=timezone.now())`

Enregistrer l'objet dans la DB :
`q.save()`

Vérifier son ID :
`q.id`

Vérifier le contenu de l'objet' :
`q.question_text`

Vérifier la date de publication :
`q.pub_date`

Modifier le contenu de l'objet :
`q.question_text = "What's up?"`

Ne pas oublier d'enregistrer l'objet après chaque modification.

Filtrer les objets, ici avec un ID :
`Question.objects.filter(id=1)`

Afficher les objets publiés selon une année :

```
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
```

Filtrer par key primaire (pk = primary key) :
`Question.objects.get(pk=1)`

Entrée une réponse associée à la question :
`q.choice_set.create(choice_text="Not much", votes=0)` ou `c = q.choice_set.create(choice_text="Just hacking again", votes=0)`

Affiche toutes les valeurs du choix :
`q.choice_set.all()`

Compte le nombre d'entrés :
`q.choice_set.count()`

Effacter une entrée (variable) :
`c.delete()`
