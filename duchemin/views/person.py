from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from duchemin.serializers.person import DCPersonListSerializer, DCPersonDetailSerializer
from duchemin.models.person import DCPerson
from duchemin.renderers.custom_html_renderer import CustomHTMLRenderer


class PersonListHTMLRenderer(CustomHTMLRenderer):
    template_name = "person/person_list.html"

class PersonDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "person/person_detail.html"

class PersonList(generics.ListAPIView):
    model = DCPerson
    serializer_class = DCPersonListSerializer
    renderer_classes = (JSONRenderer, PersonListHTMLRenderer)

class PersonDetail(generics.RetrieveAPIView):
    model = DCPerson
    serializer_class = DCPersonDetailSerializer
    renderer_classes = (JSONRenderer, PersonDetailHTMLRenderer)

# def people(request):
#     people = DCPerson.objects.all().order_by('surname')
#     paginator = Paginator(people, 20)
#     page = request.GET.get('page')
#     try:
#         all_people = paginator.page(page)
#     except PageNotAnInteger:
#         all_people = paginator.page(1)
#     except EmptyPage:
#         all_people = paginator.page(paginator.num_pages)

#     return render(request, 'main/people.html', {'people': all_people})


# def person(request, person_id):
#     try:
#         person = DCPerson.objects.get(person_id=person_id)
#     except DCPerson.DoesNotExist:
#         raise Http404

#     pieces = DCPiece.objects.filter(composer_id=person.person_id)
#     analyses = DCAnalysis.objects.filter(analyst=person.person_id)

#     data = {
#         'person': person,
#         'pieces': pieces,
#         'analyses': analyses
#     }
#     return render(request, 'main/person.html', data)