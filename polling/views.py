from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView  # added for class based view
from django.views.generic.detail import DetailView  # added for class based view

class PollListView(ListView):  # added for class based view
    model = Poll
    template_name = 'polling/list.html'

# def list_view(request):
#     context = {'polls': Poll.objects.all()}
#     return render(request, 'polling/list.html', context)

class PollDetailView(DetailView):  # added for class based view
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {'object': poll}
        return render(request, 'polling/detail.html', context)

# def detail_view(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404

#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()

#     context = {'poll': poll}
#     return render(request, 'polling/detail.html', context)
