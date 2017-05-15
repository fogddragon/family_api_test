import logging

from rest_framework import status
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer

from .serializers import FamilySerializer

# Get an instance of a logger
logger = logging.getLogger('django')

class SaveExampleApiView(views.APIView):
    serializer_class = FamilySerializer
    permission_classes = [AllowAny, ]
    renderer_class = XMLRenderer()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            logger.info(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        file_object = open("example.xml", "w")
        file_object.write(self.renderer_class.render(serializer.data))
        file_object.close()
        logger.info('examle.xml is updated')
        return Response(status=status.HTTP_200_OK)


class CheckFamilyApiView(views.APIView):
    serializer_class = FamilySerializer
    permission_classes = [AllowAny, ]
    renderer_class = XMLRenderer()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            logger.info(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        file_object = open("example.xml", "r")
        file_data = file_object.read()
        file_object.close()
        if self.renderer_class.render(serializer.data) != file_data:
            logger.info("family for check isn't equal to example")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        logger.info("family for check equal to example")
        return Response(status=status.HTTP_200_OK)