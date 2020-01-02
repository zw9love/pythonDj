from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Medical
from rest_framework import status
import mysql.connector

@api_view(['POST'])
def save_medical(request):
    # ----- YAML below for Swagger -----
    """
    description: This API deletes/uninstalls a device.
    parameters:
      - name: name
        type: string
        required: true
        location: form
      - name: bloodgroup
        type: string
        required: true
        location: form
      - name: birthmark
        type: string
        required: true
        location: form
    """
    name = request.POST.get('name')
    bloodgroup = request.POST.get('bloodgroup')
    birthmark = request.POST.get('birthmark')

    # try:
    #     Medical.objects.create(name= name, bloodgroup = bloodgroup, birthmark = birthmark)
    #     return Response("Data Saved!", status=status.HTTP_201_CREATED)
    #
    # except Exception as ex:
    #     return Response(ex, status=status.HTTP_400_BAD_REQUEST)

    print(request.data)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="159357",
        database="test",
    )

    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select  * from user")
    myresult = mycursor.fetchall()
    # # print myresult
    # for x in myresult:
    #     print(x['id'])

    mycursor.close()
    return Response({'data': '', 'message': myresult, 'code': 200})


@api_view(['GET'])
def get_medical(request):
    token = request.META.get('TOKEN')
    print('request.methods', request.method)
    print('request.META', token)
    params = request.query_params
    params.token = token
    return Response({'data': params, 'message': 'hello world!!!', 'code': 200})
    # return Response(Medical.objects.all().values(), status=status.HTTP_200_OK)