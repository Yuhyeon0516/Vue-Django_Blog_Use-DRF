import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView
from api.utils import obj_to_post

from blog.models import Post


@method_decorator(ensure_csrf_cookie, name="dispatch")
class HomeView(ListView):
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        paramCate = self.request.GET.get("category")
        paramTag = self.request.GET.get("tag")

        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        elif paramTag:
            qs = Post.objects.filter(tags__name__iexact=paramTag)
        else:
            qs = Post.objects.all()

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        postList = [obj_to_post(obj) for obj in context["object_list"]]
        pageCnt = context["paginator"].num_pages
        curPage = context["page_obj"].number

        dataDict = {
            "postList": postList,
            "pageCnt": pageCnt,
            "curPage": curPage,
        }

        context["myJson"] = json.dumps(dataDict)

        return context
