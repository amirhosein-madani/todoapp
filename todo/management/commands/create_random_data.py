from django.core.management.base import BaseCommand
from faker import Faker
from random import choice
from accounts.models import MyUser as User, Profile
from ...models import Task


class Command(BaseCommand):
    """
    this is a custom command class to create
     a user with five random tasks with different status
    """

    help = "creating random users and tasks"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):

        user = User.objects.create_user(
            username=self.fake.user_name(),
            password=self.fake.password(),
            email=self.fake.email(),
        )

        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.date_of_birth = self.fake.date_of_birth()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for _ in range(5):

            Task.objects.create(
                user=user.profile,
                title=self.fake.text(),
                is_complete=choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS("Created a user with 5 tasks."))
