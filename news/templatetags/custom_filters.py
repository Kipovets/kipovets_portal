from django import template
from news.resources import SWEAR_WORDS


register = template.Library()


@register.filter()
def censor(text: str):
    new_text = text
    for one_word in SWEAR_WORDS:
        if new_text.lower().find(one_word):
            new_text = new_text.replace(one_word, f' {one_word[:1]}{(len(one_word)-1)*"*"}', new_text.count(one_word))
    return f'{new_text}'
