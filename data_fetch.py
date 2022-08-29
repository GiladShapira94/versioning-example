import pandas as pd
import mlrun
from mlrun import MLClientCtx
def data_fetch(context:MLClientCtx):
    df = pd.DataFrame(data={"col1":[1,2,3,4]})
    context.log_dataset(key='df_1',df=df,format='csv')
        