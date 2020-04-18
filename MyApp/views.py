import json
from django.http import HttpResponse
from django.shortcuts import render
from MyApp.models import User,Dept,Doctor,Patient,Work,Room,Deal_method,Medicine
#全局变量
ss=""
dict1={}
patient_dept1=0
dept1=""
id1=""
length1=0
diag1=""
info={}
doctor_name1="0"
medicine1=""
num1=0
dict2={}
dict3={}
n=0
id2=0
id3=0
id4=""
id5=""

def test(request):
    if request.method == "GET":
        return HttpResponse("success!")


def new_login(request): # 登入
    if request.method == "GET": # 在地址栏输入new_login执行此功能模块
        return render(request, 'User/new_login.html')
    else: # 点击护士登入时执行此模块
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("password")
        user_result = User.objects.filter(user_name=user_name)
        user_r = Doctor.objects.filter(doctor_name=user_name)
        context = {}
        if len(user_result) == 1: #
            user_password_ = user_result[0].user_passwd
            if user_password == user_password_:
                # user_results = User.objects.all()  # 从user表中获取数据
                context["info"] = "success!"
                if len(user_r) == 0: # 如果在医生表里没有找到相应的记录
                    context["status"] = 0
                else:
                    context["info"] = "身份错误！！！"
                    context["status"] = 3
            else:
                context["info"] = "密码错误！！！"
                context["status"] = 1
        else:
            context["info"] = "用户名不存在！！！"
            context["status"] = 2
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")


def doctor_login(request):# 医生登入判断
    if request.method == "GET":
        return render(request, 'User/new_login.html')
    else:
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("password")
        user_result = User.objects.filter(user_name=user_name)
        user_r = Doctor.objects.filter(doctor_name=user_name)
        context = {}
        if len(user_result) == 1:
            user_password_ = user_result[0].user_passwd
            if user_password == user_password_:
                # user_results = User.objects.all()  # 从user表中获取数据
                if len(user_r) == 1:
                    context["info"] = "登录成功!"
                    context["status"] = 0
                else:
                    context["info"] = "身份错误！！！"
                    context["status"] = 3
            else:
                context["info"] = "密码错误！！！"
                context["status"] = 1
        else:
            context["info"] = "用户名不存在！！！"
            context["status"] = 2
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")


def doctor_regist(request):#医生注册
    if request.method == "GET":
        return render(request, 'User/doctor_regist.html')
    else:
        user_name = request.POST.get("user_name")
        pswd = request.POST.get("password")
        user_result_u = User.objects.filter(user_name=user_name)
        user_result = Doctor.objects.filter(doctor_name=user_name).first()#根据前端输入的姓名在医生表里找到相应的记录
        if user_result is None:
            context = {}
            context["info"] = "没有查询到您的记录"
            context["status"] = 1
            context = json.dumps(context)
            return HttpResponse(context, content_type="application/json")
        doctor_i=user_result.doctor_id   # 通过找到的该条记录获取该医生具体的编号
        doctor_id = request.POST.get("doctor_id")
        context = {}
        if len(user_result_u) == 0:
            if doctor_i==doctor_id:
                context["status"] = 0
                User.objects.create(user_name=user_name, user_passwd=pswd)
            else:
                context["info"] = "您不是医生！！！"
                context["status"] = 1
        else:
            context["info"] = "用户名存在了！！！"
            context["status"] = 2
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")

def guahao(request):
    depts = Dept.objects.all()
    context = json.dumps({"depts": [{"id": val.id, "name": val.dept_name} for val in depts]})
    return HttpResponse(context, content_type="application/json")

