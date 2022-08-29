import pandas as pd
import mlrun
from mlrun import MLClientCtx
def data_fetch(context:MLClientCtx,num_rows):
    values=[]
    for i in num_rows:
        values.append(i)
    df = pd.DataFrame(data={"col1":values})
    context.log_dataset(key='df_1',df=df,format='csv')
        