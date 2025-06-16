from django import forms
from django.core.exceptions import ValidationError

from .models import MoneyMovement, Status, Type, Category, SubCategory
import logging
from .services import MovementValidationRules

logger = logging.getLogger(__name__)


class MoneyMovementForm(forms.ModelForm):
    class Meta:
        model = MoneyMovement
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError) as e:
                logger.warning(f"Ошибка обработки type_id: {e}")
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.category_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by(
                    'name')
            except (ValueError, TypeError) as e:
                logger.warning(f"Ошибка обработки category_id: {e}")
                self.fields['subcategory'].queryset = SubCategory.objects.none()
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')

    def clean(self):
        cleaned_data = super().clean()

        # Get field values
        type_obj = cleaned_data.get('type')
        category_obj = cleaned_data.get('category')
        subcategory_obj = cleaned_data.get('subcategory')

        # Apply business rules
        if type_obj and category_obj:
            try:
                MovementValidationRules.validate_category_type(category_obj.id, type_obj.id)
            except ValidationError as e:
                self.add_error('category', e)

        if category_obj and subcategory_obj:
            try:
                MovementValidationRules.validate_subcategory_category(subcategory_obj.id, category_obj.id)
            except ValidationError as e:
                self.add_error('subcategory', e)

        return cleaned_data


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
