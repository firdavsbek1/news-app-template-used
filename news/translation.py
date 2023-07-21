from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions,translator
from .models import News,Category


@register(News)
class NewsTranslationModel(TranslationOptions):
    fields=\
        ('title','body',)
