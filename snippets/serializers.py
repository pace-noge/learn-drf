from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
        fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'title', 'code', 'linenos', 'language','style', 'owner')