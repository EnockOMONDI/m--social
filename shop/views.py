from django.shortcuts import render,redirect,get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import Image,Profile,Comment
from .forms import EditProfileForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

@login_required(login_url='/accounts/login/')
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'Gumzo |profile'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'shop/profile/profile.html',{"title":title,
                                                  "comments":comments,
                                                  "image":image,
                                                  "user":current_user,
                                                  "profile":profile,})

@login_required(login_url='/accounts/login/')
def edit(request):
    title = 'Gumzo | edit profile'
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request,'shop/profile/edit.html',{"title":title,
                                                "form":form})

def home(request):
  return render(request, 'shop/product/home.html')
  
def about(request):
  return render(request, 'shop/product/about.html')

def activity(request):
  return render(request, 'shop/product/activity.html')

def members(request):
  return render(request, 'shop/product/members.html')

def groups(request):
  return render(request, 'shop/product/groups.html')

def notfound(request):
  return render(request, 'shop/product/notfound.html')

def contact(request):
  return render(request, 'shop/product/contact.html')


def newsletter(request):
  
      if request.method == 'POST':
         form = NewsLetterForm(request.POST)
         if form.is_valid():
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(email =email)
            recipient.save()
            HttpResponseRedirect('newsletter')
             
      else:
        form = NewsLetterForm()
      return render(request, 'shop/product/contact.html')
    
