// Основные скрипты
$(document).ready(function() {
    // Инициализация всплывающих подсказок
    $('[data-bs-toggle="tooltip"]').tooltip();

    // Подтверждение удаления
    $('.btn-delete').click(function(e) {
        if (!confirm('Вы уверены, что хотите удалить эту запись?')) {
            e.preventDefault();
        }
    });

    // Динамическая загрузка категорий для фильтров
    $('#type-filter').change(function() {
        var typeId = $(this).val();
        if (typeId) {
            $.ajax({
                url: '/ajax/load-categories/',
                data: {
                    'type': typeId
                },
                success: function(data) {
                    $('#category-filter').html(data);
                    $('#subcategory-filter').html('<option value="">Все</option>');
                }
            });
        } else {
            $('#category-filter').html('<option value="">Все</option>');
            $('#subcategory-filter').html('<option value="">Все</option>');
        }
    });

    // Динамическая загрузка подкатегорий для фильтров
    $('#category-filter').change(function() {
        var categoryId = $(this).val();
        if (categoryId) {
            $.ajax({
                url: '/ajax/load-subcategories/',
                data: {
                    'category': categoryId
                },
                success: function(data) {
                    $('#subcategory-filter').html(data);
                }
            });
        } else {
            $('#subcategory-filter').html('<option value="">Все</option>');
        }
    });
});
