import data_manager
import flight_search
import flight_data
import notification_manager
import user


user = user.User()
user.new_user()
flights = flight_data.FlightData()
get_city_code = flight_search.FlightSearch()
sheet = data_manager.DataManager()
future_price = flight_data.FlightData()
#new_list = []
founds =[]
for city in sheet.sheet_data:
    # To add new city code
    #city['iataCode'] = get_city_code.get_destination_code(city["city"])
    flights.search(city['iataCode'])
    #new_list.append(city)
#sheet.update_city_code(new_list)
for city in sheet.sheet_data:
    try:
        if city['lowestPrice'] >= flights.database[city['iataCode']]["price"]:
            founds.append(flights.database[city['iataCode']])
    except KeyError:
        pass
send_box = notification_manager.NotificationManager(founds)
send_box.send_email(users=user.get_users(),founds=founds)
