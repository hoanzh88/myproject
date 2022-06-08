from django.conf import settings
from django.core.management.base import BaseCommand
from gripcontrol import HttpStreamFormat
from django_grip import publish

def sse_encode(data):
	out = 'event: message\n'
	for line in data.split('\n'):
		out += 'data: %s\n' % line
	out += '\n'
	return out

class Command(BaseCommand):
	help = 'Relay events from Kafka to GRIP proxy.'

	def handle(self, *args, **options):
		# while True:
		publish('test', HttpStreamFormat('hello world\n'))
	
