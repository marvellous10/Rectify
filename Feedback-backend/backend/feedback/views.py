from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dotenv import load_dotenv

from .models import *
from .serializers import *


load_dotenv()

class SendFeedback(APIView):
    def get(self, request, format=None, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        if feedbacks:
            try:
                feedback_serializer = FeedbackSerializer(feedbacks, many=True)
                return Response(
                    {
                        "Feedbacks": feedback_serializer.data    
                    },
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {
                        "message": f"Cannot retrieve feedbacks due to {e}"    
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    "message": "There are no feedbacks"
                },
                status=status.HTTP_204_NO_CONTENT
            )
        
    
    def post(self, request, format=None, *args, **kwargs):
        user_id = request.data['User_id']
        feedback_type = request.data['Feedback_type']
        feedback_text = request.data['Feedback_text']
        
        if user_id and feedback_text is not None:
            try:
                user_input = {
                    "user_id": user_id,
                    "feedback_type": feedback_type,
                    "feedback_text": feedback_text
                }
                feedback_serializer = FeedbackSerializer(data=user_input)
                if feedback_serializer.is_valid(raise_exception=True):
                    feedback_serializer.save()
                    return Response(
                        {
                            "message": "Feedback has been sent"
                        },
                        status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        {
                            "message": "Could not send feedback, try again"
                        },
                        status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(
                    {
                        "message": "An error occurred, please try again later"
                    },
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    "message": "User ID and Feedback cannot be empty"
                },
                status=status.HTTP_204_NO_CONTENT)