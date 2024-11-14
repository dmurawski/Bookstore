from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView

from books.models import Category

from .forms import EmailForm


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EmailForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            from_email = form.cleaned_data["from_email"]
            send_mail(
                subject,
                message,
                from_email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return self.render_to_response(
                {"form": EmailForm(), "message": "Your email has been sent!"}
            )
        return self.render_to_response({"form": form})
