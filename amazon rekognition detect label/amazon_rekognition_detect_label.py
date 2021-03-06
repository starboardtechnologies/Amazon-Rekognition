import boto3

#Main function for file

if __name__ == "__main__"

    imageFile='input.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image=('Bytes': image.read()))

print('Detected labels in ' + imageFile)
for label in response('Labels'):
    print (label)['Name'] + ' : ' + str(label['Confidence']))

print(Completed)