from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse

from .models import MoneyMovement, Status, Type, Category, SubCategory
from .forms import MoneyMovementForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm


class MoneyMovementListView(ListView):
    model = MoneyMovement
    template_name = 'management/movement_list.html'
    context_object_name = 'movements'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.GET

        # Фильтрация по дате
        if date_from := params.get('date_from'):
            queryset = queryset.filter(date__gte=date_from)
        if date_to := params.get('date_to'):
            queryset = queryset.filter(date__lte=date_to)

        # Фильтрация по другим параметрам
        filter_fields = ['status', 'type', 'category', 'subcategory']
        for field in filter_fields:
            if value := params.get(field):
                queryset = queryset.filter(**{f'{field}_id': value})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


class MoneyMovementCreateView(CreateView):
    model = MoneyMovement
    form_class = MoneyMovementForm
    template_name = 'management/movement_form.html'
    success_url = reverse_lazy('management:movement-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание новой операции'
        return context

    def form_valid(self, form):
        # Дополнительная обработка перед сохранением
        return super().form_valid(form)


class MoneyMovementUpdateView(UpdateView):
    model = MoneyMovement
    form_class = MoneyMovementForm
    template_name = 'management/movement_form.html'
    success_url = reverse_lazy('management:movement-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование операции'
        return context


class MoneyMovementDeleteView(DeleteView):
    model = MoneyMovement
    template_name = 'management/confirm_delete.html'
    success_url = reverse_lazy('management:movement-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = 'операцию'
        context['details'] = f"от {self.object.date.strftime('%d.%m.%Y')} на сумму {self.object.amount} руб."
        return context


def load_categories(request):
    type_id = request.GET.get('type')
    if not type_id:
        return JsonResponse({'error': 'Type ID is required'}, status=400)

    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return render(request, 'management/category_dropdown_list_options.html', {'categories': categories})


def load_subcategories(request):
    category_id = request.GET.get('category')
    if not category_id:
        return JsonResponse({'error': 'Category ID is required'}, status=400)

    subcategories = SubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'management/subcategory_dropdown_list_options.html', {'subcategories': subcategories})


# Справочники
class ReferenceListView(ListView):
    template_name = 'management/reference_list.html'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


# CRUD для статусов
class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание статуса'
        return context


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование статуса'
        return context


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'management/confirm_delete.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = 'статус'
        context['details'] = f'"{self.object.name}"'
        return context


# CRUD для типов
class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание типа операции'
        return context


class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование типа операции'
        return context


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'management/confirm_delete.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = 'тип операции'
        context['details'] = f'"{self.object.name}"'
        return context


# CRUD для категорий
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'management/confirm_delete.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = 'категорию'
        context['details'] = f'"{self.object.name}"'
        return context


# CRUD для подкатегорий
class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание подкатегории'
        return context


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'management/reference_form.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование подкатегории'
        return context


class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'management/confirm_delete.html'
    success_url = reverse_lazy('management:reference-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = 'подкатегорию'
        context['details'] = f'"{self.object.name}"'
        return context
