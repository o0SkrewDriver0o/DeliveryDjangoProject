from django.contrib import admin
from .models import Dish, Restaurant, MenuItem, Cart, Order, Person, Review, OrderItem, Category

# Регистрация моделей
admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Person)
admin.site.register(OrderItem)
admin.site.register(Category)


class RestaurantReviewFilter(admin.SimpleListFilter):
    title = 'Ресторан'
    parameter_name = 'restaurant'

    def lookups(self, request, model_admin):
        # Assuming you want to filter by orders with reviews:
        restaurants = Restaurant.objects.filter(order__have_review=True).distinct()
        return [(restaurant.id, restaurant.name) for restaurant in restaurants]

    def queryset(self, request, queryset):
        if self.value() == 'all':
            return queryset  # Return all reviews regardless of restaurant
        elif self.value():
            return queryset.filter(order__restaurant__id=self.value())
        return queryset


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'review_text')
    list_filter = (RestaurantReviewFilter,)


admin.site.register(Review, ReviewAdmin)


def export_restaurant_reviews_to_excel(modeladmin, request, queryset):
    # Создаем новый workbook и активный лист
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Reviews'

    # Устанавливаем заголовки столбцов
    columns = ['Restaurant', 'User', 'Review Text', 'Delivery Speed Rating', 'Taste Intensity Rating', 'Product Quality Rating', 'Service Quality Rating']
    for col_num, column_title in enumerate(columns, 1):
        column_letter = get_column_letter(col_num)
        ws[column_letter + '1'] = column_title

    # Заполняем данные
    row_num = 2
    for restaurant in queryset:
        reviews = Review.objects.filter(order__restaurant=restaurant)
        for review in reviews:
            ws[f'A{row_num}'] = restaurant.name
            ws[f'B{row_num}'] = review.user.username
            ws[f'C{row_num}'] = review.review_text
            ws[f'D{row_num}'] = review.delivery_speed_rating
            ws[f'E{row_num}'] = review.taste_intensity_rating
            ws[f'F{row_num}'] = review.product_quality_rating
            ws[f'G{row_num}'] = review.service_quality_rating
            row_num += 1

    # Устанавливаем правильные размеры столбцов
    for col_num in range(1, len(columns) + 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].auto_size = True

    # Создаем HTTP ответ
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=restaurant_reviews.xlsx'
    wb.save(response)
    return response

export_restaurant_reviews_to_excel.short_description = "Export selected restaurants' reviews to Excel"

class RestaurantAdmin(admin.ModelAdmin):
    actions = [export_restaurant_reviews_to_excel]
