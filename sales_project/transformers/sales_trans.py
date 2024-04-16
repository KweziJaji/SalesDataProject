from pandas import DataFrame
import pandas as pd
import os

@transformer
def transform_df(df1,df2,df3, **kwargs) -> DataFrame:
    df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
    filtered_df = df1.loc[(df1['date'] >= '2017-01-01') & (df1['date'] < '2018-01-01')]
    sales_prodDF = pd.merge(filtered_df,df2,on='product_id',how='left')
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
