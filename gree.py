import sys
import os

DATE = sys.argv[2]
report_date = sys.argv[1]

f_install = open("install/"+report_date,"r")
f_click = open("click/"+report_date,"r")


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
	2545:"Modern War !",
	2642:"JackpotSlots",
	4435:"Call to Arms",
	4635:"Dragon Realms",
	4636:"Dragon Realms",
	4802:"Dragon Realms Android",
	5188:"Beyond the Dead"
}


sum_impression = 0
sum_click = 0
sum_install = 0
sum_spend = 0
sum_spend_dollar = 0

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

def handle_install(points,date,device_type,SETTING,platform):
	if (points>10 or points<-10) and date==DATE:
		SETTING_NAME=Setting_dict[sid]+"_"+platform
		if device_type in ["PHONE","PAD"]:
			device_type_translate = "Android"+device_type
		else:
			device_type_translate = device_type
		
		if SETTING_NAME in data_dict:
			if points>10:
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


def handle_impression_and_click(date,event_type,sid,device_type,platform,sum_num):
	SETTING_NAME=Setting_dict[sid]+"_"+platform
	
	if date == DATE:

		if platform == "android":
			if device_type in ["PHONE","other"]:
				device_type_translate = "AndroidPHONE"
			else:
				device_type_translate = "AndroidPAD"
		elif platform == "iOS":
			if device_type in ["iPHONE","other"]:
				device_type_translate = "iPHONE"
			else:
				device_type_translate = "iPAD"

		

		

		if SETTING_NAME in data_dict:
			if event_type == '-3':
				data_dict[SETTING_NAME][device_type_translate]["impression"] = data_dict[SETTING_NAME][device_type_translate]["impression"] + int(sum_num)
			elif event_type == '-2':
				data_dict[SETTING_NAME][device_type_translate]["click"] = data_dict[SETTING_NAME][device_type_translate]["click"] + int(sum_num)
		else:
			if device_type_translate in ["AndroidPHONE","AndroidPAD"]:
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
	points = int(items[5])
	platform = items[4]
	date = items[0]
	device_type = items[3]

	handle_install(points,date,device_type,sid,platform)


# handle impression and click file
for line_ic in f_click:
	items = line_ic[:-1].split("\t")

	date = items[0]
	sid = int(items[3])
	event_type = items[1]
	device_type = items[4]
	sum_num = items[6]
	platform = items[5]

	handle_impression_and_click(date,event_type,sid,device_type,platform,sum_num)



if os.path.exists('report/Daily/Gree-'+DATE+'.csv'):
	os.remove('report/Daily/Gree-'+DATE+'.csv')
	is_same_file = 1
g=open('report/Daily/Gree-'+DATE+'.csv','a')
print >>g, "date,sid,device_type,impression,click,install,points,spend($)"
for setting in data_dict:
	for device_type in data_dict[setting]:
		print >>g, DATE+','+str(setting)+','+device_type+','+str(data_dict[setting][device_type]['impression'])+','+str(data_dict[setting][device_type]['click'])+','+str(data_dict[setting][device_type]['install'])+','+str(data_dict[setting][device_type]['spend'])+','+str(int(data_dict[setting][device_type]['spend'])/float(100))
		sum_impression = sum_impression + data_dict[setting][device_type]['impression']
		sum_click = sum_click + data_dict[setting][device_type]['click']
		sum_install = sum_install + data_dict[setting][device_type]['install']
		sum_spend = sum_spend + data_dict[setting][device_type]['spend']
		sum_spend_dollar = float(sum_spend)/100

print >>g,"Total,,,"+str(sum_impression)+","+str(sum_click)+","+str(sum_install)+","+str(sum_spend)+","+str(sum_spend_dollar)



if is_same_file==0:
	g=open('report/Monthly/Gree-'+Month+'.csv','a')
	for setting in data_dict:
		for device_type in data_dict[setting]:
			print >>g, DATE+','+str(setting)+','+device_type+','+str(data_dict[setting][device_type]['impression'])+','+str(data_dict[setting][device_type]['click'])+','+str(data_dict[setting][device_type]['install'])+','+str(data_dict[setting][device_type]['spend'])+','+str(int(data_dict[setting][device_type]['spend'])/float(100))



f_install.close()
f_click.close()
g.close()
