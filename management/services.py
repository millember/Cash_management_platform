from django.core.exceptions import ValidationError
from .models import Category, SubCategory

class MovementValidationRules:
    @staticmethod
    def validate_category_type(category_id, type_id):
        """Проверяет соответствие категории и типа"""
        if not Category.objects.filter(id=category_id, type_id=type_id).exists():
            raise ValidationError(
                "Выбранная категория не принадлежит указанному типу операции",
                code="invalid_category_type"
            )

    @staticmethod
    def validate_subcategory_category(subcategory_id, category_id):
        """Проверяет соответствие подкатегории и категории"""
        if not SubCategory.objects.filter(id=subcategory_id, category_id=category_id).exists():
            raise ValidationError(
                "Выбранная подкатегория не принадлежит указанной категории",
                code="invalid_subcategory_category"
            )