from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse

def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            request.session['order_id']=order.id
            # return render(request,'orders/order/created.html',{'order':order})
            return redirect(reverse('templates:process'))
    else:
        form=OrderCreateForm()
    return render(request,'orders/order/create.html',{'form':form,
                                                        'cart':cart,})