def add_patient(request):
    if request.method == "GET":
        patient_id = request.GET.get("patient_id")
        patient_result = Patient.objects.get(pk=int(patient_id))
        context = json.dumps({
            "id": patient_result.id,
            "name": patient_result.patient_name,
            "sex": patient_result.patient_sex,
            "age": patient_result.patient_age,
            "id_card": patient_result.patient_idcard,
            "dept": patient_result.patient_dept.dept_name
        })
        return HttpResponse(context, content_type="application/json")
    else:
        patient_name = request.POST.get('patient_name')
        patient_sex = request.POST.get("patient_sex")
        patient_age = request.POST.get("patient_age")
        patient_telep = request.POST.get("patient_telep")
        patient_idcard = request.POST.get("patient_idcard")
        patient_dept = request.POST.get("patient_dept")
        d = Dept.objects.filter(id=int(patient_dept)).first()
        Patient.objects.create(patient_name=patient_name, patient_sex=patient_sex,patient_idcard=patient_idcard,
                                patient_age=patient_age, patient_telep=patient_telep, patient_dept=d)  # 插入注册的用户信息
        patient_result = Patient.objects.filter(patient_idcard=patient_idcard).first()
        context = json.dumps({
            "id":patient_result.id,
            "name": patient_result.patient_name,
            "sex":patient_result.patient_sex,
            "age":patient_result.patient_age,
            "id_card": patient_result.patient_idcard,
            "dept":patient_result.patient_dept.dept_name
        })
        return HttpResponse(context, content_type="application/json")

def search_p(request):
    depts = Dept.objects.all()
    context = json.dumps({"depts": [{"id": val.id, "name": val.dept_name} for val in depts]})
    return HttpResponse(context, content_type="application/json")

def search_by_patient_name(request):
    patient_name = request.GET.get("patient_name")
    d = Patient.objects.filter(patient_name=patient_name).first()
    if d is None:
        return HttpResponse("{}", content_type="application/json")
    info_dic = {}
    info_dic["门诊号"] = d.id
    global id2
    id2 = d.id
    info_dic["姓名"] = d.patient_name
    info_dic["性别"] = d.patient_sex
    info_dic["年龄"] = d.patient_age
    info_dic["电话"] = d.patient_telep
    info_dic["科室"] = d.patient_dept.dept_name
    context = json.dumps({
        "result_keys": list(info_dic.keys()),
        "result_values": list(info_dic.values()),
    })
    return HttpResponse(context, content_type="application/json")

def search_by_patient_dept(request):
    if request.method == "GET":
        return render(request, 'User/choose.html')
    else:
        patient_dept = request.POST.get("patient_dept")
        patient_infos = Patient.objects.filter(patient_dept=int(patient_dept)).all()
        context = {
            "patient_infos": [
                {
                    "id": val.id,
                    "patient_name": val.patient_name,
                    "patient_sex": val.patient_sex,
                    "patient_age": val.patient_age,
                    "patient_telep": val.patient_telep,
                    "dept_name": val.patient_dept.dept_name
                } for val in patient_infos
            ]
        }
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")
def search_d(request):
    depts = Dept.objects.all()
    context = json.dumps({"depts": [{"id": val.id, "name": val.dept_name} for val in depts]})
    return HttpResponse(context, content_type="application/json")

def search_by_doctor_name(request):
    doctor_name = request.GET.get("doctor_name")
    d = Doctor.objects.filter(doctor_name=doctor_name).first()
    if d is None:
        return HttpResponse('{}', content_type="application/json")
    global doctor_name1,id4
    doctor_name1 = d.doctor_name
    info_dic = {}
    info_dic["医生编号"] = d.doctor_id
    info_dic["姓名"] = d.doctor_name
    info_dic["性别"] = d.doctor_sex
    info_dic["年龄"] = d.doctor_age
    info_dic["电话"] = d.doctor_telep
    info_dic["职位"] = d.doctor_position
    info_dic["科室"] = d.doctor_dept.dept_name
    id4=d.doctor_name
    context = json.dumps({
        "result_keys": list(info_dic.keys()),
        "result_values": list(info_dic.values()),
    })
    return HttpResponse(context, content_type="application/json")

