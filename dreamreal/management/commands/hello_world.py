from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('[#] Begin execute...')
        try:
            self.stdout.write('[#] Hello World!')
        except Exception as e:
            print('Error:', e)
        self.stdout.write('[#] DONE!')

