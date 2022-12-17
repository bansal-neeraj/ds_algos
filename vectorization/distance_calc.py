import csv
import pandas as pd
import numpy as np
import time




def haversine(user_lat, user_lng, v_lat, v_lng):
    # user_lat, user_lng, v_lat, v_lng = map(radians, [user_lat, user_lng, v_lat, v_lng])
    user_lat, user_lng, v_lat, v_lng = map(np.deg2rad, [user_lat, user_lng, v_lat, v_lng])
    dlat = v_lat - user_lat
    dlng = v_lng - user_lng
    a = np.sin(dlat / 2) ** 2 + np.cos(user_lat) * np.cos(v_lat) * np.sin(dlng / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6371 * c
    return km


def normal_loop(lat,lng,citi_list):
    dis_list = [(row[0], haversine(lat, lng, float(row[1]), float(row[2]))) for index, row in enumerate(citi_list)]
    dis_list.sort(key=lambda x: x[1])
    print(dis_list[0])


def main():
    lat = 19.076090
    lng = 72.877426
    #
    # with open('./worldcities.csv') as csvfile:
    #     cities_file = csv.reader(csvfile)
    #     print(next(cities_file))  # remove the head row
    #     citi_list = [(j[0],j[2],j[3]) for j in cities_file]
    #
    # start = time.perf_counter()
    # normal_loop(lat,lng,citi_list)
    # end = time.perf_counter()
    # print(end-start)

    df = pd.read_csv('./worldcities.csv')
    df['distance'] = haversine(lat,lng,df['lat'],df['lng'])
    df.iloc[df.idxmin()]
    # print(df.head())
    # print(df.count())


if __name__ == '__main__':
    main()