def search_by_doctor_dept(request):
    """
    <td><span>{{ doctor_info.doctor_id }}</span></td>
    <td><span>{{ doctor_info.doctor_name }}</span></td>
    <td><span>{{ doctor_info.doctor_sex }}</span></td>
    <td><span>{{ doctor_info.doctor_age }}</span></td>
    <td><span>{{ doctor_info.doctor_telep }}</span></td>
    <td><span>{{ doctor_info.doctor_position }}</span></td>
    <td><span>{{ doctor_info.doctor_dept.dept_name}}</td>
    :param request:
    :return:
    """
    doctor_dept = request.GET.get("doctor_dept")
    global id3
    id3=doctor_dept
    doctor_infos = Doctor.objects.filter(doctor_dept=int(doctor_dept)).all()
    context = {
        "doctor_infos": [
            {
                "doctor_id": val.doctor_id,
                "doctor_name": val.doctor_name,
                "doctor_sex": val.doctor_sex,
                "doctor_age": val.doctor_age,
                "doctor_telep": val.doctor_telep,
                "doctor_position": val.doctor_position,
                "dept_name": val.doctor_dept.dept_name
            } for val in doctor_infos
        ]
    }
    return HttpResponse(context, content_type="application/json")

def work1(request):
    """
        <th>{{work_time_result.work_doctor_dept.dept_name }}</th>
        <th>{{work_time_result.work_doctor_name }}</th>
        <th>{{work_time_result.work_doctor_id.doctor_id}}</th>
        <th>{{work_time_result.work_time}}</th>
    :param request:
    :return:
    """
    global id3
    work_time_results = Work.objects.filter(work_doctor_dept=int(id3))
    context = json.dumps({
        "work_time_results": [
            {
                "dept_name": val.work_doctor_dept.dept_name,
                "work_doctor_name": val.work_doctor_name,
                "doctor_id": val.work_doctor_id.doctor_id,
                "work_time": val.work_time
            } for val in work_time_results
        ],
    })
    return HttpResponse(context, content_type="application/json")

def work2(request):
    global id4
    work_time_results = Work.objects.filter(work_doctor_name=id4)
    context = json.dumps({
        "work_time_results": [
            {
                "dept_name": val.work_doctor_dept.dept_name,
                "work_doctor_name": val.work_doctor_name,
                "doctor_id": val.work_doctor_id.doctor_id,
                "work_time": val.work_time
            } for val in work_time_results
        ]
    })
    return HttpResponse(context, content_type="application/json")

def alter(request):
    global id5
    if request.method=="GET":
        global doctor_name1
        d = Doctor.objects.filter(doctor_name=doctor_name1).first()
        id5 = d.doctor_id
        context = json.dumps({
            "doctor_id":d.doctor_id,
            "doctor_name": d.doctor_name,
            "doctor_sex": d.doctor_sex,
            "dept_name": d.dept_name,
            "doctor_age": d.doctor_age,
            "doctor_telep": d.doctor_telep,
            "doctor_position": d.doctor_position
        })
        return HttpResponse(context, content_type="application/json")

def alter_work_time(request):
    alter_value=request.GET.get("alter_value")
    alter_value_to=request.GET.get("alter_value_to")
    Work.objects.filter(work_doctor_name=id4,work_time=alter_value).update(work_time=alter_value_to)
    work_time_results = Work.objects.filter(work_doctor_name=id4)
    context = json.dumps({
        "work_time_results": [
            {
                "dept_name": val.work_doctor_dept.dept_name,
                "work_doctor_name": val.work_doctor_name,
                "doctor_id": val.work_doctor_id.doctor_id,
                "work_time": val.work_time
            } for val in work_time_results
        ]
    })
    return HttpResponse(context, content_type="application/json")
