from django.utils.text import slugify
from django.db.models import Q



# logic for set auto slug
def set_product_slug(sender, instance, *args, **kwargs):
    # get the class of instance
    global klass
    klass = instance.__class__

    # theory one: when slug field set manually by admin
    if instance.slug:
        instance.slug = slugify(instance.slug, allow_unicode=True)
        if instance.id == None and klass.objects.filter(~Q(id=instance.id), slug=instance.slug).exists():
            latest_id = klass.objects.latest('id').id
            instance.slug = slugify(f'{instance.slug}-{latest_id + 1}', allow_unicode=True)
        if klass.objects.filter(~Q(id=instance.id), slug=instance.slug).exists():
            instance.slug = slugify(f'{instance.slug}-{instance.id}', allow_unicode=True)

    # theory two: when slug field leave without slug (auto slug based on something field you wnat)
    if not instance.slug:
        def unique_slug(instance, new_slug = None):
            if new_slug is not None:
                slug = new_slug
            else:
                slug = slugify(instance.name, allow_unicode=True)    # instead 'name' you can set a field that you want to slug set based on it.
            try:z
                if instance.id == None:
                    id = klass.objects.latest('id').id + 1
                if instance.id != None:
                    id = instance.id
            except:
                id = '1'
            qs_exist = klass.objects.filter(~Q(id=instance.id), slug=slug).exists()
            if qs_exist:
                new_slug = f'{slug}-{id}'
                return unique_slug(instance, new_slug=new_slug)
            return slug
        instance.slug = unique_slug(instance)

    # finally return instance with slug
    return super(klass, instance)