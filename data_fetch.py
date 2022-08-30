import pandas as pd
import mlrun
from mlrun import MLClientCtx
import time
def data_fetch(context:MLClientCtx):
    time.sleep(300)
    df = pd.DataFrame(data={"col1":[1,2,3,4,5,6]})
    context.log_dataset(key='df_2',df=df,format='csv')
        