def diagnosis_detail(request):
    global id2
    if request.method=="GET":
        d = Patient.objects.filter(id=id2).first()
        c = Deal_method.objects.filter(deal_patient_id=id2).first()
        if c is None:
            return HttpResponse("该病人暂未就诊，无就诊详情！")
        else:
            info_dic = {}
            info_dic["id"] = d.id
            info_dic["patient_name"] = d.patient_name
            info_dic["room_id"] = c.deal_room_id
            info_dic["diagnosis_result"] = c.diagnosis_result
            info_dic["medicine_detail"] = c.medicine_detail
            info_dic["doctor_suggestions"] = c.doctor_suggestions
            info_dic["deal_doctor_name"] = c.deal_doctor_name
            info_dic["diagnosis_time"] = c.diagnosis_time
            info_dic =json.dumps(info_dic)
            return HttpResponse(info_dic, content_type="application/json")

def medicine(request):
    """
    medicine.medicine_name
    medicine.medicine_num
    """
    medicine_inform = Medicine.objects.all()
    context = json.dumps({
        "medicine_inform": [
            {
                "medicine_name": val.medicine_name,
                "medicine_num": val.medicine_num
            } for val in medicine_inform
        ],
    })
    return HttpResponse(context, content_type="application/json")

def search_medicine(request):
    global medicine1,num1,dict2,dict3
    medicine_name = request.POST.get("medicine_name")
    d = Medicine.objects.filter(medicine_name=medicine_name).first()
    if d is None:
        return HttpResponse("{}", content_type="application/json")
    info_dic = {}
    info_dic["药品名称"] = d.medicine_name
    medicine1=d.medicine_name
    info_dic["药品数量"] = d.medicine_num
    num1=int(d.medicine_num)#最开始显示的时候的药品数量
    medicine_inform = Medicine.objects.all()
    context = {
        "result_keys": list(info_dic.keys()),
        "result_values": list(info_dic.values()),
        "medicine_inform": [
            {
                "medicine_name": val.medicine_name,
                "medicine_num": val.medicine_num
            } for val in medicine_inform
        ],
        "medicine": medicine_name
    }
    dict2=context
    context = json.dumps(context)
    return HttpResponse(context, content_type="application/json")

def add_medicine(request):
    global medicine1, num1
    if request.method == "GET":
        context = json.dumps({
            "medicine": medicine1
        })
        return HttpResponse(context, content_type="application/json")
    else:
        num = request.POST.get("number")
        M=Medicine.objects.filter(medicine_name=medicine1).first()
        numbers=M.medicine_num
        num_result = numbers + int(num)
        Medicine.objects.filter(medicine_name=medicine1).update(medicine_num=num_result)
        context = json.dumps({
            "num": num,
            "medicine": medicine1
        })
        return HttpResponse(context, content_type="application/json")

def take_medicine(request):
    global medicine1,num1,n
    if request.method == "GET":
        context=json.dumps({
            "medicine": medicine1
        })
        return HttpResponse(context, content_type="application/json")
    else:
        number=request.POST.get("number")
        M = Medicine.objects.filter(medicine_name=medicine1).first()
        numbers = M.medicine_num
        num_result=numbers-int(number)
        Medicine.objects.filter(medicine_name=medicine1).update(medicine_num=num_result)
        context=json.dumps({
            "num":number,
            "medicine":medicine1
        })
        return HttpResponse(context, content_type="application/json")

def add_medicine_type(request):
    m_name=request.POST.get("m_name")
    m_num=request.POST.get("m_num")
    Medicine.objects.create(medicine_name=m_name,medicine_num=m_num)
    return HttpResponse("{}", content_type="application/json")

