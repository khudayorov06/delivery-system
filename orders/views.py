from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm  # Buyurtma yaratish formasi

from django.shortcuts import render
from .models import Order


def order_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'order_date')  # Standart tartib buyurtma sanasi bo‘yicha
    filter_status = request.GET.get('status')

    orders = Order.objects.all()

    if query:
        orders = orders.filter(customer_name__icontains=query) | orders.filter(food_item__icontains=query)

    if filter_status:
        orders = orders.filter(status=filter_status)

    orders = orders.order_by(sort_by)  # Tartiblash qo‘shildi

    return render(request, 'orders/order_list.html',
                  {'orders': orders, 'sort_by': sort_by, 'filter_status': filter_status})

def create_order(request):
    """Yangi buyurtma yaratish."""
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Buyurtmalar ro‘yxati sahifasiga qaytish
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

# Buyurtmani tahrirlash
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

# Buyurtmani o‘chirish
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
