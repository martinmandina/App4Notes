from django.shortcuts import render,redirect
from .models import Notes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notes
from .serializer import NoteSerializer
from rest_framework import status




# Create your views here.

def main(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Notes.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if noteid > 0:
            note = Notes.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()
            return redirect('/?noteid=%i' % noteid)
        else:
            note = Notes.objects.create(title=title, content=content)
            return redirect('/?noteid=%i' % note.id)

    if noteid > 0:
        note = Notes.objects.get(pk=noteid)
        # return redirect('/noteid')
    else:
        note = ''

    context = {
        'noteid': noteid,
        'notes': notes,
        'note': note
    }

    return render(request,'main.html',context)

def delete_note(request, noteid):
    note = Notes.objects.get(pk=noteid)
    note.delete()

    return redirect('/?noteid=0')

class NoteList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_notes = Notes.objects.all()
        serializers = NoteSerializer(all_notes, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
 
class Notesingle(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get_note(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        note = self.get_note(pk)
        serializers = NoteSerializer(note)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        note = self.get_note(pk)
        serializers = NoteSerializer(note, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_note(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