def display(request):
    """
    <td>{{patient_info.patient_name}}</td>
    <td>{{patient_info.patient_sex}}</td>
    <td>{{patient_info.patient_age}}</td>
    <td>{{patient_info.patient_telep}}</td>
    <td>{{patient_info.patient_dept.dept_name}}</td>
    :param request:
    :return:
    """
    global id1,info
    patient_id=request.POST.get("patient_id")
    id1=patient_id
    patient_info = Patient.objects.filter(id=int(patient_id)).first()
    patient_all_id = Patient.objects.all()
    medicines = Medicine.objects.all()
    context = {
            "status": 1,
            "patient_all_id": [{"id": val.id} for val in patient_all_id],
            "patient_info": [{
                "patient_name": val.patient_name,
                "patient_sex": val.patient_sex,
                "patient_age": val.patient_age,
                "patient_telep": val.patient_telep,
                "dept_name": val.patient_dept.dept_name
            } for val in patient_info],
            "medicines": [{"medicine_name": val.medicine_name} for val in medicines],
            "patient_id":id1,
            "length": length1
    }
    info["information"]=context["patient_info"]
    info["medicine"]=context["medicines"]
    context = json.dumps(context)
    return HttpResponse(context, content_type="application/json")

def display1(request):
    test=request.POST.get("test")
    Doctor_results = Doctor.objects.all()
    Dept_results = Dept.objects.all()
    if request.method == "POST":
        context = {
        "status":2,
        "Doctor_results": Doctor_results,
        "Dept_results": Dept_results,
        }
        return render(request, 'Doctor/display.html',context=context)
    else:
        Doctor_results = Doctor.objects.all()
        context = {
            "status":1,
            "Doctor_results": Doctor_results,
        }
        return render(request, 'Doctor/display.html', context=context)

def doctor_choose(request):
    return render(request,'Doctor/doctor_choose.html')

def patient_manage(request):
    global length1
    """
    patient_name = models.CharField(max_length=20)#病人姓名
    patient_sex = models.CharField(max_length=10)#病人性别
    patient_age = models.CharField(max_length=10)#病人年龄
    patient_telep = models.CharField(max_length=20)#病人电话
    patient_idcard = models.CharField(max_length=30)#病人身份证号
    patient_dept
    """
    if request.method == "GET":
        patient_all = Patient.objects.all()
        length=len(patient_all)
        length1=length
        medicines = Medicine.objects.all()
        context = {
            "patient_all_id": [{
                "id": val.id
            } for val in patient_all],
            "medicines": [val.medicine_name for val in medicines],
            "length": length,
            "flag":1,
            "status":2
        }
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")


def insert_deal_method(request):
    patient_id=request.POST.get("patient_id") # 外键
    diagnosis_result=request.POST.get("diagnosis_result")
    room_id=request.POST.get("room_id")
    doctor_suggestions=request.POST.get("doctor_suggestions")
    diagnosis_time=request.POST.get("diagnosis_time")
    doctor_name=request.POST.get("doctor_name")
    medicine1=request.POST.get("medicine1", "")
    medicine2=request.POST.get("medicine2", "")
    medicine3=request.POST.get("medicine3", "")
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    num3 = request.POST.get("num3")
    medicine_detail=""
    if medicine1.strip()!="":
        medicine_detail = "1、"+medicine1 + "  " + num1 + "盒" + "\n"
        if medicine2.strip()!="":
            medicine_detail = medicine_detail+"2、"+medicine2 + "  " + num2 + "盒" + "\n"
            if medicine3.strip() != "":
                medicine_detail = medicine_detail+"3、"+medicine3 + "  " + num3 + "盒" + "\n"
            else:
                pass
        else:
            pass
    else:
        pass
    d = Patient.objects.filter(id=int(patient_id)).first()
    Deal_method.objects.create(
        deal_patient_id=d,
        diagnosis_result=diagnosis_result,
        deal_room_id=room_id,
        deal_doctor_name=doctor_name,
        diagnosis_time=diagnosis_time,
        medicine_detail=medicine_detail,
        doctor_suggestions=doctor_suggestions
    )  # 插入注册的用户信息
    p = Patient.objects.filter(id=int(patient_id)).first()
    Room.objects.filter(room_patient_dept=p.patient_dept,room_id=room_id).update(
        room_patient_id=patient_id, room_patient_name=d.patient_name)  # 更新数据
    return HttpResponse({"res": "success"}, content_type="application/json")

