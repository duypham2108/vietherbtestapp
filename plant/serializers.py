from rest_framework import serializers

class SearchQuerySerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   value = serializers.CharField()