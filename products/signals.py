from django.utils.text import slugify
from django.db.models import Q
from django.db.models.signals import pre_save
from django.dispatch import receiver
from . import models



@receiver(pre_save, sender=models.Brand)
@receiver(pre_save, sender=models.Category)
@receiver(pre_save, sender=models.Product)
def set_unique_slug(sender, instance, *args, **kwargs):
    Klass = instance.__class__  

    # when we have the same two slugs, it will stick current id of instance to end of slug.
    def stick_id_to_end(slug):
        id = Klass.objects.latest('id').pk + 1
        slug = f"{slug}-{id}"
        return slug

    # admin has not left any slug so it set slug auto based on 'name' field.
    if not instance.slug:
        instance.slug = slugify(instance.name, allow_unicode=True)
        if Klass.objects.filter(slug=instance.slug).exists():
            instance.slug = stick_id_to_end(instance.slug)
        return super(Klass, instance)
        
    # when admin leave a slug.
    instance.slug = slugify(instance.slug, allow_unicode=True)
    if Klass.objects.filter(~Q(id=instance.id), slug=instance.slug).exists():      # ~Q(id=instance.id) --> every objects of class(model) except itself
        instance.slug = stick_id_to_end(instance.slug)
    return super(Klass, instance)