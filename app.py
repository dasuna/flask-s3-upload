from flask import Flask, request, render_template
import boto3


app = Flask(__name__)


s3 = boto3.resource(
    's3',
    #aws_access_key_id     = keys.ACCESS_KEY_ID,
    #aws_secret_access_key = keys.ACCESS_SECRET_KEY,
    region_name           = 'us-east-1',
)

@app.route('/')
def root_route():
    #dynamodb.create_table_movie()
    #return 'Table Created'
    return render_template("index.html")
    
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['myimage']
    filename = file.filename
    bucket_name = 'labstack-534793a3-8383-48d2-aa77-0841335-s3bucket-7dlkzmn65kau'
    s3.Bucket(bucket_name).put_object(Key=filename, Body=file)
    return 'File uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')