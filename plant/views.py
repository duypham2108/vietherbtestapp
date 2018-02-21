from django.http import Http404
from .models import Plant, TherapeuticEffects, Distribution
from django.shortcuts import render

def index(request):
	all_plants = Plant.objects.all()
	return render(request, 'plant/index.html', {'all_plants': all_plants})

def detail(request, plant_id):
	try:
		plant = Plant.objects.get(pk=plant_id)
		thera = plant.planthastherapeuticeffects_set.all()
		# Therapeutic effects
		effects = []
		for effect in thera:
			effects.append(TherapeuticEffects.objects.get(thera_id = effect.thera_id))

		# Distribution
		distribution = plant.planthasdistribution_set.all()	
		distri = []
		for dis in distribution:
			distri.append(Distribution.objects.get(distribution_id = dis.distribution_id))

	except Plant.DoesNotExist:
		raise Http404("Plant does not exist")
	return render(request, 'plant/detail.html',{'plant': plant, 'effects': effects, 'distri': distri})