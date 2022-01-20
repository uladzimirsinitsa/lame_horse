    
from pytils.translit import slugify


def unique_slug_generator(instance, field):
    model = instance.__class__
    max_length = model._meta.get_field('slug').max_length
    slug = orig = slugify(field)[:max_length]

    return slug



