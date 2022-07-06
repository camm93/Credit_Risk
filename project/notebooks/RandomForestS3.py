import tempfile
import boto3
import joblib
from sklearn.ensemble import RandomForestRegressor
import os

# $ENV:AWS_ACCESS_KEY_ID = "AKIAURCFGZN4UB5MXKQS"
# $ENV:AWS_SECRET_ACCESS_KEY = "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"
aws_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')

print('ID: ', aws_id)

s3_client = boto3.client('s3', aws_access_key_id=aws_id,
                     aws_secret_access_key=aws_secret)

bucket_name = 'ds4a-credit-risk'
object_key = 'rf_score_reg.joblib'

# # WRITE
# with tempfile.TemporaryFile() as fp:
#     joblib.dump(model, fp)
#     fp.seek(0)
#     s3_client.put_object(Body=fp.read(), Bucket=bucket_name, Key=key)

# # READ
with tempfile.TemporaryFile() as fp:
    s3_client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key=object_key)
    fp.seek(0)
    model = joblib.load(fp)

import time
start_time = time.time()
# observation to predict
observation = [[7.89, 68000.00, 9000.00, 12.44, #int_rate, annual_inc, loan_amnt, dti, inq_last_6mths
              0.00, #inq_last_6mths
              30, #Grade A
              0.00, 0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, #purpose debt_consolidation
              0.00, 0.00, 0.00, 0.00, 0.00, 
              1.00, 0.00 #term 36 months
              ]]

# Make the prediction
result_score = model.predict(observation)
print("The predicted score is: ", result_score[0])
print("--- %s seconds ---" % (time.time() - start_time))