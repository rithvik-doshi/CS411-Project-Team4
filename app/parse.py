import json


def parser(input_in_json, date):

    input_dic = json.loads(input_in_json)

    date = date[:10] if len(date) >= 10 else "None"

    print(date, type(input_dic))

    specific_flight_info = {}

    for i in input_dic['flights']:

        choosedate = "None"
        try:
            choosedate = i['scheduled_out'][:10]
        except:
            pass

        if choosedate == date:
            specific_flight_info = i

    specific_flight_info = {key: specific_flight_info[key] for key in [
        'ident', 'aircraft_type', 'arrival_delay', 'origin', 'destination', 'estimated_in',
        'estimated_out', 'actual_on', 'actual_off']}

    out_info = bytes(json.dumps(specific_flight_info), 'utf-8')

    print(type(out_info), type(input_in_json))

    return out_info
