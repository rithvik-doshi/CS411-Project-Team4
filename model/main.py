def predict_cancellation(MONTH, DAY,AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT, DISTANCE, Day):
    """

    :param MONTH:
    :param DAY:
    :param ORIGIN_AIRPORT:
    :param DESTINATION_AIRPORT:
    :param DISTANCE:
    :param Day:
    :return:
    """
    import pickle
    import pandas as pd
    import joblib
    import numpy as np
    # np.reshape()
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    dummies_columns = pickle.load(open("dummies.pkl", 'rb'))
    SVC = joblib.load('model.pkl')

    df1 = pd.get_dummies(pd.DataFrame({'AL':[AIRLINE],'OA':[ORIGIN_AIRPORT], 'DA':[DESTINATION_AIRPORT]
                                   ,'Day':[Day]}))

    df3 = df1.reindex(columns=dummies_columns, fill_value=0)

    df2 = pd.DataFrame({'MONTH': [MONTH], 'DAY': [DAY],
                        'DISTANCE': [DISTANCE]})

    df_data = pd.concat([df2, df3], axis=1)

    df_data = scaler.transform(df_data)


    result = SVC.predict(df_data)
    return result

if __name__ == '__main__':
    #df3 = pd.DataFrame({'MONTH':[12],'DAY':[1],'DISTANCE':[1448]})
    x = predict_cancellation(2,28,'MQ','GUC','DFW',678,'Saturday')
    print(x)