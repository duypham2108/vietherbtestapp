from __future__ import absolute_import, unicode_literals
from .models import Plant, TherapeuticEffects, Distribution, Metabolite, Familia, Genus
from django.template.response import TemplateResponse


import string
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http.response import HttpResponse

from .tables import LinkColumnTable, MetaboliteTable

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
	return render(request, 'plant/index.html')

def contact(request):
	return render(request, 'plant/contact.html')

def aboutus(request):
	return render(request, 'plant/aboutus.html')

def herbs(request, query=''):
	table_herbs = LinkColumnTable()
	return render(request, "plant/herbs.html", {'table': table_herbs, 'query':query})

def metabolites(request):
	table_metabolites = MetaboliteTable()
	return render(request, "plant/metabolites.html", {'table': table_metabolites}) 

def detailherb(request,plant_id):
	try:
		plant = Plant.objects.get(pk=plant_id)
	except Plant.DoesNotExist:
		raise Http404("Plant does not exist")

	meta = plant.planthasmetabolite_set.all().distinct()
	thera = plant.planthastherapeuticeffects_set.all().distinct()
	loca = plant.planthasdistribution_set.all().distinct()
	morpho = plant.planthasmorphology_set.all().distinct()
	from collections import defaultdict
	def tree(): return defaultdict(tree)
	mor_dict = tree()
	for mor in morpho:
		mor_dict[mor.morpho.lv1][mor.morpho.lv2][mor.morpho.lv3] = mor.morpho.verb
	def default_to_regular(d):
	    if isinstance(d, defaultdict):
	        d = {k: default_to_regular(v) for k, v in d.items()}
	    return d


	return render(request, 'plant/detailherb.html', {'plant':plant,'meta':meta,'thera':thera,'loca':loca, 'morpho':default_to_regular(mor_dict)})

def detailmetabolite(request,metabolite_id):
	try:
		metabolite = Metabolite.objects.get(pk=metabolite_id)
	except Metabolite.DoesNotExist:
		raise Http404("Metabolite does not exist")
	setplant = metabolite.planthasmetabolite_set.values_list()
	plant = []
	for pl,mt in setplant:
		plant.append(Plant.objects.get(pk=pl))
	plant = set(plant)

	return render(request, 'plant/detailmetabolite.html', {'metabolite':metabolite, 'plant':plant})

def detailfamilia(request,familia_id):
	try:
		familia = Familia.objects.get(pk=familia_id)
	except Familia.DoesNotExist:
		raise Http404("Familia does not exist")
	setplant = familia.plant_set.values_list()
	plant = []
	for pl in setplant:
		plant.append((Plant.objects.get(pk=pl[0]).plant_engname,Plant.objects.get(pk=pl[0]).plant_id))
	plant = set(plant)

	genus =[]
	for ge in setplant:
		genus.append((Plant.objects.get(pk=ge[0]).genus,Plant.objects.get(pk=ge[0]).genus_id))
	genus = set(genus)

	return render(request, 'plant/detailfamilia.html', {'familia':familia, 'plant':plant, 'genus':genus})


def detailgenus(request,genus_id):
	try:
		genus = Genus.objects.get(pk=genus_id)
	except Genus.DoesNotExist:
		raise Http404("Familia does not exist")
	setplant = genus.plant_set.values_list()
	plant = []
	for pl in setplant:
		plant.append((Plant.objects.get(pk=pl[0]).plant_engname,Plant.objects.get(pk=pl[0]).plant_id))
	plant = set(plant)

	familia =[]
	for fa in setplant:
		familia.append((Plant.objects.get(pk=fa[0]).familia,Plant.objects.get(pk=fa[0]).familia_id))
	familia = set(familia)

	return render(request, 'plant/detailgenus.html', {'genus':genus, 'plant':plant, 'familia':familia})


def search_titles(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
		if search_text > '':
			plants = Plant.objects.filter(plant_engname__icontains=search_text) 
		else:
			plants = Plant.objects.none()
			text = 1
	else:
		search_text = ""

	
	return render(request,'plant/ajax_search.html', {'plants': plants})


class ChartData(APIView):
	"""
	View to list all users in the system.

	* Requires token authentication.
	* Only admin users are able to access this view.
	"""
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		defaultData = []
		for x in list(Plant.objects.values_list("log_box_plot")):
			if x[0] != 0:
				defaultData.append(x[0])
		defaultData2 = []
		for x in list(Plant.objects.values_list("log_box_plot2")):
			if x[0] != 0:
				defaultData2.append(x[0])
		data = {
			"defaultData": defaultData,
			"defaultData2": defaultData2

		}
	   
		return Response(data)


def error_404(request):
        data = {}
        return render(request,'plant/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'plant/error_500.html', data)