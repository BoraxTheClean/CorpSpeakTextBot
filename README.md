# CorpSpeakTextBot

* To Package Python:
```
cd src
zip -r deploy.zip .
```
* To Package Cloudformation:
```
aws cloudformation package --template-file template.yaml --s3-bucket YOUR-S3-BUCKET --s3-prefix corp-speak-app \
--output-template-file processed-template.yaml
```
* To Deploy:
```
aws cloudformation deploy --template-file processed-template.yaml --stack-name corp-speak-app --parameter-overrides PhoneNumbers=+11234567890 --capabilities CAPABILITY_IAM
```
