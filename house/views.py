from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from house.models import Project, Profile, Order, Status


# Create your views here.

def index(request):
    return render(request, 'house/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('myprofile')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'house/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('myprofile')
        else:
            messages.info(request, 'Неправильный пароль/логин')
            return redirect('signin')

    return render(request, 'house/signin.html')


@login_required(login_url='signin')
def profile(request, pk):
    user_profile = Profile.objects.get(user=request.user)
    user_orders = Order.objects.filter(user=request.user).select_related('project')
    count = Order.objects.filter(user=request.user).count()

    if request.method == 'POST':
        contacts = request.POST['contacts']
        location = request.POST['location']
        number = request.POST['number']

        user_profile.location = location
        user_profile.contacts = contacts
        user_profile.number = number
        user_profile.save()
        messages.info(request, 'Information updated')
        return redirect(request.META['HTTP_REFERER'])

    context = {
        'user_profile': user_profile,
        'user_orders': user_orders,
        'count': count,
    }

    return render(request, 'house/profile.html', context)


@login_required(login_url='signin')
def moder(request):
    user_orders = Order.objects.all().select_related('project')
    users = Profile.objects.all()
    status = Status.objects.all()
    projects = Project.objects.all()
    users_count = users.count()
    order_count = user_orders.count()

    paginator = Paginator(users, 5)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {
        'user_orders': user_orders,
        'order_count': order_count,
        'users': users,
        'users_count': users_count,
        'projects': projects,
        "page_object": page_object,
        'status': status,
    }
    return render(request, 'house/moder.html', context=context)


@login_required(login_url='signin')
def delete(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        project = Project.objects.filter(id=pk)
        project.delete()
        return redirect('projectsPage')
    return redirect('projectsPage')


@login_required(login_url='signin')
def deleteorder(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        order = Order.objects.filter(id=pk)
        print(pk)
        print(order)
        order.delete()
        return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='signin')
def updateproject(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        project = Project.objects.get(id=pk)
        name = request.POST['name']
        description = request.POST['description']
        area = request.POST['area']
        height = request.POST['height']
        roof = request.POST['roof']
        floors = request.POST['floors']
        dimensions = request.POST['dimensions']
        ceiling_height = request.POST['ceiling_height']
        price = request.POST['price']
        photo_1 = request.FILES['photo_1']
        photo_2 = request.FILES['photo_2']
        photo_3 = request.FILES['photo_3']

        project.name = name
        project.description = description
        project.area = area
        project.height = height
        project.roof = roof
        project.floors = floors
        project.dimensions = dimensions
        project.ceiling_height = ceiling_height
        project.price = price
        project.photo_1 = photo_1
        project.photo_2 = photo_2
        project.photo_3 = photo_3

        project.save()
        return redirect(request.META['HTTP_REFERER'], )
    return redirect(request.META['HTTP_REFERER'], )


def addnewproject(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        area = request.POST['area']
        height = request.POST['height']
        roof = request.POST['roof']
        floors = request.POST['floors']
        dimensions = request.POST['dimensions']
        ceiling_height = request.POST['ceiling_height']
        price = request.POST['price']
        photo_1 = request.FILES['photo_1']
        photo_2 = request.FILES['photo_2']
        photo_3 = request.FILES['photo_3']

        # Create a new Project instance
        project = Project(
            name=name,
            slug=name,
            description=description,
            area=area,
            height=height,
            roof=roof,
            floors=floors,
            dimensions=dimensions,
            ceiling_height=ceiling_height,
            type_id=1,
            price=price,
            photo_1=photo_1,
            photo_2=photo_2,
            photo_3=photo_3
        )
        project.save()

        # Redirect to the desired page after adding the project
        return redirect('projectsPage')  # Replace 'project-list' with the actual URL or view name

    return render(request, 'project/add.html')  # Replace 'project/add.html' with the actual template path


def updateorder(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        order = Order.objects.get(id=pk)

        if request.FILES.get('file') is None:
            status_id = request.POST['status']
            status = Status.objects.get(id=status_id)  # Retrieve the Status instance
            order.status = status  # Assign the Status instance to order.status

            order.save()
            messages.info(request, 'Изменения сохранены')
            return redirect(request.META['HTTP_REFERER'])
        if request.FILES.get('file') is not None:
            file = request.FILES.get('file')

            status_id = request.POST['status']
            status = Status.objects.get(id=status_id)  # Retrieve the Status instance

            order.file = file
            order.status = status  # Assign the Status instance to order.status
            order.save()
            messages.info(request, 'Изменения сохранены')
            return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])


def logout(request):
    auth.logout(request)
    return redirect('signin')


def search(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        projects = Project.objects.filter(name__icontains=project_name)

    context = {
        'projects': projects,
    }
    return render(request, 'house/projects.html', context=context)


def order(request):
    if request.method == 'POST':
        project_id = request.POST['project_id']
        file = request.FILES.get('file_upload')
        user = request.user.username

        auth = request.user.is_authenticated

        if auth:
            print(123)
            project_object = Project.objects.get(id=project_id)

            if Order.objects.filter(user=user, project=project_object, status_id=1).first():
                messages.info(request, 'Ваш заказ уже принят!')
                return redirect(request.META['HTTP_REFERER'])
            else:
                new_project = Order.objects.create(user=user, project=project_object, file=file, status_id=1)
                new_project.save()
                messages.info(request, 'Заказ принят')
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, 'Пройдите регистрацию или войдите в аккаунт')
            return redirect(request.META['HTTP_REFERER'])

        # project_object = Project.objects.get(id=pk)
    # print(project_object)
    # print(pk)

    return redirect(request.META['HTTP_REFERER'])


def projectsPage(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'house/projects.html', context=context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(request, 'house/project.html', context=context)


def contacts(request):
    return render(request, 'house/contacts.html', )


def calculator(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        floor = request.POST['floor']
        length = float(request.POST['length'])
        width = float(request.POST['width'])
        length1floor = float(request.POST['length1floor'])
        width_of_wall = float(request.POST['width_of_wall'])
        general_length = float(request.POST['general_length'])
        width_of_inner_wall = float(request.POST['width_of_inner_wall'])
        width_of_cherdak = float(request.POST['width_of_cherdak'])
        montazh = request.POST['montazh']
        fundament = request.POST['fundament']
        window = request.POST['window']
        krovlya = request.POST['krovlya']

        area_out_wall = width_of_wall + 10
        area_inner_wall = general_length * 3
        total_area = length * width

        # Calculate the approximate total price based on the area and selected options
        price_per_sqm = 9120  # Example price per square meter
        total_price = total_area * price_per_sqm

        # Add the calculated values to the context dictionary
        context = {
            'floor': floor,
            'length': length,
            'width': width,
            'length1floor': length1floor,
            'total_area': total_area,
            'width_of_wall': width_of_wall,
            'general_length': general_length,
            'width_of_inner_wall': width_of_inner_wall,
            'width_of_cherdak': width_of_cherdak,
            'montazh': montazh,
            'fundament': fundament,
            'window': window,
            'krovlya': krovlya,
            'area_out_wall': area_out_wall,
            'area_inner_wall': area_inner_wall,
            'total_price': total_price,
            'projects': projects,

        }

        messages.info(request, 'Calculated')
        return render(request, 'house/calculator.html', context=context)

    return render(request, 'house/calculator.html', {'projects': projects})


# HANDLE ERRORS
def error400(request, exception):
    return HttpResponseNotFound('<h1>Page not found 400</h1>')
    # return render(request, 'messenger/errors/400.html', status=400)


def error403(request, exception):
    return HttpResponseNotFound('<h1>Page not found 403 </h1>')
    # return render(request, 'messenger/errors/403.html', status=403)


def error404(request, exception):
    return HttpResponseNotFound('<h1>Page not found 404</h1>')


def error500(request):
    return HttpResponseNotFound('<h1>Page not found 500</h1>')
    # return render(request, 'messenger/errors/500.html', status=500)


@login_required(login_url='signin')
def myprofile(request):
    user_profile = Profile.objects.get(user=request.user)
    user_orders = Order.objects.filter(user=request.user).select_related('project')
    count = Order.objects.filter(user=request.user).count()

    if request.method == 'POST':
        contacts = request.POST['contacts']
        location = request.POST['location']
        number = request.POST['number']

        user_profile.location = location
        user_profile.contacts = contacts
        user_profile.number = number
        user_profile.save()
        messages.info(request, 'Information updated')
        return redirect(request.META['HTTP_REFERER'])

    context = {
        'user_profile': user_profile,
        'user_orders': user_orders,
        'count': count,
    }

    return render(request, 'house/profile.html', context)
