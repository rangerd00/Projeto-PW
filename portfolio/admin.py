

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Post, Noticias, TrabalhosFinaisCurso, TecnologiasInteressantes

from .models import Quizz
from .models import Pessoa
from .models import Projetos
from .models import UnidadesCurriculares

from .models import Tecnologias
from .models import Tecnicas
from .models import Padroes
admin.site.register(Post)

admin.site.register(Quizz)
admin.site.register(Pessoa)
admin.site.register(Projetos)
admin.site.register(UnidadesCurriculares)
admin.site.register(Noticias)
admin.site.register(Tecnologias)
admin.site.register(Padroes)
admin.site.register(Tecnicas)
admin.site.register(TrabalhosFinaisCurso)
admin.site.register(TecnologiasInteressantes)