def print_diagnosis_results(request):
    return render(request,'Doctor/print_diagnosis_results.html')
def out_hospital(request):
    global dept1
    if request.method == "GET":
        depts = Dept.objects.all()
        context = [{"id": val.id, "name": val.dept_name} for val  in depts]
        context = json.dumps({"depts": context})
        return HttpResponse(context, content_type="application/json")
    else:
        depts = Dept.objects.all()
        out_id=request.POST.get("out_id")#out_id是房号
        Room.objects.filter(room_patient_dept=int(dept1) ,room_id=out_id).update(room_patient_name="空",
            room_patient_id="空")  # 更新数据
        dept_room_infos = Room.objects.filter(room_patient_dept=int(patient_dept1))
        context = json.dumps({
            "depts": [{"id": val.id, "name": val.dept_name} for val in depts],
            "dept_room_infos": [{"id": val.room_id, "name": val.room_patient_name} for val in dept_room_infos],
        })
        return HttpResponse(context, content_type="application/json")

def search_room(request):
    depts = Dept.objects.all()
    global patient_dept1,dept1
    patient_dept1 = request.POST.get("patient_dept")
    dept1=patient_dept1
    dept_room_infos = Room.objects.filter(room_patient_dept=int(patient_dept1))
    context = json.dumps({
        "depts": [{"id": val.id, "name": val.dept_name} for val in depts],
        "dept_room_infos": [{"id": val.room_id, "name": val.room_patient_name} for val in dept_room_infos],
    })
    return HttpResponse(context, content_type="application/json")

def work_time_search(request):
    global dict1
    if request.method == "GET":
        depts = Dept.objects.all()
        doctor_results=Doctor.objects.all()
        context = {
            "doctor_results": [{"id": val.id, "doctor_id": val.doctor_id} for val in doctor_results],
            "depts": [{"id": val.id, "name": val.dept_name} for val in depts],
        }
        dict1=context
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")

    else:
        work_dept=request.POST.get("work_dept")
        d={
            "1":"骨科","2":"烧伤科","3":"皮肤科","4":"精神科","5":"儿科","6":"内科","7":"外科",
        }
        work_time_results=Work.objects.filter(work_doctor_dept=int(work_dept))
        context={
            "work_time_results":[{"dept_name": val.work_doctor_dept.dept_name,
                                  "work_doctor_name": val.work_doctor_name,
                                  "doctor_id": val.work_doctor_id.doctor_id,
                                  "work_time": val.work_time} for val in work_time_results],
            "work_dept":d[work_dept],
        }
        dict1=context
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")

def distribute_room(request):
    global diag1,info
    if request.method == "GET":
        depts = Dept.objects.all()
        diagnosis_result=request.GET.get("diagnosis_result")
        diag1=diagnosis_result
        context = [{"id": val.id, "name": val.dept_name} for val in depts]
        context = json.dumps({"depts": context})
        return HttpResponse(context, content_type="application/json")
    else:
        patient_dept=request.POST.get("patient_dept")
        dept_room_infos=Room.objects.filter(room_patient_dept=int(patient_dept))
        d = {
            "1": "骨科", "2": "烧伤科", "3": "皮肤科", "4": "精神科", "5": "儿科", "6": "内科", "7": "外科",
        }
        dept_room_infos = [{"room_id": val.room_id, "room_name": val.room_patient_name} for val in dept_room_infos]
        context={
            "dept_room_infos": dept_room_infos,
            "patients": d[patient_dept],
        }
        context = json.dumps(context)
        return HttpResponse(context, content_type="application/json")

