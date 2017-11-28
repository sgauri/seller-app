from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Palazzo
from .forms import PalazzoForm
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
import csv
from django.contrib import messages
import logging


def all_products(request):
	product_list = Palazzo.objects.all().order_by("sku")
	page = request.GET.get('q', 1)
	paginator = Paginator(product_list, 4)
	try:
		prods = paginator.page(page)
	except PageNotAnInteger:
		prods = paginator.page(1)
	except EmptyPage:
		prods = paginator.page(paginator.num_pages)
	return render(request, 'flipkart/product_list.html', {'prods':prods})


def uploadcsv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "flipkart/upload_csv1.html", data)
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file1"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("flipkart:upload_csv"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("flipkart:upload_csv"))

	# with open(csv_file, "rb") as file_data:
		file_data = csv.reader(csv_file)
		next(file_data, None)
	# file_data = open(csv_file1, "r")
	# lines = file_data.split("\n")
	# #loop over the lines and save them in db. If error , store as string and then display
		for fields in file_data:
			# fields = line.split(",")
			data_dict = {}
			data_dict["sku"] = fields[0]
			data_dict["item_name"] = fields[1]
			data_dict["color"] = fields[2]
			data_dict["material"] = fields[3]
			data_dict["sp"] = fields[4]
			data_dict["mrp"] = fields[5]
			data_dict["qty"] = fields[6]
			data_dict["description"] = fields[7]
			data_dict["upc"] = fields[8]
			data_dict["weight"] = fields[9]
			data_dict["weight_unit"] = fields[10]
			data_dict["size"] = fields[11]
			data_dict["key_feature1"] = fields[12]
			data_dict["key_feature2"] = fields[13]
			data_dict["img"] = fields[14]
			try:
				form = PalazzoForm(data_dict)
				if form.is_valid():
					form.save()
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())                                                
			except Exception as e:
				logging.getLogger("error_logger").error(form.errors.as_json())                    
				pass
 
	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
 
	return HttpResponseRedirect(reverse("flipkart:upload_csv"))



### my attempt to check why post method is converting to get automatically ###

	# print request.method
	# csv_file = request.FILES['csv_file1']
	# form = PalazzoForm(request.POST, request.FILES)


	# logging.info("uploaderror")
	# logger = logging.getLogger("uploaderror.%s" % __name__)
	# if request.method=="POST":
	# 	file_data = csv_file.read()
	# 	lines = file_data.split("\n")
	# 	for line in lines:
	# 		fields = line.split(",")
	# 		data_dict = {}
	# 		data_dict["sku"] = fields[0]
	# 		data_dict["item_name"] = fields[1]
	# 		data_dict["color"] = fields[2]
	# 		data_dict["material"] = fields[3]
	# 		data_dict["sp"] = fields[4]
	# 		data_dict["mrp"] = fields[5]
	# 		data_dict["qty"] = fields[6]
	# 		data_dict["description"] = fields[7]
	# 		data_dict["upc"] = fields[8]
	# 		data_dict["weight"] = fields[9]
	# 		data_dict["weight_unit"] = fields[10]
	# 		data_dict["size"] = fields[11]
	# 		data_dict["key_feature1"] = fields[12]
	# 		data_dict["key_feature2"] = fields[13]
	# 		data_dict["img"] = fields[14]
	# 		form = PalazzoForm(data_dict)
	# 		if form.is_valid():
	# 			form.save()
	# 		else:
	# 			logger.info(form.errors.as_json())
	# else:
	# 	HttpResponseRedirect(reverse("flipkart:upload_csv"))
	# return HttpResponseRedirect(reverse("flipkart:upload_csv"))


### my attempt to check why post method is converting to get automatically ###



### Worked on Logger class to get Logs here but its not working even after modifying ###


	# logging.error("error_logger")
	# logger = logging.getLogger("error_logger")
	
	# if "GET" == request.method:
	# 	return render(request, "flipkart/default.html")
	# # if not GET, then proceed

	# try:
	# 	csv_file = request.FILES["csv_file1"]
	# 	if not csv_file.name.endswith('.csv'):
	# 		messages.error(request,'File is not CSV type')
	# 		return HttpResponseRedirect(reverse("flipkart:upload_csv"))
	# 	#if file is too large, return
	# 	if csv_file.multiple_chunks():
	# 		messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
	# 		return HttpResponseRedirect(reverse("flipkart:upload_csv"))

	# 	file_data = csv_file.read().decode("utf-8")

	# 	lines = file_data.split("\n")
	# 	#loop over the lines and save them in db. If error , store as string and then display
	# 	for line in lines:
	# 		fields = line.split(",")
	# 		data_dict = {}
	# 		data_dict["sku"] = fields[0]
	# 		data_dict["item_name"] = fields[1]
	# 		data_dict["color"] = fields[2]
	# 		data_dict["material"] = fields[3]
	# 		data_dict["sp"] = fields[4]
	# 		data_dict["mrp"] = fields[5]
	# 		data_dict["qty"] = fields[6]
	# 		data_dict["description"] = fields[7]
	# 		data_dict["upc"] = fields[8]
	# 		data_dict["weight"] = fields[9]
	# 		data_dict["weight_unit"] = fields[10]
	# 		data_dict["size"] = fields[11]
	# 		data_dict["key_feature1"] = fields[12]
	# 		data_dict["key_feature2"] = fields[13]
	# 		data_dict["img"] = fields[14]
	# 		try:
	# 			form = PalazzoForm(data_dict)
	# 			if form.is_valid():
	# 				form.save()
	# 			else:
	# 				logger.error(form.errors.as_json())
	# 		except Exception as e:
	# 			logger.error(form.errors.as_json())
	# 			pass
	# except Exception as e:
	# 	logger.error("Unable to upload file. "+repr(e))
	# 	messages.error(request,"Unable to upload file. "+repr(e))
	# return HttpResponseRedirect(reverse("flipkart:upload_csv"))


### Worked on Logger class to get Logs here but its not working even after modifying ###



### my method to attempt to change the code on my own but it was unsuccessful ###

	# file = request.FILES['csv_file']
	# # if not csv_file.name.endswith('.csv'):
	# # 	messages.error(request, 'File is not csv type')
	# # 	return HttpResponseRedirect("flipkart:upload_csv")
	# f = open(file, 'r')
	# data = list(csv.reader(f))
	# for row in data:
	# 	if row[0] != 'sku':
	# 		Palazzo.objects.get_or_create(sku = row[0], item_name=row[1], color=row[2], material=row[3], sp=row[4], mrp=row[5], qty=row[6], description=row[7], upc=row[8], weight=row[9], weight_unit=row[10], size=row[11], key_feature1=row[12], key_feature2=row[13], img=row[14])
	# 	return HttpResponseRedirect('/')
	# return HttpResponseRedirect('/admin')
	# with open(csv_file) as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if row[0] != 'sku':
	# 			_, created = Palazzo.objects.get_or_create(sku = row[0], item_name=row[1], color=row[2], material=row[3], sp=row[4], mrp=row[5], qty=row[6], description=row[7], upc=row[8], weight=row[9], weight_unit=row[10], size=row[11], key_feature1=row[12], key_feature2=row[13], img=row[14])
	# return HttpResponseRedirect('/admin')

### my method to attempt to change the code on my own but it was unsuccessful ###