# Create your views here.
# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render
from django.template import RequestContext
from django.utils import simplejson
from django.utils.encoding import codecs
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.core.cache import cache
from django.db.models import Q
from pprint import pprint
from principal.models import *
import datetime
import time
import math


def home(request):
	return render_to_response('home.html',locals(), context_instance=RequestContext(request))
	

def tips(request):
	return render_to_response('tips.html',locals(), context_instance=RequestContext(request))