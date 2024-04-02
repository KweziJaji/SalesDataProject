from pandas import DataFrame
import pandas as pd
import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).getOrCreate()
      
spark._jsc.hadoopConfiguration().set("spark.hadoop.google.cloud.auth.service.account.enable","True")
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile","/home/src/sales_project/gc_creds.json")

@transformer
def transform_df(df1,df2,df3, **kwargs) -> DataFrame:

    import datetime as dt

    # df1['date'] = pd.to_datetime(df1['date'])

    #include = df1[df1['date'].dt.year == 2017]
    sales_prodDF = pd.merge(df1,df2,on='product_id',how='left')
    sales_storeDF = pd.merge(sales_prodDF,df3,on ='store_id',how='left')
    sales_storeDF[["sales","revenue","stock"]] = sales_storeDF[["sales","revenue","stock"]].fillna(0)
    sales_storeDF[["promo_bin_2","promo_discount_2","promo_discount_type_2"]] = sales_storeDF[["promo_bin_2","promo_discount_2","promo_discount_type_2"]].fillna("Unknown")
    return sales_storeDF

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'