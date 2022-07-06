import tempfile
import boto3
import joblib
from sklearn.ensemble import RandomForestRegressor
import os

class Bucket():
    AWS_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET = os.getenv('AWS_SECRET_ACCESS_KEY')

    S3_CLIENT = boto3.client('s3', aws_access_key_id=AWS_ID,
                     aws_secret_access_key=AWS_SECRET)

    BUCKET_NAME = 'ds4a-credit-risk'

    @property
    def bucket(self):
        return self._bucket

    def _load_reg_model(self):
        with tempfile.TemporaryFile() as fp:
            reg_key = 'rf_score_reg.joblib'
            self.S3_CLIENT.download_fileobj(Fileobj=fp, Bucket=self.BUCKET_NAME, Key=reg_key)
            fp.seek(0)
            reg_model = joblib.load(fp)
        return reg_model
    
    def _load_clas_model(self):
        with tempfile.TemporaryFile() as fp:
            clas_key = 'rf_loan_clas.joblib'
            self.S3_CLIENT.download_fileobj(Fileobj=fp, Bucket=self.BUCKET_NAME, Key=clas_key)
            fp.seek(0)
            reg_model = joblib.load(fp)
        return reg_model
