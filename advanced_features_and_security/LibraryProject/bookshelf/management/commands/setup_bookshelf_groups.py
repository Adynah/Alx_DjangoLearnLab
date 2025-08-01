from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up bookshelf groups with permissions'

    def handle(self, *args, **kwargs):
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        book_ct = ContentType.objects.get_for_model(Book)

        # Match your model's custom permissions
        can_create = Permission.objects.get(codename='can_create', content_type=book_ct)
        can_edit = Permission.objects.get(codename='can_edit', content_type=book_ct)
        can_delete = Permission.objects.get(codename='can_delete', content_type=book_ct)

        editors.permissions.set([can_create, can_edit])
        viewers.permissions.clear()  # You can assign can_view if needed
        admins.permissions.set([can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully."))
