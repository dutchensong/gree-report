import sys
import os

DATE = sys.argv[1]

f_install = open("install/"+DATE,"r")
f_click = open("click/"+DATE,"r")

DDates = DATE.split("-")
Month = DDates[0]+'-'+DDates[1]

is_same_file = 0

setting_list = []

data_dict={}

Setting_dict={
	1544:"Book Of Ashes",
	1545:"Kindom Age",
	1546:"Knights",  
	1547:"NFL Shuffle",
	1548:"JackpotSlots",
	1549:"MLB",
	2195:"Crime City!",
	2506:"Knights",
	2508:"Saga",
	2543:"Modern War",
	2544:"test111",
	2545:"Modern War !"
}

# dict = 
# {
# 	2195:
# 	{
# 		"PHONE":
# 		{
# 			"install":0,
# 			"impression":0,
# 			"click":0,
# 			"spend":0
# 		},
# 			"PAD":
# 		{
# 			"install":0,
# 			"impression":0,
# 			"click":0,
# 			"spend":0
# 		}
# 	}
# }

# 2013-04-27	1729	2195	PHONE	90

def handle_install(points,date,device_type,SETTING):
	if points>0 and date==DATE:
		SETTING_NAME=Setting_dict[SETTING]
		if device_type in ["PHONE","PAD"]:
			device_type_translate = "Android"+device_type
		else:
			device_type_translate = device_type
		
		if SETTING_NAME in data_dict:

			data_dict[SETTING_NAME][device_type_translate]["install"] = data_dict[SETTING_NAME][device_type_translate]["install"]+ 1
			data_dict[SETTING_NAME][device_type_translate]["spend"] = data_dict[SETTING_NAME][device_type_translate]["spend"]+ points
		else:
			if device_type in ["PHONE","PAD"]:
				data_dict[SETTING_NAME]={
					"AndroidPHONE":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					},
					"AndroidPAD":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					}
				}
			else:
				data_dict[SETTING_NAME]={
					"iPHONE":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					},
					"iPAD":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					}
				}
			data_dict[SETTING_NAME][device_type_translate]["install"] = data_dict[SETTING_NAME][device_type_translate]["install"]+ 1
			data_dict[SETTING_NAME][device_type_translate]["spend"] = data_dict[SETTING_NAME][device_type_translate]["spend"]+ points


def handle_impression_and_click(date,event_type,sid,device_type):
	if date == DATE:
		SETTING_NAME=Setting_dict[sid]
		if device_type in ["PHONE","PAD"]:
			device_type_translate = "Android"+device_type
		else:
			device_type_translate = device_type
		if SETTING_NAME in data_dict:
			if event_type == '-3':
				data_dict[SETTING_NAME][device_type_translate]["impression"] = data_dict[SETTING_NAME][device_type_translate]["impression"] + 1
			elif event_type == '-2':
				data_dict[SETTING_NAME][device_type_translate]["click"] = data_dict[SETTING_NAME][device_type_translate]["click"] + 1
		else:
			if device_type in ["PHONE","PAD"]:
				data_dict[SETTING_NAME]={
					"AndroidPHONE":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					},
					"AndroidPAD":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					}
				}
			else:
				data_dict[SETTING_NAME]={
					"iPHONE":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					},
					"iPAD":
					{
						"install":0,
						"impression":0,
						"click":0,
						"spend":0
					}
				}
			

				
# handle install file
for line in f_install:
	items = line[:-1].split("\t")

	sid = int(items[2])
	points = int(items[4])
	date = items[0]
	device_type = items[3]

	handle_install(points,date,device_type,sid)


# handle impression and click file
for line_ic in f_click:
	items = line_ic[:-1].split("\t")

	date = items[0]
	sid = int(items[3])
	event_type = items[1]
	device_type = items[4]

	handle_impression_and_click(date,event_type,sid,device_type)



if os.path.exists('report/Gree-'+DATE+'.csv'):
	os.remove('report/Gree-'+DATE+'.csv')
	is_same_file = 1
g=open('report/Daily/Gree-'+DATE+'.csv','a')
print >>g, "date,sid,device_type,impression,click,install,points,spend($)"
for setting in data_dict:
	for device_type in data_dict[setting]:
		print >>g, DATE+','+str(setting)+','+device_type+','+str(data_dict[setting][device_type]['impression'])+','+str(data_dict[setting][device_type]['click'])+','+str(data_dict[setting][device_type]['install'])+','+str(data_dict[setting][device_type]['spend'])+','+str(int(data_dict[setting][device_type]['spend'])/float(100))



if is_same_file==0:
	g=open('report/Monthly/Gree-'+Month+'.csv','a')
	for setting in data_dict:
		for device_type in data_dict[setting]:
			print >>g, DATE+','+str(setting)+','+device_type+','+str(data_dict[setting][device_type]['impression'])+','+str(data_dict[setting][device_type]['click'])+','+str(data_dict[setting][device_type]['install'])+','+str(data_dict[setting][device_type]['spend'])+','+str(int(data_dict[setting][device_type]['spend'])/float(100))



f_install.close()
f_click.close()
