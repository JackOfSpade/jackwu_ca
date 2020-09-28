from ctypes import windll
import weather.hourly_weather_class as hourly_weather_class
import weather.retrieve_info_class as retrieve_info_class
import os
import numpy as np


# Make sure zip_postal returns an actual location beforehand.
def get_appropriate_hourly_weather_instance_list(type_of_person, unit, exercise, zip_postal):
    accuweather_api_key = retrieve_info_class.retrieve_info.get_accuweather_api_key(0)
    location = retrieve_info_class.retrieve_info.get_location(accuweather_api_key, zip_postal)

    location_name = location[0]
    location_key = location[1]
    # location_key = "48968_PC"

    # Get hourly weather data for TODAY.
    hourly_weather_instance_list = retrieve_info_class.retrieve_info.get_hourly_weather(location_key,
                                                                                        accuweather_api_key,
                                                                                        unit)
    # For testing purposes
    # PyCharm Interface console fake-clear ------------
    print('\n' * 80)  # prints 80 line breaks
    os.system('cls' if os.name == 'nt' else 'clear')
    # --------------------------------------------------

    for instance in hourly_weather_instance_list:
        if hourly_weather_class.hourly_weather.sunrise_time is not None:
            print("Sunrise: " + hourly_weather_class.hourly_weather.sunrise_time)

        if hourly_weather_class.hourly_weather.sunset_time is not None:
            print("Sunset: " + hourly_weather_class.hourly_weather.sunset_time)

        print("Time: " + hourly_weather_class.hourly_weather.time_tuple_to_string(*instance.time_tuple))
        print("Real-Feel Temperature: " + str(instance.real_feel_temperature_tuple[0]) + str(
            instance.real_feel_temperature_tuple[1]))
        print("Has Precipitation? " + str(instance.has_precipitation))
        print("UV Index: " + str(instance.uv_index))
        print("\n")

    retrieve_info_class.retrieve_info.remove_incompatible_hourly_weather(hourly_weather_instance_list,
                                                                                 exercise, type_of_person)
    retrieve_info_class.retrieve_info.group_compatible_hourly_weather(hourly_weather_instance_list)

    return (hourly_weather_instance_list, location_name)

def extract_data(hourly_weather_instance_list):
    # 2D array, each element is [time_interval, feels-like_temperature_tuple_list, uv_index_list]
    data_list = []
    unit = None

    for element in hourly_weather_instance_list:
        temp_list = []

        if len(element) == 1:
            if element[0].twenty_four_hour_time.hour == 23:
                next_hour = element[0].twenty_four_hour_time.replace(hour=0)
            else:
                next_hour = element[0].twenty_four_hour_time.replace(hour=element[0].twenty_four_hour_time.hour + 1)

            temp_list.append(hourly_weather_class.hourly_weather.time_tuple_to_string(*element[0].time_tuple) + " - " + hourly_weather_class.hourly_weather.time_tuple_to_string(*hourly_weather_class.hourly_weather.convert_from_24_to_12_hour_time(next_hour)))
            temp_list.append(element[0].real_feel_temperature_tuple)
            temp_list.append(element[0].uv_index)

            data_list.append(temp_list)
        elif len(element) > 1:
            temp_list.append(hourly_weather_class.hourly_weather.time_tuple_to_string(*element[0].time_tuple) + " - " + hourly_weather_class.hourly_weather.time_tuple_to_string(*element[len(element) - 1].time_tuple))
            temp_list2 = []
            temp_list3 = []

            for item in element:
                temp_list2.append(item.real_feel_temperature_tuple)
                temp_list3.append(item.uv_index)

            temp_list.append(temp_list2)
            temp_list.append(temp_list3)

            data_list.append(temp_list)

    # Get min/max
    for element in data_list:
        temp_list = []

        if type(element[1]) is list:
            for item in element[1]:
                temp_list.append(item[0])

            unit = element[1][0][1]
        elif type(element[1]) is tuple:
            temp_list.append(element[1][0])
            unit = element[1][1]

        minimum = min(temp_list)
        maximum = max(temp_list)


        if minimum == maximum:
            element[1] = str(minimum) + unit
        else:
            element[1] = str(minimum) + unit + " - " + str(maximum) + unit

        temp_list.clear()

        if type(element[2]) is list:
            temp_list += element[2]
        elif type(element[2]) is int:
            temp_list.append(element[2])


        minimum = min(temp_list)
        maximum = max(temp_list)

        if minimum == maximum:
            element[2] = str(minimum)
        else:
            element[2] = str(minimum) + " - " + str(maximum)
    return data_list

def get_results_matrix(type_of_person, unit, exercise, zip_postal):
    if unit == "imperial":
        metric = "false"
    else:
        metric = "true"

    tuples_of_hourly_weather_instances_list, location_name = get_appropriate_hourly_weather_instance_list(type_of_person, metric, exercise, zip_postal)

    if len(tuples_of_hourly_weather_instances_list) > 0:
        data_list = extract_data(tuples_of_hourly_weather_instances_list)

        if tuples_of_hourly_weather_instances_list[0][0].sunset_time is None:
            results_matrix = np.empty(shape=(3, 0))
            results_matrix = np.append(arr=results_matrix, values=np.array(object=[["Best Time to Go Out in " + location_name + ":"],
                                                                               ["Feels-like Temperature Range:"],
                                                                               ["UV Index Range:"]]),
                                   axis=1)

            for data in data_list:
                results_matrix = np.append(arr=results_matrix, values=np.array(object=[[data[0]],
                                                                                       [data[1]],
                                                                                       [data[2]]]),
                                           axis=1)
        else:
            results_matrix = np.empty(shape=(4, 0))
            results_matrix = np.append(arr=results_matrix,
                                       values=np.array(object=[["Best Time to Go Out in " + location_name + ":"],
                                                               ["Feels-like Temperature Range:"],
                                                               ["UV Index Range:"],
                                                               ["Sunset at " + str(tuples_of_hourly_weather_instances_list[0][0].sunset_time)]]),
                                       axis=1)

            for data in data_list:
                results_matrix = np.append(arr=results_matrix, values=np.array(object=[[data[0]],
                                                                                       [data[1]],
                                                                                       [data[2]],
                                                                                       [""]]),
                                           axis=1)

            # print("Sunset time: " + str(tuples_of_hourly_weather_instances_list[0][0].sunset_time))
            # print("results_matrix: " + str(results_matrix))
    else:
        results_matrix = np.array(object=[["Weather is bad in " + location_name + " for the rest of the day."],
                                          [exercise.capitalize() + " is not recommended."],
                                          ["Drive instead or try a different exercise."]])

    results_matrix = results_matrix.astype(dtype=str)
    return results_matrix

if __name__ == "__main__":
    get_results_matrix("Imperial", "Walking", "M1P 3G4")