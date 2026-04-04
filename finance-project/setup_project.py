from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'One-click setup for the recruiter'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting setup...")
        call_command('migrate')
        call_command('loaddata', 'seed_data.json')
        self.stdout.write(self.style.SUCCESS("Done! Project is ready to test."))