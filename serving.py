import pandas as pd
import mlrun
from mlrun import MLClientCtx
def data_fetch(event):
    event['num']+=2
    return event

        
