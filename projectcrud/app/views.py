from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages


# Create your views here.
def index(request):
    data = Student.objects.all()
    print(data)
    context = {"data": data}
    return render(request,'index.html',context)

def insertData(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        # Print the form data
        print("Form Data:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")
        
        # Create and save the Student object
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect('/')
    return render(request, 'index.html')

def updateData(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        messages.warning(request, "Data Updated Successfully")
        return redirect('/')
    
    data = Student.objects.get(id=id)
    context = {"data": data}
    return render(request, 'edit.html', context)

def deleteData(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect('/')
   
    return render(request,'delete.html',context)
    
    
def about(request):
    return render(request,'about.html')
