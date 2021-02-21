from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import DestinationForm
from geopy.geocoders import MapBox
from geopy import distance
import json,requests
from .models import SensorModel,VehicleModel
from django.contrib.gis.geos import Point,GEOSGeometry
from blog.models import Post
# from django.db.models.functions import Round

def homepage(request):
	response=requests.get('http://api.openweathermap.org/data/2.5/weather?q=kathmandu,np&appid=8d2de98e089f1c28e1a22fc19a24ef04')	
	weather_data=response.json()

	print(weather_data["weather"])
	# weather_dict={weather_data["weather"][i] for i in [0,]}
	source_latitude=0
	source_longitude=0
	destination_latitude=0
	destination_longitude=0
	travel_distance=0
	if request.method == 'POST':
		form = DestinationForm(request.POST)
		if form.is_valid():
			form_data=form.save()
			address = "%s, %s" %(form_data.source,form_data.destination)
			geolocator=MapBox(api_key='pk.eyJ1IjoicmFuamFuNDM1IiwiYSI6ImNrNWIzdnNqeTE2ZjgzZG82OG40aG82ejcifQ.nrFTVyOERu6YhgS66Gxr8A')
			location_source =geolocator.geocode(form_data.source)
			location_destination = geolocator.geocode(form_data.destination)
			source_latitude= location_source.latitude
			source_longitude= location_source.longitude
			destination_latitude= location_destination.latitude
			destination_longitude= location_destination.longitude
			source=(source_latitude,source_longitude)
			destination=(destination_latitude,destination_longitude)
			str_geo=str(distance.distance(source,destination))
			travel_distance=round(float(str_geo[:-3]),2)	
			print(travel_distance)
			pnt1=GEOSGeometry('SRID=4326;POINT(%s %s)' %(source_latitude,source_longitude))
			pnt2=GEOSGeometry('SRID=4326;POINT(%s %s)' %(destination_latitude,destination_longitude))
			print(pnt1.distance(pnt2)*100)
			# location.destination = geolocator.geocode(form_data.destination)

	form=DestinationForm()

	#showing database information in map
	post_list=Post.objects.all()
	print (post_list[0].location.wkt)
	loc_list=[str(post.location) for post in post_list]
	temp=[loc.split(";") for loc in loc_list]
	point_list=[i[1] for i in temp]
	final=[(point[7:(len(point)-1)]) for point in point_list]

	tempo=[a.split(" ") for a in final]
	lat=[i[0] for i in tempo]
	lon=[i[1] for i in tempo]
	latlon=[(float(lat[i]),float(lon[i])) for i in range(len(lon))]

	#showing sensor data 
	sensor_data=SensorModel.objects.latest('id')

	#showing the number of vehicles
	vehicle_num=VehicleModel.objects.latest('id')


	return render(request, 'map/base_map.html', {
		'form': form,
		'source_latitude': source_latitude,
		'source_longitude': source_longitude,
		'destination_latitude': destination_latitude,
		'destination_longitude': destination_longitude,
		'distance': travel_distance,
		'posts':post_list,
		'location':latlon,
		'weather_data':weather_data,
		'sensor_data':sensor_data,
		'vehicle_num':vehicle_num,
		},)









# def databaseshow(request):
# 	#showing post objects
# 	post_list=Post.objects.all()
# 	print (post_list[0].location.wkt)
# 	loc_list=[str(post.location) for post in post_list]
# 	temp=[loc.split(";") for loc in loc_list]
# 	point_list=[i[1] for i in temp]
# 	final=[(point[7:(len(point)-1)]) for point in point_list]

# 	tempo=[a.split(" ") for a in final]
# 	lat=[i[0] for i in tempo]
# 	lon=[i[1] for i in tempo]
# 	latlon=[(float(lat[i]),float(lon[i])) for i in range(len(lon))]
# 	return render(request,'map/base_map.html',{'posts':post_list,'location':latlon})