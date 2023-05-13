import pandas as pd
from datetime import date


# Functions
def getDataframe(path, dtype):
    if ".xlsx" in path:
        return pd.read_excel(path, dtype=dtype, )
    elif ".csv" in path:
        return pd.read_csv(
            path, delimiter=",", dtype=dtype, low_memory=False, parse_dates=parse_dates
        )

def concatDataframe(p_df: iter):
    return pd.concat(p_df)

def daytype(p_date: str):
    datelist = p_date.split("-")
    if date(int(datelist[0]), int(datelist[1]), int(datelist[2])).weekday() < 5:
        return 1
    else:  # 5 Sat, 6 Sun
        return 2

def export(p_df, path, sheet):
    p_df.to_excel(path, sheet_name=sheet, index=False)



# Datatypes
dtypes = {"VendorID": float,
          "tpep_pickup_datetime": str,
          "tpep_dropoff_datetime": str,
          "Passenger_count": float,
          "Trip_distance": float,
          "RateCodeID": float,
          "Store_and_fwd_flag": str,
          "PULocationID": float,
          "DOLocationID": float,
          "Payment_type": float,
          "Fare_amountF": float,
          "Extra": float,
          "MTA_tax": float,
          "Tip_amount": float,
          "Tolls_amount": float,
          "Improvement_surcharge": float,
          "Total_amount": float,
          "congestion_surcharge": float
          }

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]





if __name__ == "__main__":
    df1 = getDataframe("./data/yellow_tripdata_2020-01.csv", dtypes)
    df2 = getDataframe("./data/yellow_tripdata_2020-02.csv", dtypes)
    df3 = getDataframe("./data/yellow_tripdata_2020-03.csv", dtypes)
    df = concatDataframe([df1, df2, df3])

    # Add new columns
    df.loc[:, "tpep_pickup_datetime"] = df.loc[:, "tpep_pickup_datetime"].dt.date
    df.loc[:, "mes"] = pd.to_datetime(df.loc[:, "tpep_pickup_datetime"]).dt.to_period('M')
    df.loc[:, "tipo_dia"] = pd.Series(
        df.loc[:, "tpep_pickup_datetime"].apply(lambda x: daytype(str(x)))
    )
    df.loc[:, "total_servicios"] = 1

    # Filter dates
    df = df.loc[df['mes'].astype(str).isin(["2020-01", "2020-02", "2020-03"])]

    # Filter results
    df_JFK = df.loc[df['RatecodeID'] == 2]
    df_regular = df.loc[df['RatecodeID'] == 1]
    df_others = df.loc[(df['RatecodeID'] != 1) & (df['RatecodeID'] != 2)]

    # Get results
    df_list = []
    for value in [df_JFK, df_regular, df_others]:
        df_temp = (
            value.loc[:, ["mes",
                          "tipo_dia",
                          "passenger_count",
                          "trip_distance",
                          "total_servicios"]
            ]
        )
        df_final = df_temp.groupby(['mes', 'tipo_dia'], as_index=False).sum()
        df_list.append(df_final)

    # Export to excel
    export(df_list[0], "Results.xlsx", "JFK")
    export(df_list[1], "Results.xlsx", "Regular")
    export(df_list[2], "Results.xlsx", "Others")
