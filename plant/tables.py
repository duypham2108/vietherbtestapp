#!/usr/bin/env python
# coding: utf-8
from datetime import date
import django

if django.VERSION >= (1, 10):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy

from table.columns import Column
from table.columns.imagecolumn import ImageColumn, ImageColumn2
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table import Table
from table.utils import A

from .models import Plant, Metabolite

class LinkColumnTable(Table):
    plant_id = Column(field='plant_id', header='ID')
    plant_engname = LinkColumn(field='plant_engname',header='English Name', links=[
        Link(viewname='detailherb', args=(A('plant_id'),), text=A('plant_engname'))])
    plant_vnname = LinkColumn(field='plant_vnname',header='Vietnamese Name', links=[
        Link(viewname='detailherb', args=(A('plant_id'),), text=A('plant_vnname'))])
    familia = LinkColumn(field='familia.family',header='Familia', links=[
        Link(viewname='detailfamilia', args=(A('familia_id'),), text=A('familia'))])
    genus = LinkColumn(field='genus.genus',header='Genus', links=[
        Link(viewname='detailgenus', args=(A('genus_id'),), text=A('genus'))])
    logo = ImageColumn(field='plant_image', header='Plant Image', image_title='Plant')

    class Meta:
        model = Plant
        ajax = True

class MetaboliteTable(Table):
    metabolite_id = Column(field='metabolite_id', header='ID')
    metabolite_name = LinkColumn(field='metabolite_name',header='English Name', links=[
        Link(viewname='detailmetabolite', args=(A('metabolite_id'),), text=A('metabolite_name'))])
    formula = LinkColumn(field='formula',header='Formula', links=[
        Link(viewname='detailmetabolite', args=(A('metabolite_id'),), text=A('formula'))])
    image = ImageColumn2(field='image', header='Structure', image_title='Structure')

    class Meta:
        model = Metabolite
        ajax = True