def back1(request):
    global dict2,medicine1
    d = Medicine.objects.filter(medicine_name=medicine1).first()
    info_dic = {}
    info_dic["药品名称"] = d.medicine_name
    medicine1 = d.medicine_name
    info_dic["药品数量"] = d.medicine_num
    medicine_inform = Medicine.objects.all()
    context = {
        "result_keys": list(info_dic.keys()),
        "result_values": list(info_dic.values()),
        "medicine_inform": medicine_inform,
        "medicine": medicine1
    }
    return render(request,'Medicine/medicine_manage.html',context=context)
def back2(request):
    return render(request,'Medicine/add_type.html')

def back3(request):
    global id5, doctor_name1,id4
    if request.method=="GET":
        d = Doctor.objects.filter(doctor_name=id4).first()
        info_dic = {}
        info_dic["医生编号"] = d.doctor_id
        info_dic["姓名"] = d.doctor_name
        info_dic["性别"] = d.doctor_sex
        info_dic["年龄"] = d.doctor_age
        info_dic["电话"] = d.doctor_telep
        info_dic["职位"] = d.doctor_position
        info_dic["科室"] = d.doctor_dept.dept_name
        id4 = d.doctor_name
        context = {
            "result_keys": list(info_dic.keys()),
            "result_values": list(info_dic.values()),
        }
        return render(request,'Doctor/search_by_doctor_name.html',context=context)
    else:
        age = request.POST.get("age")
        position = request.POST.get("position")
        telep = request.POST.get("telep")
        Doctor.objects.filter(doctor_id=id5).update(doctor_age=age, doctor_position=position, doctor_telep=telep)
        d = Doctor.objects.filter(doctor_name=doctor_name1).first()
        context = json.dumps({
            "doctor_id": d.doctor_id,
            "doctor_name": d.doctor_name,
            "doctor_sex": d.doctor_sex,
            "dept_name": d.dept_name,
            "doctor_age": d.doctor_age,
            "doctor_telep": d.doctor_telep,
            "doctor_position": d.doctor_position
        })
        return HttpResponse(context, content_type="application/json")

def back4(request):
    if request.method == "GET":
        global id4
        d = Doctor.objects.filter(doctor_name=id4).first()
        info_dic = {}
        info_dic["医生编号"] = d.doctor_id
        info_dic["姓名"] = d.doctor_name
        info_dic["性别"] = d.doctor_sex
        info_dic["年龄"] = d.doctor_age
        info_dic["电话"] = d.doctor_telep
        info_dic["职位"] = d.doctor_position
        info_dic["科室"] = d.doctor_dept.dept_name
        id4 = d.doctor_name
        context = {
            "result_keys": list(info_dic.keys()),
            "result_values": list(info_dic.values()),
        }
        return render(request, 'Doctor/search_by_doctor_name.html',context=context)
    else:
        global id3
        doctor_infos = Doctor.objects.filter(doctor_dept=int(id3)).all()
        context = {
            "doctor_infos": doctor_infos
        }
        return render(request, 'Doctor/search_by_doctor_dept.html', context=context)

def return5(request):
    global dict1
    if request.method == "GET":
        return render(request, 'Doctor/doctor_choose.html')
    else:
        doctor_id=request.POST.get("doctor_id")
        d={
            "1":1001,"2":1002,"3":2001,"4":2002,"5":3001,"6":3002,"7":4001,"8":4002,"9":5001,"10":5002,"11":6001,"12":7002,"13":6001,"14":7002,
        }
        work_time=Work.objects.filter(work_doctor_id=int(doctor_id))
        context=json.dumps({
            "work_time": [{"dept_name": val.work_doctor_dept.dept_name,
                           "work_doctor_name": val.work_doctor_name,
                           "doctor_id": val.work_doctor_id.doctor_id,
                           "work_time": val.work_time} for val in work_time],
            "doctor_i":d[doctor_id],
        })
        return HttpResponse(context, content_type="application/json")
