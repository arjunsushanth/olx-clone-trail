from django.urls import path
from product import views
from product.views import UserEditView

urlpatterns=[
    path("register",views.SignupView.as_view(),name="register"),
    path("",views.SigninView.as_view(),name="signin"),
    path("index",views.HomeView.as_view(),name='home'),
    path("productlist",views.ProductListView.as_view(),name="product_list"),
    path("product/details/<int:id>", views.ProductDetailView.as_view(), name="product-details"),
    path("postproduct",views.ProductAddView.as_view(),name='productadd'),
    path("logout",views.logout_view,name='signout'),
    path("editprofile",views.UserEditView.as_view(), name='user_edit'),
    # path("userprofile",views.UserProfile.as_view(),name="userprofile")
    path("userprofile",views.profile_view,name="userprofile")
    
]