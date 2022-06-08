from django.shortcuts import render
from django.http import HttpResponse
from .models import Dreamreal
from kafka import KafkaConsumer
from django_grip import set_hold_stream, publish

from gripcontrol import HttpStreamFormat
# from django_grip import publish

TOPIC_NAME = "sample"
KAFKA_SERVER = "localhost:9092"

consumer = KafkaConsumer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)

# for message in consumer:
	# print (message.value)
# Create your views here.
def index(request):
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app home')

   return response

def list(request):
   response = HttpResponse()
   response.write('list')

   # Creating an entry
   # dreamreal = Dreamreal(
   #    website="www.polo.com", mail="sorex@polo.com",
   #    name="HoanChuong", phonenumber="002376970", mydata="{abc:222}"
   # )
   # dreamreal.save()

   # Update
   # dreamreal = Dreamreal.objects.get(name='sorex')
   # dreamreal.name = 'thierry'
   # dreamreal.save()

   # sorex = Dreamreal.objects.get(name="thierry")
   # sorex.delete()


   # Read ALL entries
   objects = Dreamreal.objects.all()
   res = 'Printing all Dreamreal entries in the DB : <br>'

   for elt in objects:
      res += elt.name + "<br>"
   # return response
   return HttpResponse(res)

def endpoint(request):
    set_hold_stream(request, 'test')
    return HttpResponse(content_type='text/event-stream')
    # return HttpResponse('[stream open]\n')
	
def publishdata(request):
	publish('test', HttpStreamFormat('hello world\n'))
	formats = []
	formats.append(HttpStreamFormat('Toi ten Hoan\n'))
	# formats.append(WebSocketMessageFormat(hjson))
	publish('test', formats)
	
	response = HttpResponse()
	response.write('Đây là app home')
	return response
	
def sse_encode(data):
	out = 'event: message\n'
	for line in data.split('\n'):
		out += 'data: %s\n' % line
	out += '\n'
	return out