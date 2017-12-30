
from bs4 import BeautifulSoup
import requests
import sys
import MySQLdb
import re
import os
import urllib

# Open database connection
db = MySQLdb.connect("localhost","root","root","phone_info_demo")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data


content = BeautifulSoup(open("phonecurry-sitemap.xml"),"html.parser")
allLoc = content.find_all("loc")
file_directory = 'images'
for loc in allLoc:

    phone_name = None
    phone_directory = None
    ph_directory = None
    atag = None
    aName = None

    eachLink = loc.string
    eachLink = eachLink.rstrip().replace('\n','')

    eachPage = requests.get(eachLink,verify=False,timeout=10)
    eachPageBS = BeautifulSoup(eachPage.content,"html.parser")

    atag = eachPageBS.find("h3", attrs={'class': 'prod-name'})
    aName = eachPageBS.find("div", attrs={'id': 'productImg'})
    aPrice = eachPageBS.find("span", attrs={'class': 'phone-price-details'})
    aLaunch = eachPageBS.find("span", attrs={'class': 'phone-launch-details'})
    if aName:
        #mobile_name = aName.get('data-phone-name')
        mobile_name = str(eachLink.replace('http://www.phonecurry.com/reviews?phone=',''))
        mobile_name = mobile_name.replace("-"," ")
        # Images Folder
        phone_name = str(eachLink.replace('http://www.phonecurry.com/reviews?phone=',''))
        phone_directory = "images" + "/" + str(phone_name)

        if not os.path.exists(phone_directory):
            os.makedirs(phone_directory)

        phone_images = aName.find_all("img")

        if phone_images:
            for images in phone_images:
                image_src = images.get("src")
                if image_src:
                    image_name = image_src.replace("http://www.phonecurry.com/img/phones/","")
                    urllib.urlretrieve(image_src,phone_directory + "/" + image_name)


        phone_os = 'NA'
        touchscreen = 'NA'
        screen_size = 'NA'
        screen_resolution = 'NA'
        display_features = 'NA'
        sensors = 'NA'
        fingerprint_sensor = 'NA'
        processor = 'NA'
        gpu = 'NA'
        ram = 'NA'
        internal_memory = 'NA'
        battery_capacity = 'NA'
        weight = 'NA'
        thickness = 'NA'
        camera = 'NA'
        camera_auto_focus = 'NA'
        camera_flash = 'NA'
        hd_video_recording = 'NA'
        other_camera_features = 'NA'
        secondary_camera = 'NA'
        secondary_camera_features = 'NA'
        bluetooth= 'NA'
        usb = 'NA'
        wifi = 'NA'
        feature_4g = 'NA'
        feature_3g = 'NA'
        volte = 'NA'
        feature_2g = 'NA'
        gps = 'NA'
        compass = 'NA'
        nfc = 'NA'
        dual_sim = 'NA'
        dlna = 'NA'
        more = 'NA'
        app_store = 'NA'
        launch = 'NA'
        expandable_memory_slot = 'NA'

        if aPrice:
            price = aPrice.string
            price = price.replace(",","")
            price = price.replace("onwards","")
            price = price.replace("Rs.","")
        else:
            price = "NA"

        if aLaunch:
            launch = aLaunch.string
        else:
            launch = "NA"

        feature_tables = eachPageBS.find_all("table", attrs={'class': 'features-table'})

        for feature_table in feature_tables:
            feature_rows = feature_table.find_all('tr')

            for row in feature_rows:
                col_details = row.find_all('td')
                col_name = col_details[0].string
                col_value = col_details[1].string

                if col_name == "Smartphone OS":
                    phone_os = col_value
                if col_name == "App Store":
                    app_store = col_value

                if col_name == "Expandable Memory Slot":
                    expandable_memory_slot = col_value

                if col_name == "Touchscreen":
                    touchscreen = col_value

                if col_name == "Screen Size":
                    screen_size = col_value

                if col_name == "Screen Resolution":
                    screen_resolution = col_value

                if col_name == "Display Features":
                    if col_value:
                        display_features = col_value
                    else:
                        li_elements = col_details[1].find_all('li')
                        if li_elements:
                            display_features = None
                            for element in li_elements:
                                if element.string:
                                    if display_features:
                                        display_features = display_features + "," + element.string
                                    else:
                                        display_features = element.string


                if col_name == "Sensors":
                    if col_value:
                        sensors = col_value
                    else:
                        li_elements = col_details[1].find_all('li')
                        if li_elements:
                            sensors = None
                            for element in li_elements:
                                if element.string:
                                    if sensors:
                                        sensors = sensors + "," + element.string
                                    else:
                                        sensors = element.string

                if col_name == "Fingerprint sensor":
                    fingerprint_sensor = col_value


                if col_name == "Processor":
                    processor = col_value

                if col_name == "GPU":
                    gpu = col_value

                if col_name == "RAM":
                    ram = col_value

                if col_name == "Internal Memory":
                    internal_memory = col_value

                if col_name == "Battery Capacity":
                    battery_capacity = col_value

                if col_name == "Weight":
                    weight = col_value

                if col_name == "Thickness":
                    thickness = col_value

                if col_name == "Camera":
                    camera = col_value

                if col_name == "Camera Auto-Focus":
                    camera_auto_focus = col_value

                if col_name == "Camera Flash":
                    camera_flash = col_value

                if col_name == "HD Video Recording":
                    hd_video_recording = col_value

                if col_name == "Other Camera Features":
                    other_camera_features = col_value
                    if col_value:
                        other_camera_features = col_value
                    else:
                        li_elements = col_details[1].find_all('li')
                        if li_elements:
                            other_camera_features = None
                            for element in li_elements:
                                if element.string:
                                    if other_camera_features:
                                        other_camera_features = other_camera_features + "," + element.string
                                    else:
                                        other_camera_features = element.string

                if col_name == "Secondary Camera":
                    secondary_camera = col_value

                if col_name == "Secondary Camera Features":
                    secondary_camera_features = col_value
                    if col_value:
                        secondary_camera_features = col_value
                    else:
                        li_elements = col_details[1].find_all('li')
                        if li_elements:
                            other_camera_features = None
                            for element in li_elements:
                                if element.string:
                                    if secondary_camera_features:
                                        secondary_camera_features = secondary_camera_features + "," + element.string
                                    else:
                                        secondary_camera_features = element.string

                if col_name == "Bluetooth":
                    bluetooth = col_value

                if col_name == "USB":
                    usb = col_value

                if col_name == "WiFi":
                    wifi = col_value
                if col_name == "4G":
                    feature_4g = col_value

                if col_name == "VoLTE":
                    volte = col_value

                if col_name == "3G":
                    feature_3g = col_value

                if col_name == "2G Internet (GPRS/EDGE)":
                    feature_2g = col_value

                if col_name == "GPS":
                    gps = col_value

                if col_name == "Compass":
                    compass = col_value

                if col_name == "NFC":
                    nfc = col_value

                if col_name == "Dual SIM":
                    dual_sim = col_value

                if col_name == "DLNA ":
                    dlna = col_value

                if col_name == "More":
                    if col_value:
                        more = col_value
                    else:
                        li_elements = col_details[1].find_all('li')
                        if li_elements:
                            more = None
                            for element in li_elements:
                                if element.string:
                                    if more:
                                        more = more + "," + element.string
                                    else:
                                        more = element.string


        read_sql = "SELECT * FROM phone_mobileinfos \
            WHERE mobile_name = '%s'" % mobile_name
        print(mobile_name);
        # Prepare SQL query to INSERT a record into the database.
        write_sql = "INSERT INTO phone_mobileinfos(mobile_name, \
                   phone_os, \
                   touchscreen, \
                   processor, \
                   sensors, \
                   screen_size, \
                   screen_resolution,\
                   display_features, \
                   fingerprint_sensor, \
                   gpu, \
                   ram, \
                   internal_memory,\
                   battery_capacity,\
                   weight,\
                   thickness, \
                   camera, \
                   camera_auto_focus,  \
                   camera_flash,  \
                   hd_video_recording,\
                   other_camera_features,\
                   secondary_camera, \
                   secondary_camera_features ,\
                   bluetooth ,\
                   usb ,\
                   feature_4g ,\
                   volte ,\
                   feature_3g ,\
                   feature_2g ,\
                   wifi ,\
                   compass ,\
                   gps ,\
                   dual_sim ,\
                   nfc ,\
                   dlna ,\
                   more ,\
                   price  ,\
                   app_store ,\
                   launch ,\
                   expandable_memory_slot ,\
                   mobile_url) \
                   VALUES ('%s', '%s', '%s','%s','%s', '%s','%s', '%s' ,'%s', '%s', \
                   '%s' ,'%s', '%s', '%s' ,'%s', '%s', '%s' ,'%s', '%s', '%s' , \
                   '%s', '%s', '%s', '%s', '%s' ,'%s', '%s', '%s', '%s', '%s' , \
                   '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s', '%s'  )" % \
                   (mobile_name, phone_os, touchscreen, processor, screen_size, screen_resolution, display_features, sensors,fingerprint_sensor, gpu,
                    ram, internal_memory, battery_capacity, weight, thickness, camera, camera_auto_focus, camera_flash, hd_video_recording, other_camera_features,
                    secondary_camera,secondary_camera_features, bluetooth,usb,feature_4g,volte,feature_3g,feature_2g,wifi,compass,
                    gps,dual_sim, nfc, dlna, more, price, app_store, launch, expandable_memory_slot, eachLink)

        update_sql = "UPDATE phone_mobileinfos SET \
                    phone_os = '%s', \
                    touchscreen ='%s', \
                    processor = '%s', \
                    sensors = '%s', \
                    screen_size = '%s', \
                    screen_resolution = '%s', \
                    fingerprint_sensor = '%s', \
                    gpu = '%s', \
                    ram = '%s', \
                    internal_memory = '%s', \
                    battery_capacity = '%s', \
                    weight = '%s', \
                    thickness = '%s', \
                    camera = '%s', \
                    camera_auto_focus = '%s', \
                    camera_flash = '%s', \
                    hd_video_recording = '%s', \
                    other_camera_features = '%s', \
                    secondary_camera = '%s', \
                    display_features = '%s', \
                    secondary_camera_features = '%s',\
                    bluetooth  = '%s',\
                    usb  = '%s',\
                    feature_4g  = '%s',\
                    volte  = '%s',\
                    feature_3g  = '%s',\
                    feature_2g  = '%s',\
                    wifi  = '%s',\
                    compass  = '%s',\
                    gps  = '%s',\
                    dual_sim  = '%s', \
                    dlna  = '%s', \
                    more  = '%s', \
                    price  = '%s', \
                    app_store  = '%s', \
                    launch  = '%s', \
                    expandable_memory_slot = '%s' ,\
                    nfc  = '%s'\
                    where mobile_name = '%s'" % (phone_os, touchscreen, processor, sensors, screen_size, screen_resolution,
                    fingerprint_sensor, gpu, ram, internal_memory, battery_capacity,
                    weight, thickness, camera, camera_auto_focus, camera_flash, hd_video_recording,
                    other_camera_features, secondary_camera, display_features,secondary_camera_features,bluetooth,usb,
                    feature_4g,volte,feature_3g,feature_2g,wifi,compass, gps,dual_sim, dlna, more, price,app_store, launch, expandable_memory_slot, nfc, mobile_name)


        try:
            # Execute the SQL command
            cursor.execute(read_sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            print eachLink
            if not results:
                print "Added %s" % mobile_name
                cursor.execute(write_sql)
            else:
                print "Found %s" % mobile_name
                cursor.execute(update_sql)

            # Commit your changes in the database
            db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()

# disconnect from server
db.close()
