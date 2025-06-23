from modeltranslation.translator import translator,register,TranslationOptions
from .models import *

@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ("name", "text",)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name", "job", "text")

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("name", "review", "text")
