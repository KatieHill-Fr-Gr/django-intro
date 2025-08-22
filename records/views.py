from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Record
from .serializers.common import RecordSerializer

# * Path: /records

class RecordListView(APIView):

    # Index route
    def get(self, request):
        records = Record.objects.all()
        serialized_records = RecordSerializer(records, many=True)
        print('serialized_records.data')
        return Response(serialized_records.data)
    
    # Create route
    def post(self, request):
        serialized_records = RecordSerializer(data=request.data)
        serialized_records.is_valid()
        return Response('Hit create route')
    
# * Path: /records/<record:pk>/

class RecordDetailView(APIView):
     
    # NotFound helper function
    def get_record(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist as e:
            print(e)
            raise NotFound('Record not found in archive')
        
    # Show route
    def get(self, request, pk):
        record = self.get_record(pk)
        serialized_record = RecordSerializer(record)
        return Response(serialized_record.data)
    
    # Update route
    def put(self, request, pk):
        country = self.get_record(pk)
        serialized_record = RecordSerializer(country, data=request.data, partial=True)
        serialized_record.is_valid()
        return Response(serialized_record.validated_data)
    
    # Delete route
    def delete(self, request, pk)
        record = self.get_record(pk)
        record.delete()
        return Response(status=201)


