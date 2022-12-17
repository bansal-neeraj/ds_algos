# to understand the basic functioning of a serializer

from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer


class Comment:
    def __init__(self,author,text,num_char):
        self.author = author
        self.text = text
        self.num_char = num_char


class CommentSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=20)
    num_char = serializers.IntegerField()


c1 = Comment('Neeraj','testing serilizers',243)

print(c1.author)
print(c1.text)
print(c1.num_char)

serializer = CommentSerializer(c1)  # convert a model instance to Python native data types
print(serializer.data)

# j = JSONRenderer.render(serializer.data)
# print(j)


