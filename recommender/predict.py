import os
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from django.conf import settings

model=load_model(os.path.join(settings.BASE_DIR,'recommender/model/model.h5'))
pipeline=joblib.load(os.path.join(settings.BASE_DIR,'recommender/model/pipeline.pkl'))
encoder=joblib.load(os.path.join(settings.BASE_DIR,'recommender/model/encoder.pkl'))

def predict(min_temp,max_pre,min_pre,ph,sh_tol,dr_tol,soil_tex):
    transformed=[list(pipeline.transform([[min_temp,max_pre,min_pre,ph,sh_tol,dr_tol,soil_tex]])[0])]
    transformed[0][2:2]=[int(soil_tex==x) for x in ['','coarse','fine','medium']]
    transformed[0].pop()
    predictions=model.predict(transformed)
    top10=np.argsort(-1*predictions)[:,:10]
    return ([encoder.classes_[x] for x in top10[0]])

