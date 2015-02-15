from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format="html")
    
    
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('url', 'highlight',  'owner', 'id', 'title', 'code', 'linenos', 'language','style')