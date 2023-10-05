from hackathon.utils import predict_anomalies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AnomalyDetectionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            anomalies = predict_anomalies(data)

            if not anomalies:
                return Response({"status": "Normal"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "Anomalies detected in fields:", "anomalies": anomalies}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


