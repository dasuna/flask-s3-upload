from flask import Flask, request, render_template
import boto3
import urllib.parse


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
    bucket_name = 'das-flask-bucket77'
    #s3.Bucket(bucket_name).put_object(Key=filename, Body=file)
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(
        Key=filename,
        Body=file,
        ContentType='image/jpeg',
        ContentDisposition='inline'
    )
    
    encoded_object_key = urllib.parse.quote(filename)
    object_url = f"https://{bucket_name}.s3.amazonaws.com/{encoded_object_key}"
    
    return object_url
    

@app.route("/create-bucket", methods=["POST"]) 
def create_bucket():
    bucket_name = request.form["bucket_name"]
    s3.create_bucket(Bucket=bucket_name)
    return 'Bucket was created'


if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')