import pandas as pd 
#predict model
def predict_model(data_record,model):
    y_pred=model.predict(data_record)
    catBoost_predict_prob=model.predict_proba(data_record)
    catBoost_confidence_score=max(catBoost_predict_prob[0])
    #catBoost_pred_score = model.predict(x).tolist()[0]
    #catBoost_confidence_score = round(model.predict_proba(x)[0][catBoost_pred_score], 2)
    return y_pred[0],catBoost_confidence_score
