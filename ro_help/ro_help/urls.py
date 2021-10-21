"""ro_help URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from .views import StaticPageView


urlpatterns = (
    i18n_patterns(
        path("about/", StaticPageView.as_view(template_name="about.html"), name="about"),
        path("rules/", StaticPageView.as_view(template_name="rules.html"), name="rules"),
        path("contact/", StaticPageView.as_view(template_name="contact.html"), name="contact"),
        path("terms/", StaticPageView.as_view(template_name="terms_and_conditions.html"), name="terms"),
        path("cookies/", StaticPageView.as_view(template_name="cookies.html"), name="cookies"),
        path("updates/", StaticPageView.as_view(template_name="updates.html"), name="updates"),
        path("mobilpay/", include("mobilpay.urls", namespace="mobilpay")),
        path("admin/", admin.site.urls),
        path(
            "admin/password_reset/",
            auth_views.PasswordResetView.as_view(html_email_template_name="registration/password_reset_email.html"),
            name="admin_password_reset",
        ),
        path("admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
        path(
            "admin/reset/<uidb64>/<token>/",
            auth_views.PasswordResetConfirmView.as_view(template_name="registration/set_password.html"),
            name="password_reset_confirm",
        ),
        path("admin/reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
        path("", include("hub.urls")),
    )
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
