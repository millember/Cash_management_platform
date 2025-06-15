from django.urls import path
from . import views

app_name = 'management'
urlpatterns = [
    # Движения денежных средств
    path('', views.MoneyMovementListView.as_view(), name='movement-list'),
    path('create/', views.MoneyMovementCreateView.as_view(), name='movement-create'),
    path('<int:pk>/update/', views.MoneyMovementUpdateView.as_view(), name='movement-update'),
    path('<int:pk>/delete/', views.MoneyMovementDeleteView.as_view(), name='movement-delete'),

    # AJAX
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

    # Справочники
    path('references/', views.ReferenceListView.as_view(), name='reference-list'),

    # Статусы
    path('status/create/', views.StatusCreateView.as_view(), name='status-create'),
    path('status/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status-update'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),

    # Типы
    path('type/create/', views.TypeCreateView.as_view(), name='type-create'),
    path('type/<int:pk>/update/', views.TypeUpdateView.as_view(), name='type-update'),
    path('type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type-delete'),

    # Категории
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Подкатегории
    path('subcategory/create/', views.SubCategoryCreateView.as_view(), name='subcategory-create'),
    path('subcategory/<int:pk>/update/', views.SubCategoryUpdateView.as_view(), name='subcategory-update'),
    path('subcategory/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='subcategory-delete'),
]
